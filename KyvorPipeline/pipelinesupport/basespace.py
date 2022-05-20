import time
import os
import requests as re
import string

from djangoprojects.settings import MEDIA_ROOT


from distutils.util import strtobool
from sqlite3 import IntegrityError


from KyvorPipeline.models import Basespace, Project, Biosample, AnalysisStatus

def usercreds():

    bs_recent_login = Basespace.objects.latest('id')
    pk_of_recent_login = bs_recent_login.id
    current_access_token = bs_recent_login.bs_access_token
    current_bs_email = bs_recent_login.bs_email
    bearer_auth = "Bearer " + str(current_access_token)
    novogene_gc_file = "files/"+str(bs_recent_login.novogene_gcc_id)
    novogene_bed_file = "files/"+str(bs_recent_login.novogene_bed_id)
    fulgent_gc_file = "files/" + str(bs_recent_login.novogene_gcc_id)
    fulgent_bed_file = "files/" + str(bs_recent_login.novogene_bed_id)

    request_headers = {
        "Content-Type": "application/json",
        "User-Agent": "BaseSpaceGOSDK/0.9.3 BaseSpaceCLI/1.2.1",
        "Authorization": bearer_auth
    }

    return_json = {}

    return_json['pk_recent_login'] = pk_of_recent_login
    return_json['bs_email'] = current_bs_email
    return_json['headers'] = request_headers
    return_json['bs_recent_login'] = bs_recent_login
    return_json['novogene_bed'] = novogene_bed_file
    return_json['novogene_gc'] = novogene_gc_file
    return_json['fulgent_bed'] = fulgent_bed_file
    return_json['fulgent_gc'] = fulgent_gc_file

    #return pk_of_recent_login, current_bs_email, request_headers, bs_recent_login

    return return_json

