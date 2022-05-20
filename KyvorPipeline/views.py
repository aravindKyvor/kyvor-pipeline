import os
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
    currentProject = Project.objects.latest('id')
    projectData = Project.objects.get(id=currentProject.id)
    project_name = projectData.project_name

    res = Path.joinpath(Path(MEDIA_ROOT), project_name,
                        'DSP_Outputs', 'TO', project_name + "_BS_TO_DSP_Outputs")
    print(res)
    result = os.listdir(res)
    print(result)
    for files in result:
        if files == project_name + "_BS_TO_Src_curation":
            TMB_folder = files
            print(TMB_folder)
            abpath = str(res) + "/" + str(TMB_folder)
            print(abpath)
    for files in os.listdir(abpath):
        print(files)
    if files == project_name + '_BS_TO_TMB_Calculation.xlsx':
        files1 = files
    TMB_files = str(abpath) + "/" + str(files1)

    df = pd.read_excel(TMB_files)

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

    return Response({finalvalue, finalStatus, finalRegion})


@api_view(['GET'])
def MSI_values(request):
    currentProject = Project.objects.latest('id')
    projectData = Project.objects.get(id=currentProject.id)
    project_name = projectData.project_name
    MSI_files = project_name.replace("_", ' ')
    MSI_files = MSI_files.split()
    MSI_files = MSI_files[0]

    res = Path.joinpath(Path(MEDIA_ROOT), project_name,
                        "MSI")
    print(res)
    result = os.listdir(res)
    print(result)

    for files in result:
        if files == MSI_files + "_MSI":
            file1 = files
            print(file1)
            abpath = str(res) + "/" + str(file1)
    df = pd.read_csv(abpath, sep="\t")
# import pandas as pd
# path = '/content/INDTSA54969_MSI'
# df = pd.read_csv(path,sep = "\t")

    df.rename({"%": "Percentage"}, axis='columns', inplace=True)
    df1 = df['Percentage'].to_numpy().tolist()
    finalvalue = float(df1[0])
    print(finalvalue)
    return Response(finalvalue)


# @api_view(['GET'])
# def get_status_on_data_uploading(request):
#     bs_recent_login = Basespace.objects.latest('id')
#     pk_of_recent_login = bs_recent_login.id
#     current_access_token = bs_recent_login.bs_access_token
#     current_bs_email = bs_recent_login.bs_email
#     bearer_auth = "Bearer " + str(current_access_token)
#     request_headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "BaseSpaceGOSDK/0.9.3 BaseSpaceCLI/1.2.1",
#         "Authorization": bearer_auth
#     }


#     print(request_headers)
#     return HttpResponse({'bs_recent_login':bs_recent_login, 'pk_of_recent_login':pk_of_recent_login,'current_access_token':current_access_token,'current_bs_email':current_bs_email,'bearer_auth':bearer_auth,'request_headers':request_headers})


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
    f= open('/home/aravind/Desktop/DjangoProjects/djangoprojects/kgct-test.json')
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
    with open('/home/aravind/Desktop/cnvkits/moculardata1.json','r') as j:
        files = json.loads(j.read())
    return Response(files)






# @api_view(['GET'])
# def get_latest_patient_portal(request):
   
#     queryset= PatientPortal.objects.all()
#     print(queryset)
#     return Response(queryset)
   
@api_view(["GET"])
def fad_sheet_filters(request): 
   
    
    res = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder')
    result = os.listdir(res)
    
    fda_sheet = Path.joinpath(
        Path(MEDIA_ROOT), 'Files_folder', "fda_output_files" )
    os.makedirs(fda_sheet, exist_ok=True)
    
    

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
    
    df_fda = pd.read_excel(fda_path, sheet_name="FDA+FDA CDx_SNVGT")
    df_patient_data= pd.read_excel(crcm_path,sheet_name='Source')

    df_fda['Status']= np.where((df_fda["GENE"].isin(df_patient_data["Gene.refGene"]) &(df_fda["PSEUDOVARIANT"].isin(df_patient_data["AAChange"]))), 'Positive', 'Negative')
    df_filtered=df_fda

    result = df_filtered.loc[(df_filtered['GENE'].isin(df_patient_data['Gene.refGene'])) &(df_filtered['PSEUDOVARIANT'].isin(df_patient_data['AAChange']))]
    df_cd = pd.merge(result, df_patient_data, how='inner', left_on = 'VARIANT', right_on = 'AAChange')

    df_cd.drop(['Chr', 'Start_y',
        'End', 'Ref', 'Alt', 'Gene.refGene', 'AAChange', 'AAChange_CDS',
        'fathmm-MKL_coding_score', 'cosmic_id', 'Report_Decision', 'Otherinfo1',
        'Otherinfo2', 'Otherinfo3', 'Otherinfo4', 'Otherinfo5', 'Otherinfo6',
        'Otherinfo7', 'Otherinfo8', 'Otherinfo9', 'Otherinfo10', 'Otherinfo11',
        'Otherinfo12', 'Otherinfo13', 'DP_Total', 'MQ', 'TLOD',
        'FractionInformativeReads', 'GT', 'AD','F1R2', 'F2R1',
        'DP_Sample', 'OBC', 'SB', 'MB', 'PS', 'Gene', '2455_Gene_Source',
        '2455_Gene_Alias', 'Gene_Alias2'], axis=1, inplace=True)

