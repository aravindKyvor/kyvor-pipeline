from operator import truediv
import regex as eg
from pandas import json_normalize
import os
import requests as re
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1
import glob
import regex
import numpy as np
import pandas as pd
import json
import xlrd
from selenium import webdriver
import yaml
from jsonschema import draft201909_format_checker
from numpy import int0
import pandas as pd
import sys
import time
import excel2json
from pandas import reset_option
import requests
import requests as re
from sqlite3 import IntegrityError
from django.http.response import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
from KyvorPipeline.pipelinesupport.CNVkit_run import RunCNVkit
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from djangoprojects.settings import MEDIA_ROOT
from django.http import HttpResponseRedirect
from .models import *
from .serializer import *
from django.http import HttpResponse
from KyvorPipeline.functions import handle_uploaded_file
from .forms import PipelineToForm
from rest_framework.parsers import FileUploadParser
from .pipelinesupport import basespace, msisensor, CurationV3
from .pipelinesupport.DSP import CurationDSP
from .pipelinesupport.DE import CurationDE
from .pipelinesupport.findfile import filepath
from .pipelinesupport.clinicaltrials import clinicalLauncher
# from .pipelinesupport.gdriveUpload import uploadProject
from .pipelinesupport.ichorCNA import RunIchorCNA
import openpyxl
from .pipelinesupport.annotsv import RunAnnotsv
from .pipelinesupport.annovar import RunAnnovar
from .pipelinesupport.basespace import ValidateProjectName, usercreds, GetLibrary
from .pipelinesupport.basespace import CreateProject
from .pipelinesupport.basespace import CreateBioSample
from .pipelinesupport.basespace import LaunchDSP
from .pipelinesupport.basespace import LaunchDE
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from .pipelinesupport.CurationV3 import curation

from .pipelinesupport.msisensor import RunMsiSensorTO
from .forms import PipelineToForm
from .pipelinesupport.basespace import CreateProject
from pathlib import Path
from threading import Thread
import multiprocessing as mp
import fnmatch
import jsonpickle
from json import JSONEncoder
from .pipelinesupport.reports import vus_results,process_clilical_files,FDA_automated_results
# Create your views here.


class BasespaceViewSet(viewsets.ModelViewSet):
    queryset = Basespace.objects.all().order_by('id')
    serializer_class = BasespaceSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer


class BiosampleViewSet(viewsets.ModelViewSet):
    queryset = Biosample.objects.all().order_by('id')
    serializer_class = BiosampleSerializer


class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = AnalysisStatus.objects.all().order_by('id')

    serializer_class = AnalysisSerializer


class AnalysisDetailView(RetrieveAPIView):
    queryset = AnalysisStatus.objects.all()
    serializer_class = AnalysisSerializer


class Patient_Portal(viewsets.ModelViewSet):
    queryset = PatientPortal.objects.all().order_by('-id')
    serializer_class = PortalSerializer


class PipelineTO(APIView):
    parser_class = (FileUploadParser,)
    http_method_names = ['get', 'head', 'post']

    def post(self, request, *args, **kwargs):
        self.http_method_names.append("GET")

        # libraryData = basespace.GetLibrary(415497083)
        # print(libraryData)

        # launchDE = basespace.LaunchDE(148,"TO", lab="Novogene")
        # checkAnalysis = basespace.checkAnalysisStatus(28, 423654261)
        # checkAnalysis2 = basespace.checkAnalysisStatus(28, 423732341)
        # print(checkAnalysis, checkAnalysis2)
        # LaunchPipelineDSP = DSP.CurationDSP(project_key=31, analysis_id=424128772)
        # LaunchMsi = msisensor.RunMsiSensorTO("/root/basespace/Projects/INDTNA28221_v4_13/AppSessions/INDTNA28221_v4_13_DSP_TO/AppResults.253992751.INDTNA28221_v4_13_BS_TO/Files/INDTNA28221_v4_13_BS_TO.bam", "/root/DjangoProjects/djangoProject/media/INDTNA28221_v4_14/MSI/INDTNA28221_v4_14")

        # LaunchDE = CurationDE(project_key=44, analysis_id=425696276)
        # sys.exit()

        # sv_local_vcf_file = "/root/basespace/Projects/INDKAA82901_test10/AppResults/INDKAA82901_test10_BS_TO%20%282%29/Files/INDKAA82901_test10_BS_TO.sv.vcf.gz"
        # annotated_files_folder = "/root/DjangoProjects/djangoprojects/media/INDKAA82901_test10/Annotated_Files/Annovar/"

        # initiate_annotsv_sv = RunAnnotsv(sv_local_vcf_file,annotated_files_folder, "SV")

        # de_bam_path = "/root/basespace/Projects/INDTNAN55362/AppSessions/INDTNA55362_DE_TO/AppResults.246718506.INDTNA55362_BS_TO/Files/INDTNA55362_BS_TO.bam"
        # LaunchIchorCNA = RunIchorCNA(de_bam_path, "/root/ichorCNA_test/", "TO")
        # sys.exit()
        """
        de_folder = Path.joinpath(
            Path(MEDIA_ROOT), "INDTNA28221_v4_23", "DE_Outputs")
        dsp_folder = Path.joinpath(
            Path(MEDIA_ROOT), "INDTNA28221_v4_23", "DSP_Outputs")

        sv_file_for_ct = filepath(str(de_folder), "SVPASS_2455_Gene_Alias")
        cnv_file_for_ct = filepath(str(de_folder), "CNV_PASS_2455_Gene_Alias")
        dsp_file_for_ct = filepath(
            str(dsp_folder), "EES_PASS_NS,FS,SGL_2455GeneAlias")


        # create folder for Clinical Trials
        ct_folder = Path.joinpath(
            Path(MEDIA_ROOT), "INDTNA28221_v4_23", "ClinicalTrials")
        os.makedirs(ct_folder, exist_ok=True)
        cancer_type = "Solid Tumor, Metastatic Cancer"
        launchCT = clinicalLauncher(sv_file_for_ct, cnv_file_for_ct, dsp_file_for_ct, cancer_type,
                                    "INDTNA28221_v4_23", str(ct_folder))
        sys.exit()


        cme_path = "/root/annovar/humandb/CosmicMutantExport.tsv"
        cge_path = "/root/CurationV4/cancer_gene_census.csv"
        dcb_file = "/root/CurationV4/INTEGRATED_DCP.xlsx"
        multianno_txt_file = "/root/DjangoProjects/djangoProject/media/INDTNA28221_v4_16/Annotated_Files/Annovar/TO/INDTNA28221_v4_16_BS_TO_multianno.hg38_multianno.txt"
        curation_output_folder  = "/root/DjangoProjects/djangoProject/media/INDTNA28221_v4_16/Annotated_Files/Annovar/TO/"

        curation_program_to = CurationV3.curation(multianno_txt_file, cme_path, cge_path, "",
                                                  str(curation_output_folder), dcb_file)

        print(curation_program_to)
        """
        # launchPipelineDE = DE.CurationDE(project_key=36, analysis_id=425055631)
        # sys.exit()

        project_name = request.data["project_name"]

        default_project_name = project_name
        cancer_type = request.data["project_cancer_type"]
        rerun = request.data['project_rerun']

        # project_path = Path.joinpath(Path(MEDIA_ROOT), project_name)
        # project_path = "/root/INDTNA26620/"
        # upload_gdrive = uploadProject(project_path, "Raw")
        # sys.exit()
        get_projects = Project.objects.filter(bs_default_project=project_name)

        if len(get_projects) != 0:
            if rerun is True:
                default_project_name = project_name
                project_name = project_name + \
                    str("_re_")+str(get_projects.count()+1)
            else:
                return Response("Project already exists. Please check Rerun to proceed", status=400)
        else:
            # check Basespace Logins
            basespace.usercreds()
            # check project id in basespace
            validate = basespace.ValidateBasespace()
            if validate["Status"] == 200 or validate["Status"] == 201:
                # Check Fastq file format
                formData = request.data

                postError = []
                fileError = False
                for files in request.FILES:
                    validateFasq = basespace.FastQFormatCheck(formData[files])
                    if len(validateFasq) > 0:
                        fileError = True
                        break

                if fileError == True:
                    postError.append(True)
                    return Response(validateFasq, status=500)

                # create project folder in media

                project_path = Path.joinpath(Path(MEDIA_ROOT), project_name)

                biosample_folder = Path.joinpath(
                    Path(MEDIA_ROOT), project_name, "Biosamples", "FastQz", "TO")

                annotsv_folder = Path.joinpath(
                    Path(MEDIA_ROOT), project_name, "Biosamples", "VCFs", "DE", "TO")
                os.makedirs(biosample_folder)
                os.makedirs(annotsv_folder)

                # Upload Files
                for files in request.FILES:
                    file_object = formData[files]
                    file_name = file_object.name
                    file_content_type = file_object.content_type
                    file_size = file_object.size

                    with open(str(biosample_folder) + "/" + file_name, 'wb+') as f:
                        for chunk in file_object.chunks():
                            f.write(chunk)

                print("Move Extra Fastq")
                time.sleep(10)
                print('TimesUp')
                # Create Project
                createProject = basespace.CreateProject(
                    project_name, default_project_name, "DSP-TO")

                currentProject = Project.objects.latest('id')

                if createProject["Type"] == True:
                    # create Biosamples
                    createBiosamples = basespace.CreateBioSample(project_id=currentProject.id, sample_type="TO",
                                                                 biosample_path=biosample_folder)

                    if createBiosamples["Type"] == True:
                        print("Biosample Uploaded Successfully")

                        launchDSP = basespace.LaunchDSP(
                            project_key=currentProject.id, sample_type="TO")
                        launchDE = basespace.LaunchDE(
                            project_key=currentProject.id, sample_type="TO", lab="Novogene")

                        # Check for status every 5 mins

                        # Do multi processing here
                        p1 = mp.Process(target=CurationDSP, args=(
                            currentProject.id, launchDSP, ))
                        p2 = mp.Process(target=CurationDE, args=(
                            currentProject.id, launchDE, ))

                        # LaunchPipelineDSP = DSP.CurationDSP(project_key=currentProject.id, analysis_id=launchDSP)
                        # launchPipelineDE = DE.CurationDE(project_key=currentProject.id, analysis_id=launchDE)

                        p1.start()
                        p2.start()

                        p1.join()
                        p2.join()

                        print("Done")

                        # Start Clinical Trials
                        de_folder = Path.joinpath(
                            Path(MEDIA_ROOT), currentProject.project_name, "DE_Outputs")
                        dsp_folder = Path.joinpath(
                            Path(MEDIA_ROOT), currentProject.project_name, "DSP_Outputs")

                        sv_file_for_ct = filepath(
                            str(de_folder), "SVPASS_2455_Gene_Alias")
                        cnv_file_for_ct = filepath(
                            str(de_folder), "CNV_PASS_2455_Gene_Alias")
                        dsp_file_for_ct = filepath(
                            str(dsp_folder), "EES_PASS_NS,FS,SGL_2455GeneAlias")

                        # create folder for Clinical Trials
                        ct_folder = Path.joinpath(
                            Path(MEDIA_ROOT), project_name, "ClinicalTrials")
                        os.makedirs(ct_folder, exist_ok=True)

                        launchCT = clinicalLauncher(sv_file_for_ct, cnv_file_for_ct, dsp_file_for_ct, cancer_type,
                                                    currentProject.project_name, str(ct_folder))

                        launchFADautomatedResults=FDA_automated_results()
                        time.sleep(10)
                        launchClilicalResults=process_clilical_files()
                        time.sleep(10)
                        launchvus_results= vus_results()
                        
                       

                        print("Starting Data upload")
                        time.sleep(10)

                        # upload_gdrive = uploadProject(project_path, "Raw")

                        print("Upload Complete")



                        return Response("Pipeline Finished", status=200)

                        
                    return Response(createBiosamples, status=200)
                else:
                    return Response("Not able to create project", status=401)
            else:
                return Response(validate["Reference"].str(" ").validate["Message"], status=validate["Status"])