def ValidateBasespace():
    return_data = {}
    #get basespace credentials
    bsCreds = usercreds()

    request_url = "https://api.basespace.illumina.com/v1pre3/users/current"

    req = re.get(request_url, headers=bsCreds["headers"])
    req_status = req.status_code

    if req_status == 200 or req_status == 201:
        req_data = req.json()
        if bsCreds["bs_email"] == req_data["Response"]["Email"]:
            bs_user_id = int(req_data["Response"]["Id"])
            bs_user_created_on = req_data["Response"]["DateCreated"]
            print(bs_user_id)
            #Check the basespace CLI user
            bs_who_am_i_cmd = os.popen("bs whoami")
            bs_who_am_i_list = bs_who_am_i_cmd.read().split("|")
            strip_list = [item.strip() for item in bs_who_am_i_list]
            print(strip_list, type(strip_list))
            cmd_user_id = ""
            for idx, val in enumerate(strip_list):
                if val == "Id":
                    cmd_user_id = int(strip_list[idx + 1])
                    break
            if cmd_user_id != "":
                print(cmd_user_id)
                if bs_user_id == cmd_user_id:
                    # Check Subscription Status
                    subscription_url = "https://api.basespace.illumina.com/v2/users/current/subscription"
                    sub_req = re.get(subscription_url, headers=bsCreds["headers"])
                    sub_status = sub_req.status_code
                    if sub_status == 200 or sub_status == 201:
                        sub_data = sub_req.json()
                        account_active = sub_data["IsActive"]
                        expiration_date= sub_data["ExpirationDate"]
                        if account_active:
                            credits_remaining = sub_data["Wallet"]["ICreditBalance"]
                            if credits_remaining > 25:
                                #update basesapce creds data
                                try:
                                    updateCreds = Basespace(
                                        id=bsCreds["pk_recent_login"],
                                        bs_user_id=bs_user_id,
                                        bs_date_created=bs_user_created_on,
                                        bs_credits=credits_remaining,
                                        bs_expiry_on=expiration_date,
                                        bs_active=account_active
                                    ).save(update_fields=["bs_date_created", "bs_user_id", "bs_credits", "bs_expiry_on",
                                                          "bs_active"])
                                except IntegrityError as ie:
                                    return_data["Status"] = sub_status
                                    return_data["Message"] = ie
                                    return_data["Reference"] = "Basespace validates. But details not saved in basespace creds"
                                    return_data["Type"] = True
                                except ValueError as ve:
                                    return_data["Status"] = sub_status
                                    return_data["Message"] = ve
                                    return_data["Reference"] = "Basespace validates. But details not saved in basespace creds"
                                    return_data["Type"] = True

                                return_data["Status"] = sub_status
                                return_data["Message"] = "Basespace Validated"
                                return_data["Reference"] = "Basespace validated and recent data saved in basespace creds"
                                return_data["Type"] = True
                            else:
                                return_data["Status"] = sub_status
                                return_data["Code"] = "Err01-5"
                                return_data["Message"] = "Not enough credits in basespace"
                                return_data["Reference"] = "Low credits in basespace account. Try creating a new id " \
                                                           "and configure the id in the App "
                                return_data["Type"] = False
                        else:
                            return_data["Status"] = sub_status
                            return_data["Code"] = "Err01-4"
                            return_data["Message"] = "Basespace account Expired"
                            return_data["Reference"] = "Basespace account has been expired. " \
                                                       "Try creating a new id and configure the id in the App"

                            return_data["Type"] = False
                    else:
                        return_data["Status"] = sub_status
                        return_data["Code"] = "Err01-3"
                        return_data["Message"] = "Basespace validation subscription connection failed"
                        return_data["Reference"] = "Check the request url and access_token or maybe internet issue"
                        return_data["Type"] = False
                else:
                    return_reference = "API User Id: " + str(bs_user_id) + " ,CLI User Id: " + str(cmd_user_id) + \
                                       " Check the user credentials used in bs whoami"
                    return_data["Code"] = "Err01-6"
                    return_data["Status"] = req_status
                    return_data["Message"] = "Basespace API and CLI Id's mismatch"
                    return_data["Reference"] = return_reference
                    return_data["Type"] = False
            else:
                return_reference = "API User Id: " + str(bs_user_id) + " ,CLI User Id: " + str(cmd_user_id)
                return_data["Code"] = "Err01-7"
                return_data["Status"] = req_status
                return_data["Message"] = "CLI User id returned empty string"
                return_data["Reference"] = return_reference
                return_data["Type"] = False

        else:
            return_reference = "Recent Email from DB: "+str(bsCreds["bs_email"])+ " ,Email from Basespace: "+str(req_data["Email"])
            return_data["Code"] = "Err01-2"
            return_data["Status"] = req_status
            return_data["Message"] = "Basespace access token mismatch"
            return_data["Reference"] = return_reference
            return_data["Type"] = False
    else:
        return_data["Status"] = req_status
        return_data["Code"] = "Err01-1"
        return_data["Message"] = "Basespace validation connection failed"
        return_data["Reference"] = "Check the request url and access_token or maybe internet issue"
        return_data["Type"] = False

    return return_data


def FastQFormatCheck(fastqFile):
    file_error = []
    #check file extention
    fastqFile = str(fastqFile).split(".txt")[0]
    if not str(fastqFile).endswith("fastq.gz"):
        file_error.append("Extension Error")
        return file_error
    splitFile = str(fastqFile).split('.')[0].split('_')
    print(splitFile)
    print(splitFile[1], len(splitFile))
    if len(splitFile) != 5:
        file_error.append("1. Filename Issue")
    elif str(splitFile[1])[0] != "S":
        file_error.append("2. Filename Issue")
    elif str(splitFile[2])[0] != "L":
        file_error.append("3. Filename Issue")
    elif len(str(splitFile[2])) != 4:
        file_error.append("4. Filename Issue")
    elif str(splitFile[3])[0] != "R":
        file_error.append("5. Filename Issue")
    elif len(str(splitFile[4])) != 3:
        file_error.append("6. Filename Issue")

    return file_error