# # result['Status']=np.where(df_fda["GENE"].isin(df_patient_data["Gene.refGene"]), True, False)
    output_file_folder= os.path.join(str(fda_sheet),str(fda_sheet)+'.xlsx')
    
    df_cd.drop([ 'VARIANT CDS', 'EXON', 
        'PSEUDOVARIANT CDS', 'TYPE OF VARIANT', 'COMBINATION MARKER', 
        'VARIANT ORIGIN', 'ZYGOSITY',
        'EVIDENCE STATEMENT FROM LABEL',
            'SIGNIFICANCE', 'LEVELS OF EVIDENCE',
        'TYPE OF EVIDENCE', 'REMARKS', 'REFERENCES', 'PMID', 'DOID',
        'Chromosome', 'Start_x', 'Stop', 'Size (kb)', 'Cytoband',
        'ARCHIVAL NUMBER', 'SOURCE', 'LABEL DATE'], axis=1, inplace=True)
    
    df_cd.rename(columns = {'EVIDENCE STATEMENT 1':'EVIDENCE_STATEMENT_1', 'EVIDENCE STATEMENT 2':'EVIDENCE_STATEMENT_2','CANCER TYPE':'CANCER_TYPE'}, inplace = True)
    df_files = df_cd['CANCER_TYPE'].values.tolist()
    for i in df_files:
        result=" ".join(i.split()[2:])

        df_cd['CANCER_TYPES']= result
        
    df_cd.drop(['CANCER_TYPE'],axis = 1,inplace=True)
   
    df_cd.to_excel(output_file_folder)
    print(df_cd)
    # time.sleep(10)
    # for files in result:
       
    #     if files.startswith("fda_output_files"):
    #         fda_output_files = files
    #         fda_output_path = str(res) + "/" + str(fda_output_files)
    #         break
    # time.sleep(5)
    # fda_path = pd.read_excel(fda_output_path, sheet_name="Sheet1")
    time.sleep(5)
    output_json_file= os.path.join(res,'fda_reports.json') 
    
    with open(output_json_file, 'w') as f:
        json.dump(df_cd.to_dict(orient='records'), f)
    
    time.sleep(10)
    with open(output_json_file,'r') as j:
        files = json.loads(j.read())
    return Response(files)

    
    
    

   