class PipelineVCF(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        project_name = request.data["project_name"]


class PipelineTN(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        project_name = request.data["project_name"]
        default_project_name = project_name
        cancer_type = request.data["project_cancer_type"]
        rerun = request.data['project_rerun']

        get_projects = Project.objects.filter(bs_default_project=project_name)

        if len(get_projects) != 0:
            if rerun is True:
                default_project_name = project_name
                project_name = project_name + \
                    str("_re_") + str(get_projects.count() + 1)
            else:
                return Response("Project already exists. Please check Rerun to proceed", status=400)
        else:
            # check Basespace Logins
            basespace.usercreds()
            # check project id in basespace
            validate = basespace.ValidateBasespace()
            if validate["Status"] == 200 or validate["Status"] == 201:
                # Check Fastq file format
                formData = request.data

                postError = []
                fileError = False
                for files in request.FILES:
                    validateFasq = basespace.FastQFormatCheck(formData[files])
                    if len(validateFasq) > 0:
                        fileError = True
                        break

                if fileError == True:
                    postError.append(True)
                    return Response(validateFasq, status=500)

                # create project folder in media

                project_path = Path.joinpath(Path(MEDIA_ROOT), project_name)

                biosample_folder_to = Path.joinpath(
                    Path(MEDIA_ROOT), project_name, "Biosamples", "FastQz", "TO")
                biosample_folder_no = Path.joinpath(
                    Path(MEDIA_ROOT), project_name, "Biosamples", "FastQz", "NO")

                annotsv_folder = Path.joinpath(
                    Path(MEDIA_ROOT), project_name, "Biosamples", "VCFs", "DE", "TO")
                os.makedirs(biosample_folder_to)
                os.makedirs(biosample_folder_no)
                os.makedirs(annotsv_folder)

                # Upload Files
                for files in request.FILES:
                    print(files)
                    file_object = formData[files]
                    file_name = file_object.name
                    file_content_type = file_object.content_type
                    file_size = file_object.size

                    if "_n_" in files:
                        print("Normal, ", files)
                        with open(str(biosample_folder_no) + "/" + file_name, 'wb+') as f:
                            for chunk in file_object.chunks():
                                f.write(chunk)
                    elif "_t_" in files:
                        print("Tumor, ", files)
                        with open(str(biosample_folder_to) + "/" + file_name, 'wb+') as f:
                            for chunk in file_object.chunks():
                                f.write(chunk)

                # Create Project
                createProject = basespace.CreateProject(
                    project_name, default_project_name, "DSP-TN")

                currentProject = Project.objects.latest('id')

                if createProject["Type"] == True:
                    # create Biosamples
                    createBiosamples_to = basespace.CreateBioSample(project_id=currentProject.id, sample_type="TO",
                                                                    biosample_path=biosample_folder_to)
                    createBiosamples_no = basespace.CreateBioSample(project_id=currentProject.id, sample_type="NO",
                                                                    biosample_path=biosample_folder_no)

                    if (createBiosamples_to["Type"] == True) & (createBiosamples_no["Type"] == True):
                        print("Biosample Uploaded Successfully")

                        launchDSP_to = basespace.LaunchDSP(
                            project_key=currentProject.id, sample_type="TO")
                        launchDE_to = basespace.LaunchDE(
                            project_key=currentProject.id, sample_type="TO", lab="Novogene")

                        launchDSP_tn = basespace.LaunchDSP(
                            project_key=currentProject.id, sample_type="TN")
                        launchDE_tn = basespace.LaunchDE(project_key=currentProject.id, sample_type="TN",
                                                         lab="Novogene")

                        # Check for status every 5 mins

                        # Do multi processing here
                        p1 = mp.Process(target=CurationDSP, args=(
                            currentProject.id, launchDSP_to,))
                        p2 = mp.Process(target=CurationDE, args=(
                            currentProject.id, launchDE_to,))
                        p3 = mp.Process(target=CurationDSP, args=(
                            currentProject.id, launchDSP_tn,))
                        p4 = mp.Process(target=CurationDE, args=(
                            currentProject.id, launchDE_tn,))
                        # LaunchPipelineDSP = DSP.CurationDSP(project_key=currentProject.id, analysis_id=launchDSP)
                        # launchPipelineDE = DE.CurationDE(project_key=currentProject.id, analysis_id=launchDE)

                        p1.start()
                        p2.start()
                        p3.start()
                        p4.start()

                        p1.join()
                        p2.join()
                        p3.join()
                        p4.join()

                        print("Done")

                        # Start Clinical Trials
                        de_folder = Path.joinpath(
                            Path(MEDIA_ROOT), currentProject.project_name, "DE_Outputs")
                        dsp_folder = Path.joinpath(
                            Path(MEDIA_ROOT), currentProject.project_name, "DSP_Outputs")

                        sv_file_for_ct = filepath(
                            str(de_folder), "SVPASS_2455_Gene_Alias")
                        cnv_file_for_ct = filepath(
                            str(de_folder), "CNV_PASS_2455_Gene_Alias")
                        dsp_file_for_ct = filepath(
                            str(dsp_folder), "EES_PASS_NS,FS,SGL_2455GeneAlias")

                        # create folder for Clinical Trials
                        ct_folder = Path.joinpath(
                            Path(MEDIA_ROOT), project_name, "ClinicalTrials")
                        os.makedirs(ct_folder, exist_ok=True)

                        launchCT = clinicalLauncher(sv_file_for_ct, cnv_file_for_ct, dsp_file_for_ct, cancer_type,
                                                    currentProject.project_name, str(ct_folder))

                    return Response({
                        createBiosamples_to, createBiosamples_no
                    }, status=200)
                else:
                    return Response("Not able to create project", status=401)
            else:
                return Response(validate["Reference"].str(" ").validate["Message"], status=validate["Status"])


@api_view(['GET'])
def get_analysis(request):
    basespace_credentials = usercreds()
    request_url = "https://api.basespace.illumina.com/v1pre3/users/current/appsessions/"

    req = requests.get(request_url, headers=basespace_credentials["headers"])
    req_status = req.status_code

    if req_status == 200 or req_status == 201:
        print(req.json())
        return JsonResponse(req.json())


@api_view(['GET'])
def get_application(request):
    basespace_credentials = usercreds()
    request_url = "https://api.basespace.illumina.com/v1pre3/applications/"

    req = requests.get(request_url, headers=basespace_credentials["headers"])
    req_status = req.status_code
    print(req_status)
    print(os.getcwd())

    if req_status == 200 or req_status == 201:

        return JsonResponse(req.json())


@api_view(['GET'])
def get_user(request):
    basespace_credentials = usercreds()
    request_url = "https://api.basespace.illumina.com/v1pre3/users/current/"

    req = requests.get(request_url, headers=basespace_credentials["headers"])
    req_status = req.status_code

    if req_status == 200 or req_status == 201:

        return JsonResponse(req.json())


@api_view(['GET'])
def get_credits(request):
    basespace_credentials = usercreds()
    request_url = "https://api.basespace.illumina.com/v2/users/current/subscription/"

    req = requests.get(request_url, headers=basespace_credentials["headers"])
    req_status = req.status_code

    if req_status == 200 or req_status == 201:

        return JsonResponse(req.json())


@api_view(['GET'])
def get_files(request):
    currentProject = Project.objects.latest('id')
    projectData = Project.objects.get(id=currentProject.id)
    project_name = projectData.project_name
    print(project_name)
    # project_name = 'INDTSA54969_RE2'
    res = Path.joinpath(Path(MEDIA_ROOT), project_name, 'MSI')
    result = os.listdir(res)

    return Response(result)


@api_view(['GET'])
def get_Annovar_data(request):
    # currentProject = Project.objects.latest('id')
    # projectData = Project.objects.get(id=currentProject.id)
    # project_name = projectData.project_name
    # print(project_name)
    project_name = 'INDTSA54969_RE2'
    res = Path.joinpath(Path(MEDIA_ROOT), project_name,
                        'Annotated_Files', 'Annovar', 'TO')
    result = os.listdir(res)

    return Response(result)


@api_view(['GET'])
def get_DSP_data(request):
    # currentProject = Project.objects.latest('id')
    # projectData = Project.objects.get(id=currentProject.id)
    # project_name = projectData.project_name
    project_name = 'INDTSA54969_RE2'
    res = Path.joinpath(Path(MEDIA_ROOT), project_name,
                        'DSP_Outputs', 'TO', project_name+'_BS_TO_DSP_Outputs')
    print(res)
    result = os.listdir(res)

    return Response(result)


@api_view(['GET'])
def get_Biosamples(request):
    # currentProject = Project.objects.latest('id')
    # projectData = Project.objects.get(id=currentProject.id)
    # project_name = projectData.project_name
    project_name = 'INDTSA54969_RE2'
    res = Path.joinpath(Path(MEDIA_ROOT), project_name, 'Biosamples')
    results = Path.joinpath(res, 'FastQz', 'TO')
    result = os.listdir(res)
    results = os.listdir(results)

    return Response(results)


@api_view(['GET'])
def analysis_latest(request):
    currentProject = Project.objects.latest('id')
    queryset = AnalysisStatus.objects.filter(
        analysis_ref_id=currentProject).values()
    return Response(queryset)


@api_view(['GET'])
def get_DE_data(request):
    # currentProject = Project.objects.latest('id')
    # projectData = Project.objects.get(id=currentProject.id)
    # project_name = projectData.project_name
    project_name = 'INDTSA54969_RE2'
    res = Path.joinpath(Path(MEDIA_ROOT), project_name, 'DE_Outputs')
    print(res)
    result = os.listdir(res)

    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(res):
        listOfFiles += [os.path.join(file) for file in filenames]

    return Response({"files": listOfFiles,
                     "project_name": project_name
                     })


@api_view(['GET'])
def get_clinicalTrails(request):
    # currentProject = Project.objects.latest('id')
    # projectData = Project.objects.get(id=currentProject.id)
    # project_name = projectData.project_name
    project_name = 'INDTSA54969_RE2'
    res = Path.joinpath(Path(MEDIA_ROOT), project_name, 'ClinicalTrials')
    print(res)
    result = os.listdir(res)

    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(res):
        listOfFiles += [os.path.join(file) for file in filenames]

    return Response(listOfFiles)


@api_view(['GET'])
def get_clinicalStudies(request):
    # currentProject = Project.objects.latest('id')
    # projectData = Project.objects.get(id=currentProject.id)
    # project_name = projectData.project_name
    project_name = 'INDTSA54969_RE2'
    res = Path.joinpath(Path(MEDIA_ROOT), project_name,
                        'ClinicalTrials', 'studies')
    print(res)
    result = os.listdir(res)

    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(res):
        listOfFiles += [os.path.join(file) for file in filenames]

    return Response(listOfFiles)


@api_view(['GET'])
def get_latest_project(request):
    currentProject = Project.objects.latest('id')
    projectData = Project.objects.get(id=currentProject.id)
    project_name = projectData.project_name
    return Response(project_name)


@api_view(['GET'])
def get_TMBvalues(request):
    # currentProject = Project.objects.latest('id')
    # projectData = Project.objects.get(id=currentProject.id)
    # project_name = projectData.project_name

    # res = Path.joinpath(Path(MEDIA_ROOT), project_name,
    #                     'DSP_Outputs', 'TO', project_name + "_BS_TO_DSP_Outputs")
    # print(res)
    # result = os.listdir(res)
    # print(result)
    # for files in result:
    #     if files == project_name + "_BS_TO_Src_curation":
    #         TMB_folder = files
    #         print(TMB_folder)
    #         abpath = str(res) + "/" + str(TMB_folder)
    #         print(abpath)
    # for files in os.listdir(abpath):
    #     print(files)
    # if files == project_name + '_BS_TO_TMB_Calculation.xlsx':
    #     files1 = files
    # TMB_files = str(abpath) + "/" + str(files1)

    df = pd.read_excel('/home/aravind/Desktop/data/INDTNA37065_RE_BS_TO_TMB_Calculation.xlsx')

    df.rename({"TMB Calculation": "TMBCalculation",
              "Unnamed: 1": "Values"}, axis='columns', inplace=True)

    df1 = df.dropna()
    df = df1[df1['TMBCalculation'] == 'TMB']
    value = df['Values'].to_numpy().tolist()
    valueTMB = value[0].split()
    finalvalue = int(float(valueTMB[0]))
    print(finalvalue)
    df = df1[df1['TMBCalculation'] == 'STATUS']

    status = df['Values'].to_numpy().tolist()
    statusTMB = status[0]
    finalStatus = str(statusTMB)
    print(finalStatus)

    df = df1[df1['TMBCalculation'] == 'Size of coding Region']
    region = df['Values'].to_numpy().tolist()
    finalRegion = int(float(region[0]))

    print(finalRegion)
    rating = []
    for row in df['Values']:
        if row <= 6 :    rating.append('Low')
        elif( row >=6):   rating.append('Mid')
        elif(row <=20): rating.append('Mid')
    
            
        else:           
            rating.append('High')


    df['status'] = rating

    newstatus=  df['status'].to_numpy().tolist()
    print(newstatus)
    finalNewStatus = newstatus[0]
    print(finalNewStatus)

    return Response({finalvalue, finalNewStatus, finalRegion})


@api_view(['GET'])
def MSI_values(request):
    # currentProject = Project.objects.latest('id')
    # projectData = Project.objects.get(id=currentProject.id)
    # project_name = projectData.project_name
    # MSI_files = project_name.replace("_", ' ')
    # MSI_files = MSI_files.split()
    # MSI_files = MSI_files[0]

    # res = Path.joinpath(Path(MEDIA_ROOT), project_name,
    #                     "MSI")
    # print(res)
    # result = os.listdir(res)
    # print(result)

    # for files in result:
    #     if files == MSI_files + "_MSI":
    #         file1 = files
    #         print(file1)
    #         abpath = str(res) + "/" + str(file1)
    abpath='/home/aravind/Desktop/data/INDTNA37065_MSI'
    df = pd.read_csv(abpath, sep="\t")


    df.rename({"%": "Percentage"}, axis='columns', inplace=True)
    df1 = df['Percentage'].to_numpy().tolist()
    finalvalue = float(df1[0])
    print(finalvalue)
    finalvalue = float(df1[0])

    df['MSI']= finalvalue

    MSI= df['MSI']

    rating = []
    for row in df['MSI']:
        if row <= 20 :    rating.append('Low')
        elif row > 20:   rating.append('High')
    
            
        else:           
            rating.append('-')


    df['status'] = rating
    

   
    STATUS= df['status'].to_numpy().tolist()
    finalstatus = str(STATUS[0])



    print(MSI)
    print(STATUS)
    return Response({ 'MSI':finalvalue , 'STATUS':finalstatus})



@api_view(['GET'])
def get_status_on_data_uploading(request):

    bs_recent_login = Basespace.objects.latest('id')
    pk_of_recent_login = bs_recent_login.id
    current_access_token = bs_recent_login.bs_access_token
    current_bs_email = bs_recent_login.bs_email
    bearer_auth = "Bearer " + str(current_access_token)
    request_headers = {
        "Content-Type": "application/json",
        "User-Agent": "BaseSpaceGOSDK/0.9.3 BaseSpaceCLI/1.2.1",
        "Authorization": bearer_auth
    }
    return_json = {}

    return_json['pk_recent_login'] = pk_of_recent_login
    return_json['bs_email'] = current_bs_email
    return_json['headers'] = request_headers
    return_json['bs_recent_login'] = str(bs_recent_login)

    print(return_json['bs_recent_login'])

    return Response(return_json)


@api_view(['GET'])
def get_whoami(request):

    bs_whoami = os.popen("bs whoami")
    print(bs_whoami)

    return Response(bs_whoami)


@api_view(['GET'])
def get_tests(request):
    req_url = "https://api.basespace.illumina.com/v2/biosamples"
    params = {
        'limit': 25,
        'offset': 0,
        # 'projectId': project_details.bs_project_id,
        'sortBy': 'DateModified',
        'sortDir': 'desc'
    }
    req = re.get(url=req_url, params=params)
    print(req)
    print(req.status_code, req.json())
    return Response(req)


@api_view(['GET'])
def get_VUS(request):

    # path = '/home/aravind/INDTSA54969_RE2_BS_TO_Report/INDTSA54969_RE2_BS_TO_FDA_Report/INDTSA54969_RE2_BS_TO_EES_PASS_NS,FS,SGL_FDA_Report.xlsx'
    # df = excel2json.convert_from_file(path)
    # print(df)
    path_json = '/home/aravind/Desktop/DjangoProjects/data1.json'
    with open(path_json, 'r') as j:
        contents = json.loads(j.read())
    return Response(contents)
    # df= pd.read_excel(path,header=None)
    # df1=df.drop(0)

    # df1.rename(columns = {0:"Drug", 1:'BioMarker',2:'VariantStatusInPatient'}, inplace=True)
    # print(df1)
    # df2=df1.groupby(['Drug', 'BioMarker' ,'VariantStatusInPatient']).sum().reset_index()
    # # for x, y in [(x,y) for x in df1 for y in b]:
    # #     print (x, y)
    # print(df2)
    # writer = pd.ExcelWriter("/home/aravind/INDTSA54969_RE2_BS_TO_Report/INDTSA54969_RE2_BS_TO_FDA_Report/dataframes.xlsx", engine='xlsxwriter')
    # df2.to_excel(writer,sheet_name = 'Source',index=False)
    # writer.save()

    # time.sleep(10)
    # wb = xlrd.open_workbook("/home/aravind/INDTSA54969_RE2_BS_TO_Report/INDTSA54969_RE2_BS_TO_FDA_Report/dataframes.xlsx")
    # for sheet in wb.sheets():
    #     print(sheet.name)

    # sheet = wb.sheet_by_name('Source')
    # for i in range(sheet.nrows):
    #     res=sheet.row_values(i)
    #     print(res)

    # return Response(sheet.row_values(i) )

    # # for row in df.itertuples():
    # for index, row in df.iterrows():
    #     df1=row['Drug'], row['BioMarker'],row['VariantStatusInPatient']
    #     print(df1)


#

@api_view(['GET'])
def results(biosampleId):
    currentProject = Project.objects.latest('id')
    projectData = Project.objects.get(id=currentProject.id)
    project_name = projectData.project_name
    default_project_name = project_name

    bsCreds = usercreds()
    basespaceInstance = Basespace.objects.get(id=bsCreds["pk_recent_login"])
    req_url = "https://api.basespace.illumina.com/v1pre3/projects"
    data = {
        "Name": project_name,
        "Description": "New Project."
    }
    req_headers = bsCreds["headers"]
    req_projects = re.post(url=req_url, json=data, headers=req_headers)
    res_status = req_projects.status_code
    # print(res_status)

    project_details = Project.objects.get(id=currentProject.id)
    sample_type = "TO"
    biosample_name = "%s_BS_%s" % (project_details.project_name, sample_type)
    return_data = {}

    req = "https://api.basespace.illumina.com/v2/biosamples/bulkimport"
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
    req = re.post(url=req, json=data, headers=req_headers)
    res_status = req.status_code

    upload_cmd = "bs upload dataset -p "+str(project_details.bs_project_id) + \
        " --type common.files --concurrency=high --recursive . --biosample-name=" + \
        str(biosample_name)
    data_upload = 'Data Uploading'
    req_url_bioSampleID = "https://api.basespace.illumina.com/v2/biosamples"
    params = {
        'limit': 25,
        'offset': 0,
        'projectId': project_details.bs_project_id,
        'sortBy': 'DateModified',
        'sortDir': 'desc'
    }
    req_bio = re.get(url=req_url_bioSampleID,
                     params=params, headers=req_headers)

    return Response({'req_projects': req_projects, "req": req, "upload_cmd": upload_cmd, "req_bio": req_bio, 'data_upload': data_upload})


@api_view(['GET'])
def get_biosampleId(request):
    currentProject = Project.objects.latest('id')
    projectData = Project.objects.get(id=currentProject.id)
    project_name = projectData.project_name
    default_project_name = project_name
    project_details = Project.objects.get(id=currentProject.id)
    sample_type = "TO"
    biosample_name = "%s_BS_%s" % (project_details.project_name, sample_type)
    upload_cmd = "bs upload dataset -p " + \
        str(project_details.bs_project_id) + \
        " --recursive . --biosample-name="+str(biosample_name)

    # old command
    # bs upload dataset -p str(264362101) --recursive . --biosample-name=str(biosample_name) -vvvv

    uploaddata = os.popen(upload_cmd)
    print(upload_cmd)
    print('Data uploading')
    upload = uploaddata.read()
    time.sleep(50)
    print("Upload Status", upload)

    return Response({'upload': upload, })


@api_view(['GET'])
def clinicaldata(request):
    f = open('/home/aravind/Desktop/DjangoProjects/djangoprojects/kgct-test.json')
    print(f)

    return Response(f)


@api_view(['GET'])
def get_fdaValues(request):

    path_json = '/home/aravind/Desktop/DjangoProjects/Sheet1 (1).json'
    with open(path_json, 'r') as j:
        contents = json.loads(j.read())

    return Response(contents)


@api_view(['GET'])
def get_clilicalReport(request):
    with open('/home/aravind/Desktop/DjangoProjects/clilicaldata.json', 'r') as j:
        files = json.loads(j.read())

    return Response(files)


@api_view(['GET'])
def get_mocular_profile(request):

    fda_path = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder')

    for files in os.listdir(fda_path):
        if files.startswith('fda_output_files.xlsx'):
            fda_files_path = os.path.join(fda_path, files)
    df_fda = pd.read_excel(fda_files_path, sheet_name='Sheet1')
    df_fda.drop(['Unnamed: 0'], axis=1, inplace=True)
    df_fda.reset_index(drop=True, inplace=True)

    Molecular_path = Path.joinpath(
        Path(MEDIA_ROOT), 'Files_folder', 'Molecular_profile')

    for files in os.listdir(Molecular_path):
        if files.endswith('profile.xlsx'):
            molecular_file = files
            molecular_path = str(Molecular_path) + "/" + str(molecular_file)
            break

    df_gene = pd.read_excel(molecular_path, sheet_name='GENE VARIANTS')
    df_gene.loc[(df_gene['Gene'].isin(df_fda['GENE'])) &
                (df_gene['Variant'].isin(df_fda['VARIANT']))]

    df_values = df_gene.loc[(df_gene['Gene'].isin(df_fda['GENE'])) & (
        df_gene['Variant'].isin(df_fda['VARIANT']))]
    df_values.reset_index(drop=True, inplace=True)
    df_values['Profile'] = df_values['Gene'].str.cat(
        df_values['Variant'], sep="(")+")"
    df_values.to_excel('mocular_profile.xlsx')

    df_values.drop([
        'Associated with drug Resistance'

    ], axis=1, inplace=True)

    output_molecular_file = os.path.join(
        Molecular_path, 'molecular_file_results.json')

    with open(output_molecular_file, 'w') as f:
        json.dump(df_values.to_dict(orient='records'), f)

    time.sleep(10)
    with open(output_molecular_file, 'r') as j:
        files = json.loads(j.read())
    return Response(files)


@api_view(["GET"])
def fad_sheet_filters(request):

    res = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder')
    result = os.listdir(res)

    fda_sheet = Path.joinpath(
        Path(MEDIA_ROOT), 'Files_folder', "fda_output_files")
    os.makedirs(fda_sheet, exist_ok=True)

    input_file_path_AF_VAF_inclusion = Path.joinpath(
        Path(MEDIA_ROOT), 'Files_folder', 'CRCM')
    AF_files = os.listdir(input_file_path_AF_VAF_inclusion)

    for files in result:
        if files.startswith("FDA_Master"):
            fda_file = files
            fda_path = str(res) + "/" + str(fda_file)
            break
    for files in result:
        if files.endswith("_N_FOR_LIST_Report.xlsx"):
            CRCM_files = files
            crcm_path = str(res) + "/" + str(CRCM_files)
            break

    for files in AF_files:
        if files.endswith('_EES_PASS.xlsx'):
            af_vaf = files
            af_path = str(input_file_path_AF_VAF_inclusion) + '/' + str(af_vaf)
            break
    df_fda = pd.read_excel(fda_path, sheet_name="FDA+FDA CDx_SNVGT")
    df_patient_data = pd.read_excel(crcm_path, sheet_name='Source')
    df_af_data = pd.read_excel(af_path, sheet_name='Sheet1')

    df_new_file = df_patient_data.loc[(df_patient_data['Chr'].isin(df_af_data['Chr'])) & (
        df_patient_data['Start'].isin(df_af_data['Start'])) & (df_patient_data['End'].isin(df_af_data['End']))]

    df_new_data = pd.merge(df_new_file, df_af_data, how='inner', left_on=[
                           'Chr', 'Start', 'End'], right_on=['Chr', 'Start', 'End'])

    df_new_extract_file = df_new_data[['Chr', 'Start', 'Gene.refGene_x', 'AAChange', 'AAChange_CDS',
                                       'cosmic_id', 'ExonicFunc.refGene', 'fathmm-MKL_coding_score_x', 'Report_Decision', 'AF_VAF_y']]

    df_new_extract_file.rename(columns={'Gene.refGene_x': 'Gene.refGene',
                               'fathmm-MKL_coding_score_x': 'fathmm-MKL_coding_score', 'AF_VAF_y': 'AF_VAF'}, inplace=True)

    df_fda['Status'] = np.where((df_fda["GENE"].isin(df_new_extract_file["Gene.refGene"]) & (
        df_fda["PSEUDOVARIANT"].isin(df_new_extract_file["AAChange"]))), 'Positive', 'Negative')
    df_filtered = df_fda
    result = df_filtered.loc[(df_filtered['GENE'].isin(df_new_extract_file['Gene.refGene'])) & (
        df_filtered['PSEUDOVARIANT'].isin(df_new_extract_file['AAChange']))]
    df_cd = pd.merge(result, df_new_extract_file, how='inner',
                     left_on='VARIANT', right_on='AAChange')
    df_cd.drop(['EXON', 'PSEUDOVARIANT',
                'PSEUDOVARIANT CDS', 'TYPE OF VARIANT', 'COMBINATION MARKER', 'VARIANT ORIGIN', 'ZYGOSITY',
                'EVIDENCE STATEMENT FROM LABEL', 'SIGNIFICANCE', 'LEVELS OF EVIDENCE',
                'TYPE OF EVIDENCE', 'REMARKS', 'REFERENCES', 'PMID', 'DOID',
                'Chromosome', 'Start_x', 'Stop', 'Size (kb)', 'Cytoband',
                'ARCHIVAL NUMBER', 'SOURCE', 'LABEL DATE',
                'Chr', 'Start_y', 'Gene.refGene', 'AAChange', 'AAChange_CDS',
                'cosmic_id', 'ExonicFunc.refGene', 'fathmm-MKL_coding_score',
                'Report_Decision'], axis=1, inplace=True)

    output_file_folder = os.path.join(str(fda_sheet), str(fda_sheet)+'.xlsx')

    df_cd.rename(columns={'EVIDENCE STATEMENT 1': 'EVIDENCE_STATEMENT_1', 'VARIANT CDS': 'VARIANT_CDS',
                 'EVIDENCE STATEMENT 2': 'EVIDENCE_STATEMENT_2', 'CANCER TYPE': 'CANCER_TYPE'}, inplace=True)
    df_files = df_cd['CANCER_TYPE'].values.tolist()
    for i in df_files:
        result = " ".join(i.split()[2:])

        df_cd['CANCER_TYPES'] = result

    df_cd.drop(['CANCER_TYPE'], axis=1, inplace=True)
    df_cd.to_excel(output_file_folder)

    time.sleep(5)
    output_json_file = os.path.join(res, 'fda_reports.json')

    output = dict()

    thisisjson = df_cd.to_json(orient='records')

    thisisjson_dict = json.loads(thisisjson)
    output = thisisjson_dict

    with open(output_json_file, 'w') as json_file:
        json.dump(output, json_file)

    time.sleep(10)
    with open(output_json_file, 'r') as j:
        files = json.loads(j.read())
    return Response(files)






  

@api_view(['GET', 'POST'])
def Genes_Variants_Cancertypes(request):
    Genes = request.POST['Genes']
    variants = request.POST['variants']
    cancer_types = request.POST['cancer_types']

    person = FDAReports(Genes=Genes, variants=variants,
                        cancer_types=cancer_types)
    person.save()
    return Response(person)


@api_view(['GET'])
def de_results(request):
    path = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder', 'De_results')

    for files in os.listdir(path):
        if files.endswith('_TO_CNV_Report.xlsx'):
            cnv_file = files
            cnv_path = str(path) + "/" + str(cnv_file)
            break

    de_path = pd.read_excel(cnv_path, sheet_name='Report')
    de_file = de_path.fillna('NaN')
    de_file.rename(columns={'Variant status in patient': 'Variant_status_in_patient',
                            'Cancer Type': 'Cancer_Type', 'Evidence Statement': 'EVIDENCE_STATEMENT', 'LEVELS OF EVIDENCE': 'LEVELS_OF_EVIDENCE'}, inplace=True)

    output_cnv_file = os.path.join(path, 'CNV.json')

    with open(output_cnv_file, 'w') as f:
        json.dump(de_file.to_dict(orient='records'), f)

    with open(output_cnv_file, 'r') as j:
        cnv_files = json.loads(j.read())
    return Response(cnv_files)


@api_view(['GET'])
def DSP_results(request):
    path = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder', 'dsp_results')

    for files in os.listdir(path):
        if files.endswith('_TO_EES_PASS_Database_MATCH.xlsx'):
            dsp_file = files
            dsp_path = str(path) + "/" + str(dsp_file)
            break

    dsp_path = pd.read_excel(dsp_path, sheet_name='Sheet1')
    df_variant_filter = dsp_path.loc[dsp_path['PSEUDOVARIANT'] != 'WT']
    df_fda_filter = df_variant_filter.loc[df_variant_filter['SOURCE'] != 'FDA']

    df_dsp = df_fda_filter[['Gene.refGene', 'AAChange', 'AAChange_Exon', 'CLNSIG', 'AF_VAF', 'VARIANT ', 'PSEUDOVARIANT',
                            'THERAPY', 'CANCER TYPE', 'EVIDENCE STATEMENT', 'SIGNIFICANCE', 'LEVELS OF EVIDENCE', 'REFERENCES']]

    df_dsp.rename(columns={'Gene.refGene': 'Gene', 'VARIANT ': 'Variant',
                           'CANCER TYPE': 'Cancer_Type', 'EVIDENCE STATEMENT': 'EVIDENCE_STATEMENT', 'LEVELS OF EVIDENCE': 'LEVELS_OF_EVIDENCE'}, inplace=True)
    df_dsp_file = df_dsp.fillna('NaN')

    output_dsp_file = os.path.join(path, 'DSP.json')

    with open(output_dsp_file, 'w') as f:
        json.dump(df_dsp_file.to_dict(orient='records'), f)

    with open(output_dsp_file, 'r') as j:
        dsp_files = json.loads(j.read())
    return Response(dsp_files)


@api_view(["GET"])
def patient_ids(request):

    pat_id = 'INDTS99585'
    df = re.get(
        f"http://pp.kyvorgenomics.com/patient_data.php?patient_id={pat_id}")

    x = df.json()
    df = pd.read_json(json.dumps(x))

    df_id = pd.DataFrame(df['patient_specimen_id'].tolist())
    df_split = df_id[0].to_numpy().tolist()
    Types = [line.split(";") for line in df_split]
    prefixes = ('a:', 'i:', '}')
    newlist = [x for x in Types[0] if not x.startswith(prefixes)]

    new_id = [line.split(":") for line in newlist]

    final_id = [line[-1] for line in new_id]

    final_specimen_id = [i.replace('"', '') for i in final_id]

    new_values = [n for n in final_specimen_id if '/' in n]

    specimen_values = [n for n in final_specimen_id if '/' not in n]
    print(specimen_values)

    count_id = len(final_specimen_id)

    result_list = []
    first_value = []
    for i in new_values:
        if count_id > 1:
            try:

                first_value.append(i.split('/')[0])
                last_value = i.split('/')[1]
                string_val = f"({','.join(first_value)})"

                if first_value and last_value:

                    brackets_value = f" ID - {string_val}/{last_value}"

                    result_list.append(brackets_value)

                elif last_value:
                    result_list.append(last_value)

            except Exception as e:
                print("ERROR : "+str(e))

        elif count_id <= 1:

            for i in final_specimen_id:
                try:
                    first_value = i.split('/')[0]
                    last_value = i.split('/')[1]
                    if first_value and last_value:

                        brackets_value = f" ID - {first_value}/{last_value}"
                        result_list.append(brackets_value)

                    elif last_value:
                        result_list.append(last_value)

                except:
                    last_value = i

    final_result_value = ''.join(map(str, result_list[-1:]))
    df['patient_specimen_type']

    df_type = pd.DataFrame(df['patient_specimen_type'].tolist())
    df_split_type = df_type[0].to_numpy().tolist()
    specimen_types = [line.split(";") for line in df_split_type]
    type_prefixes = ('a:', 'i:', ';', '}')
    newlist_type = [x for x in specimen_types[0]
                    if not x.startswith(type_prefixes)]
    newlist_type

    new_type_id = [line.split(":") for line in newlist_type]

    final_type_id = [line[-1] for line in new_type_id]

    final_specimen_type = [i.replace('"', '') for i in final_type_id]
    print(final_specimen_type)

    count_type_id = len(final_specimen_type)

    result_type_list = []
    first_type_value = []
    for i in final_specimen_type:
        if count_id > 1:

            first_type_value.append(i)

            string_val = ','.join(first_type_value)

            string_results = ('Type' + ' ' + '-'+' ' + str(string_val))

            result_type_list.append(string_results)

        elif count_id <= 1:

            result_type_list.append(i)

            string_val = ','.join(result_type_list)

            string_results = ('Type' + ' ' + '-'+' ' + str(string_val))

            result_type_list.append(string_results)
            break

    final_result_type = ''.join(map(str, result_type_list[-1:]))

    df_site = pd.DataFrame(df['patient_specimen_site'].tolist())
    df_split_site = df_site[0].to_numpy().tolist()
    specimen_site = [line.split(";") for line in df_split_site]
    site_prefixes = ('a:', 'i:', ';', '}')
    newlist_site = [x for x in specimen_site[0]
                    if not x.startswith(site_prefixes)]
    newlist_site

    new_site_id = [line.split(":") for line in newlist_site]

    new_site_id
    final_site_id = [line[-1] for line in new_site_id]
    final_site_id

    final_specimen_site = [i.replace('"', '') for i in final_site_id]

    res_site = []
    for i in final_specimen_site:
        if i.strip() != '':
            res_site.append(i)

    res_site

    count_type_id = len(res_site)
    print(count_type_id)

    result_site_list = []
    first_site_value = []
    for i in res_site:

        if i:

            first_site_value.append(i)

            string_site = ','.join(first_site_value)

            string_site_results = ('Site' + ' ' + '-'+' ' + str(string_site))

            result_site_list.append(string_site_results)

        else:

            print("Site- '' ")
            break

    final_result_site = ''.join(map(str, result_site_list))

    df['Final_results_colum'] = str(final_result_value) + " " + "|" + " "+str(
        final_result_type) + " " + "|" + " "+str(final_result_site)

    df = df[['key', 'patient_id', 'patient_name', 'patient_gender', 'patient_age', 'patient_marital_status',
             'patient_cancer_type', 'physician_id', 'physician_name', 'Final_results_colum']]

    def f(row):
        if row['patient_gender'] == 'Male':
            val = 'Mr'
        elif row['patient_gender'] == 'Female':
            val = 'Mrs'
        else:
            val = ''
        return val

    df['Head'] = df.apply(f, axis=1)
    df

    df_age = df['patient_age'].values.astype(str)

    df['Patient_Information'] = df['patient_id'] + " " + " | " + df['patient_gender'] + \
        " " + " | " + df_age + " " + 'Yrs' + " " + \
        " | " + df['Head']+'.' + df['patient_name']

    df['Physician_information'] = df['physician_id'] + \
        " " + " | "+" " + "Dr." + df['physician_name']
    df = df[['Patient_Information', 'Physician_information',
             'patient_cancer_type', 'Final_results_colum']]

    patient_id_output_folder = Path.joinpath(
        Path(MEDIA_ROOT), 'Patient_id', pat_id)
    os.makedirs(patient_id_output_folder, exist_ok=True)

    output_patient_id_file = os.path.join(
        patient_id_output_folder, 'patientId.json')

    with open(output_patient_id_file, 'w') as f:
        json.dump(df.to_dict(orient='records'), f)

    with open(output_patient_id_file, 'r') as j:
        patient_id_files = json.loads(j.read())
    return Response(patient_id_files)






@api_view(["GET"])
def process_clilical_files(request):
    res = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder',
                        'clinical_trial_file')
    result = os.listdir(res)
    #================= fad_file_path===========#
    fda_path = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder')

    for files in os.listdir(fda_path):
        if files.startswith('fda_output_files.xlsx'):
            fda_files_path = os.path.join(fda_path, files)
    df_fda = pd.read_excel(fda_files_path, sheet_name='Sheet1')
    df_fda.drop(['Unnamed: 0'], axis=1, inplace=True)
    df_fda.reset_index(drop=True, inplace=True)

    for files in result:
        if files.endswith("kgct.xlsx"):
            kgct_files = files
            kgct_path = str(res) + "/" + str(kgct_files)
            break

    df = pd.read_excel(kgct_path)

    df.drop(['Unnamed: 0', 'gene_found_in',  'gene_aliases_found', 'variants_found_in', 'role_in_cancer', 'protein_effect', 'impact',
            'associated_with_drug_resistance', 'intervention_other_name', 'intervention_description', 'arm_title',
             'arm_description', 'arm_group_intervention', 'eligibility_criteria',
             'inclusion_criteria', 'exclusion_criteria', 'primary_om_title',
             'primary_om_description', 'secondary_om_title',
             'secondary_om_description', 'other_om_title', 'other_om_description',
             'keywords', 'mesh_terms', 'pmid',


             'brief_title',
             'brief_summary', 'detailed_description'], axis=1, inplace=True)

    df_study_type_filter = df[(df['study_type'] == 'Interventional') | (
        df['study_type'] == 'Expanded Access')]

    df_study_purpose_filter = df_study_type_filter[df_study_type_filter['study_purpose'] == 'Treatment']

    df_level_filter = df_study_purpose_filter[df_study_type_filter['level'] == '1A']

    df_recruitment_col_filter = df_level_filter[(df_level_filter['recruitment_status'] == 'Not yet recruiting') | (df_level_filter['recruitment_status'] == 'Recruiting') | (
        df_level_filter['recruitment_status'] == 'Enrolling by invitation') | (df_level_filter['recruitment_status'] == 'Active, not recruiting')]
    Genes = ['EGFR']
    variants = ['l858r']
    cancer_types = 'Lung Cancer' .lower()
    df_gene_find = df_recruitment_col_filter[df_recruitment_col_filter['gene_name'].isin(
        Genes)]

    df_variant_filter = df_gene_find[df_gene_find['variant_found'].isin(
        variants)]

    df_variant_filter = df_variant_filter.reset_index()

    final_draft = df_variant_filter[df_variant_filter.cancer_type.str.contains(
        cancer_types, flags=regex.IGNORECASE, regex=True, na=False)]
    final_draft.reset_index(inplace=True)
    final_draft.drop(['level_0', 'index'], axis=1, inplace=True)

    final_draft['BioMarker'] = final_draft['gene_name'].str.cat(
        final_draft['variant_found'], sep=" ")

    final_draft['Reference'] = final_draft[['nct_id', 'phase',
                                            'recruitment_status']].apply(lambda x: ' | '.join(x), axis=1)

    final_draft.drop([
        'gene_id',  'gene_name', 'study_type', 'study_purpose',
        'study_model', 'recruitment_status', 'phase', 'level',
        'cancer_type',  'drug_found', 'drug_not_found',
        'drug_target', 'drug_target_pathway',
        'variant_match_type', 'curation_status', 'curator',
        'curator_comments', 'last_update_post_date', 'id',

    ], axis=1, inplace=True)

    final_draft['BioMarker'] = final_draft['BioMarker'].str.upper()
    final_draft['variant_found'] = final_draft['variant_found'].str.upper()

    df_new_data = pd.merge(final_draft, df_fda, how='inner',
                           left_on='variant_found', right_on='VARIANT')

    df_final = df_new_data.drop_duplicates(subset='nct_id', keep='last')
    df_final.reset_index(drop=True, inplace=True)
    outputfile_kgct = os.path.join(str(res), 'kgct_results.xlsx')
    df_final.to_excel(outputfile_kgct)

    time.sleep(10)
    excel_data_df = pd.read_excel(outputfile_kgct)

    excel_data_df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

    excel_data_df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

    output = dict()

    thisisjson = excel_data_df.to_json(orient='records')

    thisisjson_dict = json.loads(thisisjson)
    output = thisisjson_dict

    output_clinical_trail_file = os.path.join(res, 'clinicalTrail.json')

    with open(output_clinical_trail_file, 'w') as json_file:
        json.dump(output, json_file)
        
    with open(output_clinical_trail_file) as f:
        posts_json = json.load(f)
        print(posts_json)

    for post in posts_json:
        post = Clinical_DATA(id=post['id'], nct_id=post['nct_id'], official_title=post['official_title'], intervention=post['intervention'], variant_found=post['variant_found'],
                          url=post['url'], BioMarker=post['BioMarker'], Reference=post['Reference'], GENE=post['GENE'], VARIANT=post['VARIANT'],   VARIANT_CDS=post['VARIANT_CDS'], THERAPY=post['THERAPY'], EVIDENCE_STATEMENT_1=post['EVIDENCE_STATEMENT_1'], EVIDENCE_STATEMENT_2=post['EVIDENCE_STATEMENT_2'] ,Status=post['Status'], AF_VAF=post['AF_VAF'],CANCER_TYPES=post['CANCER_TYPES'])
        post.save()

    return Response('Data uploaded to database')


@api_view(['GET'])
def vus_results(result):
    fda_path = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder')

    SNV_PATH = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder', 'SV&CNV')

    Molecular_path = Path.joinpath(
        Path(MEDIA_ROOT), 'Files_folder', 'Molecular_profile')
    for files in os.listdir(SNV_PATH):
        if files.endswith('_N_FOR_LIST_Report.xlsx'):
            snv_file = files
            snv_path = str(SNV_PATH) + "/" + str(snv_file)
            break

    for files in os.listdir(SNV_PATH):
        if files.endswith('_B_FOR_LIST_Report.xlsx'):
            indel_file = files
            indel_path = str(SNV_PATH) + "/" + str(indel_file)
            break
    for files in os.listdir(Molecular_path):
        if files.endswith('profile.xlsx'):
            molecular_file = files
            molecular_path = str(Molecular_path) + "/" + str(molecular_file)
            break

    for files in os.listdir(fda_path):
        if files.startswith('fda_output_files.xlsx'):
            fda_files_path = os.path.join(fda_path, files)
    df_fda = pd.read_excel(fda_files_path, sheet_name='Sheet1')
    df_fda.drop(['Unnamed: 0'], axis=1, inplace=True)
    df_fda.reset_index(drop=True, inplace=True)

    df_snv = pd.read_excel(snv_path, sheet_name='Cols Sorted')
    df_snv.rename(columns={'Gene.refGene': 'GENE',
                  'AAChange': 'AMINO_ACID_CHANGE'}, inplace=True)

    df_indel = pd.read_excel(indel_path, sheet_name='Cols Sorted')
    df_indel.rename(columns={'Gene.refGene': 'GENE',
                    'AAChange': 'AMINO_ACID_CHANGE'}, inplace=True)

    df_molecular_profile = pd.read_excel(
        molecular_path, sheet_name='GENE VARIANTS')

    # _____________________ SNVFILE________________________________________
    result_df = df_molecular_profile.loc[(df_molecular_profile['Gene'].isin(
        df_snv['GENE'])) | (df_molecular_profile['Variant'].isin(df_snv['AMINO_ACID_CHANGE']))]

    result_df['status'] = np.where((result_df["Gene"].isin(df_fda["GENE"]) | (
        result_df["Variant"].isin(df_fda["VARIANT"]))), 'True', 'False')

    df_True_SNV = result_df.loc[result_df['status'] == 'True']

    df_False_SNV = result_df.loc[result_df['status'] == 'False']

    df_snv['status'] = np.where((df_snv["GENE"].isin(df_True_SNV["Gene"]) | (
        df_snv['AMINO_ACID_CHANGE'].isin(df_True_SNV["Variant"]))), 'True', 'False')

    df_true_SNV = df_snv.loc[df_snv['status'] == 'True']

    df_false_SNV = df_snv.loc[df_snv['status'] == 'False']

    # _____________________________SNVFILE____________COMpleted________________

    # _________________________iNDEL FILE______________________________

    result_df_indel = df_molecular_profile.loc[(df_molecular_profile['Gene'].isin(
        df_indel['GENE'])) | (df_molecular_profile['Variant'].isin(df_indel['AMINO_ACID_CHANGE']))]

    result_df_indel['status'] = np.where((result_df_indel["Gene"].isin(df_fda["GENE"]) | (
        result_df_indel["Variant"].isin(df_fda["VARIANT"]))), 'True', 'False')

    df_True_indel = result_df_indel.loc[result_df_indel['status'] == 'True']

    df_False_indel = result_df_indel.loc[result_df_indel['status'] == 'False']

    df_indel['status'] = np.where((df_indel["GENE"].isin(df_True_indel["Gene"]) | (
        df_indel['AMINO_ACID_CHANGE'].isin(df_True_indel["Variant"]))), 'True', 'False')

    df_true_indel = df_indel.loc[df_indel['status'] == 'True']

    df_false_indel = df_indel.loc[df_indel['status'] == 'False']

    # ____________________indelfile_______completed_____________

    output_snv_file = os.path.join(Molecular_path, 'SNV.xlsx')
    output_indel_file = os.path.join(Molecular_path, 'INDEL.xlsx')


    df_false_SNV.to_excel(output_snv_file)
    df_false_indel.to_excel(output_indel_file)


    for files in os.listdir(Molecular_path):
        if files.endswith('SNV.xlsx'):
            snv_database_files = files
            snv_database_path = str(Molecular_path) + "/" + str(snv_database_files)
            break

    for files in os.listdir(Molecular_path):
        if files.endswith('INDEL.xlsx'):
            indel_database_files = files
            indel_database_path = str(Molecular_path) + "/" + str(indel_database_files)
            break

    df_snv_path= pd.read_excel(snv_database_path)
    df_indel_path= pd.read_excel(indel_database_path)

    df_snv_path.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
    df_indel_path.rename(columns={'Unnamed: 0': 'id'}, inplace=True)


    output = dict()

    output2 = dict()
    thisisjson = df_snv_path.to_json(orient='records')
    thisisjson2 = df_indel_path.to_json(orient='records')




    thisisjson_dict = json.loads(thisisjson)
    thisisjson_dict2 = json.loads(thisisjson2)
    output = thisisjson_dict
    output2=thisisjson_dict2

    output_snv_database_file = os.path.join(Molecular_path, 'SNV_database.json')
    output_indel_database_file = os.path.join(Molecular_path, 'Indel_database.json')


    with open(output_snv_database_file, 'w') as json_file:
            json.dump(output, json_file)


    with open(output_snv_database_file) as f:
        posts_json = json.load(f)
        print(posts_json)

    for post in posts_json:
        post = SNV_datas(id=post['id'], GENE=post['GENE'], AMINO_ACID_CHANGE=post['AMINO_ACID_CHANGE'], CDS=post['CDS'])
        post.save()


    with open(output_indel_database_file, 'w') as json_file:
            json.dump(output2, json_file)


    with open(output_indel_database_file) as f:
        posts_json = json.load(f)
        print(posts_json)

    for post in posts_json:
        post = INDEL_datas(id=post['id'], GENE=post['GENE'], AMINO_ACID_CHANGE=post['AMINO_ACID_CHANGE'], CDS=post['CDS'])
        post.save()



    return Response('Data uploaded to database')

@api_view(['GET'])
def FDA_automated_results(request):

    res = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder')
    result = os.listdir(res)

    fda_sheet = Path.joinpath(
        Path(MEDIA_ROOT), 'Files_folder', "fda_output_files")
    os.makedirs(fda_sheet, exist_ok=True)

    input_file_path_AF_VAF_inclusion = Path.joinpath(
        Path(MEDIA_ROOT), 'Files_folder', 'CRCM')
    AF_files = os.listdir(input_file_path_AF_VAF_inclusion)

    for files in result:
        if files.startswith("FDA_Master"):
            fda_file = files
            fda_path = str(res) + "/" + str(fda_file)
            break
    for files in result:
        if files.endswith("_N_FOR_LIST_Report.xlsx"):
            CRCM_files = files
            crcm_path = str(res) + "/" + str(CRCM_files)
            break

    for files in AF_files:
        if files.endswith('_EES_PASS.xlsx'):
            af_vaf = files
            af_path = str(input_file_path_AF_VAF_inclusion) + '/' + str(af_vaf)
            break
    df_fda = pd.read_excel(fda_path, sheet_name="FDA+FDA CDx_SNVGT")
    df_patient_data = pd.read_excel(crcm_path, sheet_name='Source')
    df_af_data = pd.read_excel(af_path, sheet_name='Sheet1')

    df_new_file = df_patient_data.loc[(df_patient_data['Chr'].isin(df_af_data['Chr'])) & (
        df_patient_data['Start'].isin(df_af_data['Start'])) & (df_patient_data['End'].isin(df_af_data['End']))]

    df_new_data = pd.merge(df_new_file, df_af_data, how='inner', left_on=[
                           'Chr', 'Start', 'End'], right_on=['Chr', 'Start', 'End'])

    df_new_extract_file = df_new_data[['Chr', 'Start', 'Gene.refGene_x', 'AAChange', 'AAChange_CDS',
                                       'cosmic_id', 'ExonicFunc.refGene', 'fathmm-MKL_coding_score_x', 'Report_Decision', 'AF_VAF_y']]

    df_new_extract_file.rename(columns={'Gene.refGene_x': 'Gene.refGene',
                               'fathmm-MKL_coding_score_x': 'fathmm-MKL_coding_score', 'AF_VAF_y': 'AF_VAF'}, inplace=True)

    df_fda['Status'] = np.where((df_fda["GENE"].isin(df_new_extract_file["Gene.refGene"]) & (
        df_fda["PSEUDOVARIANT"].isin(df_new_extract_file["AAChange"]))), 'Positive', 'Negative')
    df_filtered = df_fda
    result = df_filtered.loc[(df_filtered['GENE'].isin(df_new_extract_file['Gene.refGene'])) & (
        df_filtered['PSEUDOVARIANT'].isin(df_new_extract_file['AAChange']))]
    df_cd = pd.merge(result, df_new_extract_file, how='inner',
                     left_on='VARIANT', right_on='AAChange')
    df_cd.drop(['EXON', 'PSEUDOVARIANT',
                'PSEUDOVARIANT CDS', 'TYPE OF VARIANT', 'COMBINATION MARKER', 'VARIANT ORIGIN', 'ZYGOSITY',
                'EVIDENCE STATEMENT FROM LABEL', 'SIGNIFICANCE', 'LEVELS OF EVIDENCE',
                'TYPE OF EVIDENCE', 'REMARKS', 'REFERENCES', 'PMID', 'DOID',
                'Chromosome', 'Start_x', 'Stop', 'Size (kb)', 'Cytoband',
                'ARCHIVAL NUMBER', 'SOURCE', 'LABEL DATE',
                'Chr', 'Start_y', 'Gene.refGene', 'AAChange', 'AAChange_CDS',
                'cosmic_id', 'ExonicFunc.refGene', 'fathmm-MKL_coding_score',
                'Report_Decision'], axis=1, inplace=True)

    output_file_folder = os.path.join(str(fda_sheet), str(fda_sheet)+'.xlsx')

    df_cd.rename(columns={'EVIDENCE STATEMENT 1': 'EVIDENCE_STATEMENT_1', 'VARIANT CDS': 'VARIANT_CDS',
                 'EVIDENCE STATEMENT 2': 'EVIDENCE_STATEMENT_2', 'CANCER TYPE': 'CANCER_TYPE'}, inplace=True)
    df_files = df_cd['CANCER_TYPE'].values.tolist()
    for i in df_files:
        result = " ".join(i.split()[2:])

        df_cd['CANCER_TYPES'] = result

    df_cd.drop(['CANCER_TYPE'], axis=1, inplace=True)
    df_cd.to_excel(output_file_folder)

    time.sleep(5)
    for files in os.listdir(res):
        if files.endswith('_output_files.xlsx'):
            fda_json = files
            fda_json_path = str(res) + "/" + str(fda_json)
            break

    output = dict()

    df_fda = pd.read_excel(fda_json_path)
    df_fda.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

    thisisjson = df_fda.to_json(orient='records')

    thisisjson_dict = json.loads(thisisjson)
    output = thisisjson_dict

    output_fda_reports_file = os.path.join(res, 'databaseFDA.json')

    with open(output_fda_reports_file, 'w') as json_file:
        json.dump(output, json_file)

    with open(output_fda_reports_file) as f:
        posts_json = json.load(f)
        print(posts_json)

    for post in posts_json:
        post = FDA_Sheets(id=post['id'], GENE=post['GENE'], BIOMARKER=post['BIOMARKER'], VARIANT_CDS=post['VARIANT_CDS'], THERAPY=post['THERAPY'],
                          EVIDENCE_STATEMENT_1=post['EVIDENCE_STATEMENT_1'], EVIDENCE_STATEMENT_2=post['EVIDENCE_STATEMENT_2'], Status=post['Status'], AF_VAF=post['AF_VAF'], CANCER_TYPES=post['CANCER_TYPES'])
        post.save()

    return Response('Data uploaded to database')


class FDA_DATABASE(viewsets.ModelViewSet):
    queryset = FDA_Sheets.objects.all().order_by('id')
    serializer_class = FDA_Serializer



class ClinicalDatabases(viewsets.ModelViewSet):
    queryset = Clinical_DATA.objects.all().order_by('id')
    serializer_class = ClinicalDataSerializer


class SNVdatabase(viewsets.ModelViewSet):
    queryset=SNV_datas.objects.all().order_by('id')
    serializer_class= SNVDataSerializer

class INDELdatabase(viewsets.ModelViewSet):
    queryset= INDEL_datas.objects.all().order_by('id')
    serializer_class=INDELDataSerializer