def ValidateProjectName(name):
    return_data = {}
    # check for the project name in database
    project_count = Project.objects.filter(project_name=name).count()
    if project_count == 0:
        ##check for the project name in basespace
        # Basespace Credential data
        bsCreds = usercreds()
        project_url = "https://api.basespace.illumina.com/v1pre3/users/current/projects"
        params = {
            "Limit": 200,
            "Offset": 0,
            "name": name
        }
        request_headers = bsCreds["headers"]
        req = re.get(project_url, params=params, headers=request_headers)

        res_status = req.status_code
        print(res_status)
        if req.status_code == 200 or req.status_code == 201:
            res_data = req.json()
            project_count = res_data["Response"]["TotalCount"]
            print(project_count)
            if project_count == 0:
                return_data["Status"] = res_status
                return_data["Message"] = "Project not found"
                return_data["Reference"] = "Good to go. Create project, default project with the given name"
                return_data["Type"] = True
                pass
            else:
                # project exists
                return_data["Status"] = res_status
                return_data["Code"] = "Err02-3"
                return_data["Message"] = "Basespace exist with basespace current user id"
                return_data["Reference"] = "We can still create a project by modifying the project name"
                return_data["Type"] = False
        else:
            return_data["Status"] = res_status
            return_data["Code"] = "Err02-2"
            return_data["Message"] = "Basespace project validation connection failed"
            return_data["Reference"] = "Check the request url and access_token or maybe internet issue"
            return_data["Type"] = False
    else:
        return_data["Status"] = 200
        return_data["Code"] = "Err02-1"
        return_data["Message"] = "Project Already Exists"
        return_data["Reference"] = "Given project name is already there in database. " \
                                   "Try using diff id or project itself will rename it into a unique name"
        return_data["Type"] = False
    return return_data


def GetLibrary(biosampleId):
    #get library path to launch applications
    req_url = "https://api.basespace.illumina.com/v2/biosamples/" + str(biosampleId) + "/libraries"
    params = {
        'Limit': 25,
        'offset': 0
    }
    bsCreds = usercreds()
    req_headers = bsCreds["headers"]
    req = re.get(req_url, params=params, headers=req_headers)
    print(req)
    return_data = {}
    if req.status_code in [200,201]:
        res = req.json()
        libraryId = ""
        for item in res["Items"]:
            libraryId = item["LibraryPrep"]["Id"]
            print("Library Id Dude: ",libraryId)
        if libraryId != "":
            return_data["Status"] = req.status_code
            return_data["LibraryId"] = libraryId
            return_data["Message"] = "Library Id Found"
            return_data["Reference"] = req.json()
            return_data["Type"] = True
        else:
            return_data["Status"] = req.status_code
            return_data["Code"] = "Err05-02"
            return_data["Message"] = "Not able to retrieve Library Id"
            return_data["Reference"] = req.json()
            return_data["Type"] = False
    else:
        return_data["Status"] = req.status_code
        return_data["Code"] = "Err05-01"
        return_data["Message"] = "Biosample Id not found"
        return_data["Reference"] = req.json()
        return_data["Type"] = False

    return return_data


def CreateProject(project_name, default_project_name, project_type):
    return_data = {}
    validate = ValidateProjectName(project_name)
    if validate["Type"] is True:
        projectname = project_name
        default_project_name = default_project_name
        # Basespace Credential data
        bsCreds = usercreds()
        basespaceInstance = Basespace.objects.get(id = bsCreds["pk_recent_login"])
        #create project id and save data to database
        req_url = "https://api.basespace.illumina.com/v1pre3/projects"
        data = {
            "Name": projectname,
            "Description": "New Project."
        }
        req_headers = bsCreds["headers"]
        req = re.post(url=req_url, json=data, headers=req_headers)
        res_status = req.status_code
        if res_status in [201, 200]:
            print(req.json())
            res_data = req.json()
            bs_project_id = res_data["Response"]["Id"]
            bs_project_name = res_data["Response"]["Name"]
            bs_project_user = res_data["Response"]["UserOwnedBy"]["Id"]
            bs_project_created_on = res_data["Response"]["DateCreated"]
            try:
                Project.objects.create(
                    project_name=project_name,
                    bs_default_project=default_project_name,
                    bs_project_id=bs_project_id,
                    bs_user_id = basespaceInstance,
                    project_type = project_type
                )
                return_data["Status"] = res_status
                return_data["Message"] = "Project Created. Project Id is " + str(bs_project_id)
                return_data["Reference"] = "Basespace Project Created. Details saved in database"
                return_data["Type"] = True
                print("Yolo")
            except IntegrityError as ie:
                print("IE", ie)
                return_data["Status"] = res_status
                return_data["Code"] = "Err03-2"
                return_data["Message"] = str(ie)
                return_data["Reference"] = "Basespace Project Created. But details not saved in database"
                return_data["Type"] = False
            except ValueError as ve:
                print("VE",ve)
                return_data["Status"] = res_status
                return_data["Code"] = "Err03-3"
                return_data["Message"] = str(ve)
                return_data["Reference"] = "Basespace validates. But details not saved in basespace creds"
                return_data["Type"] = False

            print(return_data)
        else:
            print(req.json())
            print("Connection Error", res_status)
            return_data["Status"] = res_status
            return_data["Code"] = "Err03-1"
            return_data["Message"] = "Connection Error, Please check internet or the requested URL"
            return_data["Reference"] = "Basespace validates. But details not saved in basespace creds"
            return_data["Type"] = False

    return return_data