@api_view(["GET"])
def process_clilical_files(request): 
    res = Path.joinpath(Path(MEDIA_ROOT), 'Files_folder',
                        'clinical_trial_file')
    result = os.listdir(res)
    #================= fad_file_path===========#
    fda_path= Path.joinpath(Path(MEDIA_ROOT), 'Files_folder')
    print(fda_path)
    
    for files in os.listdir(fda_path):
        if files.startswith('fda_output_files.xlsx'):
            print(files)
            fda_files_path= os.path.join(fda_path,files)
            print(fda_files_path)
    df_fda= pd.read_excel(fda_files_path,sheet_name='Sheet1')
    df_fda.drop(['Unnamed: 0'],axis=1,inplace=True)
    df_fda.reset_index(drop=True,inplace=True)
    print(df_fda)

    for files in result:
        print(files)
    abpath = str(res) + "/" + str(files)
    print(abpath)
    
    
   
            
    
   
            
    df= pd.read_excel(abpath)
   
    

    df.drop(['Unnamed: 0','gene_found_in',  'gene_aliases_found', 'variants_found_in', 'role_in_cancer', 'protein_effect', 'impact',
            'associated_with_drug_resistance', 'intervention_other_name', 'intervention_description', 'arm_title',
            'arm_description', 'arm_group_intervention', 'eligibility_criteria',
            'inclusion_criteria', 'exclusion_criteria', 'primary_om_title',
            'primary_om_description', 'secondary_om_title',
            'secondary_om_description', 'other_om_title', 'other_om_description',
            'keywords', 'mesh_terms', 'pmid',


            'brief_title',
            'brief_summary', 'detailed_description'], axis=1, inplace=True)


    print(df.head(10))

    df_study_type_filter=df[(df['study_type'] == 'Interventional') | (df['study_type'] == 'Expanded Access')]

    df_study_purpose_filter= df_study_type_filter[df_study_type_filter['study_purpose'] == 'Treatment' ]

    df_level_filter= df_study_purpose_filter[df_study_type_filter['level'] == '1A']

    df_recruitment_col_filter=df_level_filter[(df_level_filter['recruitment_status']=='Not yet recruiting')|(df_level_filter['recruitment_status']=='Recruiting') | (df_level_filter['recruitment_status']== 'Enrolling by invitation') | (df_level_filter['recruitment_status']=='Active, not recruiting')]
    print(df_recruitment_col_filter)
    Genes= ['EGFR']
    variants=['l858r']
    cancer_types= 'Lung Cancer' .lower()
    df_gene_find= df_recruitment_col_filter[df_recruitment_col_filter['gene_name'].isin(Genes)]

    df_variant_filter= df_gene_find[df_gene_find['variant_found'].isin(variants)]

    df_variant_filter=df_variant_filter.reset_index()





    final_draft=df_variant_filter[df_variant_filter.cancer_type.str.contains(cancer_types,flags=regex.IGNORECASE, regex= True, na=False)]
    final_draft.reset_index(inplace = True)
    final_draft.drop(['level_0','index'], axis=1, inplace=True)

    final_draft['BioMarker'] = final_draft['gene_name'].str.cat(final_draft['variant_found'], sep =" ")

    final_draft['Reference']  = final_draft[['nct_id', 'phase','recruitment_status']].apply(lambda x: ' | '.join(x), axis = 1)


    final_draft.drop([
        'gene_id',  'gene_name', 'study_type', 'study_purpose',
        'study_model', 'recruitment_status', 'phase', 'level', 
        'cancer_type',  'drug_found', 'drug_not_found',
        'drug_target', 'drug_target_pathway',
        'variant_match_type', 'curation_status', 'curator',
        'curator_comments', 'last_update_post_date', 'id', 
        
    ],axis=1, inplace=True)

    final_draft['BioMarker']=  final_draft['BioMarker'].str.upper()
    final_draft['variant_found']= final_draft['variant_found'].str.upper()
   
    df_new_data = pd.merge(final_draft, df_fda, how='inner', left_on = 'variant_found', right_on = 'VARIANT')
   
    df_final=df_new_data.drop_duplicates(subset='nct_id', keep='last')
    df_final.reset_index(drop=True,inplace=True)
    outputfile_kgct= os.path.join(str(res), 'kgct_results.xlsx')
    df_final.to_excel(outputfile_kgct)
    

    return Response('completed')
    
    
    
@api_view(['GET'])
def vus_results(result): 
       
    with open('/home/aravind/Desktop/DjangoProjects/djangoprojects/media/Files_folder/fda_output_files/snv.json','r') as j:
        snv_file = json.loads(j.read())
        
    with open('/home/aravind/Desktop/DjangoProjects/djangoprojects/media/Files_folder/fda_output_files/indel.json','r') as j:
        indel_file = json.loads(j.read())
    
    return Response({'indel':indel_file, "snv":snv_file})






### VUS format
# import pandas as pd
# import numpy as np
# import json
# snv_path='/content/CRCM3_CG_NS,FS,SGL_N_FOR_LIST_Report.xlsx'
# indel_path= '/content/CRCM3_CG_NS,FS,SGL_B_FOR_LIST_Report.xlsx'
# fda_path = '/content/fda_output_files.xlsx'
# df_snv= pd.read_excel(snv_path,sheet_name='Cols Sorted')
# df_indel= pd.read_excel(indel_path,sheet_name='Cols Sorted')
# df_fda_result= pd.read_excel(fda_path,sheet_name='Sheet1')

# df_snv.rename(columns = {'Gene.refGene':'GENE', 'AAChange':'AMINO_ACID_CHANGE'}, inplace = True)
# df_snv


# df_indel.rename(columns = {'Gene.refGene':'GENE', 'AAChange':'AMINO_ACID_CHANGE'}, inplace = True)
# df_snv