from pathlib import Path
import time
import csv
import os
import requests as re
import pandas as pd
import string
import threading
from shutil import copyfile
from multiprocessing import Process
from djangoprojects.settings import MEDIA_ROOT
from .findfile import filepath
from .svcnvtableTO import cnv_svextractorTO
from .ichorCNA import RunIchorCNA
from distutils.util import strtobool
from sqlite3 import IntegrityError
from .CNVkit_run import RunCNVkit,RunHeatMap,LOH_Runner,compare_cnv_and_re2_file

from KyvorPipeline.pipelinesupport import basespace, annovar, msisensor, annotsv, SvCurationV4, CnvCurationV4,CNVkit_run


from KyvorPipeline.models import Basespace, Project, Biosample, AnalysisStatus


def CurationDE(project_key, analysis_id):
    currentProject = Project.objects.latest('id')
    projectData = Project.objects.get(id=project_key)
    
    project_name = projectData.project_name

    # Check Analysis Done or not
    while True:
        time.sleep(10)
        print(projectData, analysis_id)
        checkDE = basespace.checkAnalysisStatus(projectData.id, analysis_id)
        if checkDE != "Complete":
            print("DE Not Completed yet")
        else:
            print(checkDE)
            break

    try:
        # refresh basespace projects
        bs_projects_path = "/home/aravind/basespace/Projects/"
        os.chdir(bs_projects_path)
        refresh_basespace = os.popen("basemount-cmd refresh")
        mount = refresh_basespace.read()
        print("Refreshing Basespace")
    except Exception as ex:
        print(ex)
        print("Exception Error")

    # Launch Annovar
    saveAnalysis = AnalysisStatus.objects.create(
        analysis_type="DE_Annotsv",
        analysis_ref_id=projectData,
        analysis_status="Started",
        analysis_description="DE Annotsv-VCF to tsv file conversion"
    )
    print("Running AnnotSv")
    # Get VCF file

    # Mkdir for Annovar VCF File
    annotsv_folder = Path.joinpath(
        Path(MEDIA_ROOT), project_name, "Biosamples", "VCFs", "DE", "TO")
    os.makedirs(annotsv_folder, exist_ok=True)

    # Find DSP VCF Files
    appsession_id = ".id."+str(analysis_id)
    # example structure
    # /root/basespace/Projects/INDTNA28221_v4_5/AppSessions/.id.423732341/AppResults.253723656.INDTNA28221_v4_5_BS_TO/Files/
    appsession_path = os.path.join(
        "/home","aravind" ,"basespace", "Projects", project_name, "AppSessions", appsession_id)

    for folder in os.listdir(appsession_path):
        print(folder)
        if "AppResult" in folder:
            de_files_folder = os.path.join(appsession_path, folder, "Files")
            break
    cnv_vcf_file_name = ""
    sv_vcf_file_name = ""
    sv_vcf_file_path = ""
    cnv_vcf_file_path = ""
    for file in os.listdir(de_files_folder):
        if file.endswith("cnv.vcf.gz"):
            cnv_vcf_file_path = os.path.join(de_files_folder, file)
            cnv_vcf_file_name = file
            break

    for file in os.listdir(de_files_folder):
        if file.endswith("sv.vcf.gz"):
            sv_vcf_file_path = os.path.join(de_files_folder, file)
            sv_vcf_file_name = file
            break

    for file in os.listdir(de_files_folder):
        if file.endswith("bam"):
            de_bam_file_path = os.path.join(de_files_folder, file)
            de_bam_file_name = file
            break
        
    for file in os.listdir(de_files_folder):
        if file.endswith("hard-filtered.vcf.gz"):
            vcf_file_path = os.path.join(de_files_folder, file)
            vcf_file_name = file
            break

    # Move SV Vcf
    sv_local_vcf_file = os.path.join(annotsv_folder, sv_vcf_file_name)
    print("VCF-BS", sv_vcf_file_path, sv_local_vcf_file)
    copyfile(sv_vcf_file_path, sv_local_vcf_file)

    # Move CNV Vcf
    cnv_local_vcf_file = os.path.join(annotsv_folder, cnv_vcf_file_name)
    print("VCF-BS", cnv_vcf_file_path, cnv_local_vcf_file)
    copyfile(cnv_vcf_file_path, cnv_local_vcf_file)

    # Launch AnnotSV
    annotated_files_folder = Path.joinpath(
        Path(MEDIA_ROOT), project_name, "Annotated_Files", "AnnotSv", "TO")
    os.makedirs(annotated_files_folder, exist_ok=True)
    initiate_annotsv_sv = annotsv.RunAnnotsv(
        sv_local_vcf_file, annotated_files_folder, "SV")
    initiate_annotsv_cnv = annotsv.RunAnnotsv(
        cnv_local_vcf_file, annotated_files_folder, "CNV")

    print(initiate_annotsv_cnv, initiate_annotsv_sv)

    # Launch Curation Program

    # Output Folder
    sv_output_folder = project_name + "_SV"
    cnv_output_folder = project_name + "_CNV"
    sv_curation_output_folder = Path.joinpath(
        Path(MEDIA_ROOT), project_name, "DE_Outputs", "TO", sv_output_folder)
    os.makedirs(sv_curation_output_folder, exist_ok=True)

    cnv_curation_output_folder = Path.joinpath(
        Path(MEDIA_ROOT), project_name, "DE_Outputs", "TO", cnv_output_folder)
    os.makedirs(cnv_curation_output_folder, exist_ok=True)

    ichorCNA_output_folder = Path.joinpath(
        Path(MEDIA_ROOT), project_name, "DE_Outputs", "TO", "ichorCNA_TO")
    os.makedirs(ichorCNA_output_folder, exist_ok=True)
    
    CNVkit_output_folder = Path.joinpath(
        Path(MEDIA_ROOT), project_name, "DE_Outputs", "TO", "CNVkit_Outputs")
    os.makedirs(CNVkit_output_folder, exist_ok=True)

    # get Annotated File Path
    sv_txt_file = ""
    cnv_txt_file = ""
    for file in os.listdir(annotated_files_folder):
        if file.endswith("SV.tsv"):
            sv_txt_file = os.path.join(annotated_files_folder, file)
        elif file.endswith("CNV.tsv"):
            cnv_txt_file = os.path.join(annotated_files_folder, file)

    dcb_file = "/home/aravind/Desktop/CurationV4/INTEGRATED_DCP.xlsx"

    """
    DE SV Inputs
    svFile = "/home/arun/wfh/INDKAA57861/INDKAA57861_TO_SV.tsv"
    integratedDCP = "/home/arun/wfh/v4/INTEGRATED_DCP-28-8-20.xlsx"
    path = "INDKAA57861_SV_TO"
    """

    callSV = SvCurationV4.svextractor(
        sv_txt_file, dcb_file, str(sv_curation_output_folder))

    """
    cnvFile = "/home/arun/wfh/INDKAA57861/INDKAA57861_TO_CNV.tsv"
    integratedDCP = "/home/arun/wfh/v4/INTEGRATED_DCP-28-8-20.xlsx"
    path = "INDKAA57861_CNV_TO"
    exonFile = "ncbiRefSeq.txt"
    cnaFile = "BRCA_CNA_Genes.txt"
    callCNV = cnvextractor(cnvFile, integratedDCP, cnaFile, path)
    """

    exon_file = "/home/aravind/Desktop/CurationV4/ncbiRefSeq.txt"
    cna_file = "/home/aravind/Desktop/CurationV4/BRCA_CNA_Genes.txt"
    callCNV = CnvCurationV4.cnvextractor(
        cnv_txt_file, dcb_file, cna_file, str(cnv_curation_output_folder))

    time.sleep(5)

    # DE Results Folder
    de_folder = Path.joinpath(Path(MEDIA_ROOT), project_name, "DE_Outputs")
    sv_2455_gene_alias_file = filepath(
        str(de_folder), "SVPASS_2455_Gene_Alias")
    cnv_2455_gene_alias_file = filepath(
        str(de_folder), "CNV_PASS_2455_Gene_Alias")
    print("Table Files", sv_2455_gene_alias_file, cnv_2455_gene_alias_file)
    launchTable = cnv_svextractorTO(str(sv_2455_gene_alias_file), str(
        cnv_2455_gene_alias_file), str(de_folder))

    time.sleep(10)
    saveAnalysis = AnalysisStatus.objects.create(
        analysis_type="DE_IchorCNA",
        analysis_ref_id=projectData,
        analysis_status="Started",
        analysis_description="DE IchorCNA started"
    )
    print("Running ichorCNA")
    launchIchorCna = RunIchorCNA(
        de_bam_file_path, ichorCNA_output_folder, "TO")
    
    time.sleep(10)
    saveAnalysis = AnalysisStatus.objects.create(
        analysis_type="DE_CNVkit",
        analysis_ref_id=projectData,
        analysis_status="Started",
        analysis_description="DE CNVkit started"
    )
    print("Running DE CNVkit")
    RunCNVkit(
        de_bam_file_path, '/home/aravind/Downloads/cnvkit_bed.bed', '/home/aravind/Downloads/hg19.fa', CNVkit_output_folder, "TO")
    
    RunHeatMap(project_key=currentProject.id, filtered_vcf=vcf_file_path)
    LOH_Runner(project_key=currentProject.id)
    compare_cnv_and_re2_file(project_key=currentProject.id,cnv_pass_file=cnv_2455_gene_alias_file)
    
    
    
    
    

    



    
    
    
    