def CreateBioSample(project_id, sample_type, biosample_path):
    print("Biosample started")
    project_details = Project.objects.get(id=project_id)

    biosample_name = "%s_BS_%s" % (project_details.project_name, sample_type)
    return_data = {}

    # create biosample and upload biosamples
    req_url = "https://api.basespace.illumina.com/v2/biosamples/bulkimport"
    data = {"Preview": "true",
            "ValidationFlags": ["ExistingBioSamplesAsError"],
            "BioSamples":
                [
                    {
                        "BioSampleName": biosample_name,
                        "DefaultProjectName": project_details.project_name
                    }
                ]
            }

    bsCreds = usercreds()
    req_headers = bsCreds["headers"]
    req = re.post(url=req_url, json=data, headers=req_headers)
    res_status = req.status_code
    if res_status in [201, 200]:
        res_data = req.json()
        
        biosample_id = ""
        print(res_data)
        if res_data["TotalErrors"] == 0:
            for biosample in res_data["BioSamples"]:
                biosample_id = biosample["BioSample"]["Id"]

                print("Previous Biosample ID: ", biosample_id)

        if biosample_id != "":
            #Biosample path

            os.chdir(biosample_path)

            # upload_cmd = "bs upload dataset -p "+str(project_details.bs_project_id)+ " --type common.files --concurrency=high --recursive . --biosample-name="+str(biosample_name)
            upload_cmd = "bs upload dataset -p "+str(project_details.bs_project_id)+ " --recursive . --biosample-name="+str(biosample_name)

            #old command
            #bs upload dataset -p str(264362101) --recursive . --biosample-name=str(biosample_name) -vvvv

            uploaddata = os.popen(upload_cmd)
            print(upload_cmd)
            print('Data uploading')
            upload = uploaddata.read()
            time.sleep(150)
            print("Upload Status", upload)
            if "100.00" in upload:
                print("Upload Completed dude")

                # get biosample ID
                req_url = "https://api.basespace.illumina.com/v2/biosamples"
                params = {
                    'limit': 25,
                    'offset': 0,
                    'projectId': project_details.bs_project_id,
                    'sortBy': 'DateModified',
                    'sortDir': 'desc'
                }
                req = re.get(url=req_url, params=params, headers=req_headers)
                print(req)
                print(req.status_code, req.json())
                libraryData = "Empty"
                if req.status_code in [200, 201]:
                    res_data = req.json()

                    for item in res_data["Items"]:
                        print(item["Id"])
                        bsId = str(item["Id"])

                        print("Changed Biosample ID: ", bsId)
                        # get library prep id
                        libraryData = GetLibrary(bsId)
                        
                    print("Library Data", libraryData)
                    if libraryData["Type"] == True:
                        library_id = libraryData["LibraryId"]
                        print("LibraryID Yes", libraryData)
                    else:
                        print("LibraryID No", libraryData)
                        print(libraryData["Message"], libraryData["Reference"])
                        library_id = "1014015"

                    print("Biosample Id to Save: ", biosample_id, " BS ID: ", bsId)
                    ##save biosample in model
                    Biosample.objects.create(
                        project_id=project_details,
                        biosample_id=bsId,
                        biosample_type=sample_type,
                        biosample_name=biosample_name,
                        biosample_path=biosample_path,
                        library_id=library_id
                    )

                    #updateBiosampleId = BioSamples.objects.filter(id=saveBs.id).update(biosampleId=bsId,libraryId=library_id)
                    print(bsId, project_details)

                    return_data["Status"] = req.status_code
                    return_data["Message"] = "Biosample Created and biosamples uploaded"
                    return_data["Reference"] = req.json()
                    return_data["Type"] = True

                else:
                    return_data["Status"] = 200
                    return_data["Code"] = "Err04-05"
                    return_data["Message"] = "Failed to get biosample Id"
                    return_data["Reference"] = req.json()
                    return_data["Type"] = False
            else:
                return_data["Status"] = 200
                return_data["Code"] = "Err04-04"
                return_data["Message"] = "Failed to upload biosample"
                return_data["Reference"] = "Check the CLI cmd" + str(upload_cmd)
                return_data["Type"] = False
        else:
            return_data["Status"] = 200
            return_data["Code"] = "Err04-03"
            return_data["Message"] = "Failed to create biosample."
            return_data["Reference"] = req.json()
            return_data["Type"] = False
    else:
        return_data["Status"] = req.status_code
        return_data["Code"] = "Err04-02"
        return_data["Message"] = "Not able to create biosample name"
        return_data["Reference"] = req.json()
        return_data["Type"] = False

    return return_data

def LaunchDSP(project_key, sample_type):
    print(project_key)

    projectData = Project.objects.get(id=project_key)
    biosampleData = projectData.biosample_set.all()

    print(projectData, biosampleData)

    biosampleTypes = []

    for bs in biosampleData:
        if bs.biosample_type == "TO":
            tumorSamplePath = "biosamples/"+str(bs.biosample_id)+"/librarypreps/"+str(bs.library_id)
            biosampleTypes.append(bs.biosample_type)
        elif bs.biosampleType == "NO":
            normalSamplePath = bs.biosampleId
            biosampleTypes.append(bs.biosample_type)

    if "NO" in biosampleTypes:
        app_session_name = projectData.project_name + "_DSP_" + "TN"
        analysis_type = "DSP-TN"
    else:
        app_session_name = projectData.project_name + "_DSP_" + "TO"
        analysis_type = "DSP-TO"

    projectPath = "projects/"+str(projectData.bs_project_id)

    data = {
        "AutoStart": "true",
        "InputParameters": {
            "app-session-name": app_session_name,
            "bai_checkbox": "1",
            "dupmark_checkbox": "1",
            "ffpe_checkbox": "1",
            "ht-ref": "hg38-altaware-cnv-anchor.v7",
            "input_list.tumor-sample": [tumorSamplePath],
            "output_format": "BAM",
            "pipeline-mode": "1",
            "project-id": projectPath,
        },
        "Name": app_session_name,
        "StatusSummary": "API Launch"
    }

    bsCreds = usercreds()
    req_headers = bsCreds["headers"]

    dsp_url = "https://api.basespace.illumina.com/v2/applications/8985978/launch"
    req = re.post(dsp_url, json=data, headers=req_headers)
    print(req.status_code)
    print(req.json())
    resp_json = req.json()

    analysis_type = "DSP_"+str(sample_type)


    #save analysis status
    saveAnalysis = AnalysisStatus.objects.create(
        analysis_type=analysis_type,
        analysis_ref_id=projectData,
        analysis_status="Pass",
        analysis_description="DSP TO Project Launched",
        bs_analysis_id=resp_json["Id"],
        bs_analysis_status=resp_json["ExecutionStatus"],
        bs_analysis_name=resp_json["Name"]
    )

    return resp_json["Id"]

def LaunchDE(project_key, sample_type, lab):
    print(project_key)

    projectData = Project.objects.get(id=project_key)
    biosampleData = projectData.biosample_set.all()

    bsCreds = usercreds()
    req_headers = bsCreds["headers"]

    biosampleTypes = []
    for bs in biosampleData:
        if bs.biosample_type == "TO":
            tumorSamplePath = "biosamples/" + str(bs.biosample_id) + "/librarypreps/" + str(bs.library_id)
            biosampleTypes.append(bs.biosample_type)
        elif bs.biosample_type == "NO":
            normalSamplePath = bs.biosample_id
            biosampleTypes.append(bs.biosample_type)

    if "NO" in biosampleTypes:
        app_session_name = projectData.project_name + "_DE_" + "NO"
        analysis_type = "NO"
    else:
        app_session_name = projectData.project_name + "_DE_" + "TO"
        analysis_type = "TO"

    projectPath = "projects/" + str(projectData.bs_project_id)

    #bed and gc files
    if lab == "Novogene":
        bed_file = bsCreds["novogene_bed"]
        gc_file = bsCreds["novogene_gc"]
    elif lab == "Fulgent":
        bed_file = bsCreds["fulgent_bed"]
        gc_file = bsCreds["fulgent_gc"]
        
    print(bed_file, gc_file, "gc_file")

    data = {
      "AutoStart": "true",
      "InputParameters": {
        "annotation-source": "refseq",
        "app-session-name": app_session_name,
        "automation-sex": "unknown",
        "bait_bed_default_or_custom": "default",
        "cnv-baseline-id": gc_file,
        "cnv-filter-qual": "50.0",
        "cnv_checkbox": "1",
        "cnv_gcbias_checkbox": "1",
        "cnv_segmentation_mode": "cbs",
        "dupmark_checkbox": "1",
        "fixed-bed": "custom",
        "ht-ref": "hg19-altaware-cnv-anchor.v7",
        "input_list.sample-id": [
          tumorSamplePath
        ],
        "input_list.sex": [
          "unknown"
        ],
        "pipeline-mode": "1",
        "project-id": projectPath,
        "qc-coverage-region-padding-2": "150",
        "sv_checkbox": "1",
        "target_bed_id": bed_file,
        "vc-af-call-threshold": "1",
        "vc-af-filter-threshold": "5",
        "vc-target-bed-padding": "0",
        "vc-type": "1",
        "vcf_or_gvcf": "GVCF"
      },
      "Name": app_session_name,
      "StatusSummary": "CLI Launch"
    }



    de_url = "https://api.basespace.illumina.com/v2/applications/8976969/launch"
    req = re.post(de_url, json=data, headers=req_headers)
    print(req.status_code)
    print(req.json())
    resp_json = req.json()




    # save analysis status
    """
    saveAnalysis = AnalysisStatus.objects.create(
        analysisName=app_session_name,
        analysisType=analysis_type,
        analysisStatus=resp_json["ExecutionStatus"],
        analysisId=resp_json["Id"],
        analysisURL=resp_json["Href"],
        project=Projects.objects.get(id=projectKey)
    )

    """

    saveAnalysis = AnalysisStatus.objects.create(
        analysis_type=analysis_type,
        analysis_ref_id=projectData,
        analysis_status="Pass",
        analysis_description="DE TO Project Launched",
        bs_analysis_id= resp_json["Id"],
        bs_analysis_status= resp_json["ExecutionStatus"],
        bs_analysis_name=resp_json["Name"]
    )

    return resp_json["Id"]

def checkAnalysisStatus(project_key, analysis_id):
    projectData = Project.objects.get(id=project_key)
    bs_project_id = projectData.bs_project_id

    bsCreds = usercreds()
    req_headers = bsCreds["headers"]

    params = {
        "AutoStart": "true",
        "Limit": 200,
        "Offset": 0,
        "OutputProjects": bs_project_id
    }

    analysis_url = "https://api.basespace.illumina.com/v2/appsessions"
    req = re.get(analysis_url, params=params, headers=req_headers)
    res_data = req.json()

    for item in res_data["Items"]:
        print("Analysis ID" ,analysis_id)
        if str(analysis_id) == str(item["Id"]):
            updateStatus = AnalysisStatus.objects.get(bs_analysis_id=str(analysis_id))
            print("Checking Out", updateStatus, updateStatus.bs_analysis_status)
            updateStatus.bs_analysis_status = item["ExecutionStatus"]
            updateStatus.save(
                update_fields=['bs_analysis_status']
            )
            return item["ExecutionStatus"]
