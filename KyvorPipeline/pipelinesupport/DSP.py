from pathlib import Path
import time
import os
import requests as re
import string
import threading
from shutil import copyfile
from djangoprojects.settings import MEDIA_ROOT

from distutils.util import strtobool
from sqlite3 import IntegrityError

from KyvorPipeline.pipelinesupport import basespace, annovar, msisensor, CurationV3


from KyvorPipeline.models import Basespace, Project, Biosample, AnalysisStatus

def CurationDSP(project_key, analysis_id):

    projectData = Project.objects.get(id=project_key)
    project_name = projectData.project_name


    #Check Analysis Done or not
    while True:
        time.sleep(10)
        print(projectData, analysis_id)
        checkDSP = basespace.checkAnalysisStatus(projectData.id, analysis_id)
        if checkDSP != "Complete":
            print("DSP Not Completed yet")
        else:
            print(checkDSP)
            break

    try:
        #refresh basespace projects
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
        analysis_type="DSP_Annovar",
        analysis_ref_id=projectData,
        analysis_status="Started",
        analysis_description="DSP Annovar-VCF to multianno text file conversion"
    )
    print("Running Annovar")
    #Get VCF file

    #Mkdir for Annovar VCF File
    annovar_folder = Path.joinpath(Path(MEDIA_ROOT), project_name, "Biosamples", "VCFs", "DSP", "TO")
    os.makedirs(annovar_folder, exist_ok=True)

    #Find DSP VCF Files
    appsession_id = ".id."+str(analysis_id)
    #example structure
    #/root/basespace/Projects/INDTNA28221_v4_5/AppSessions/.id.423732341/AppResults.253723656.INDTNA28221_v4_5_BS_TO/Files/
    appsession_path = os.path.join("/home","aravind","basespace","Projects",project_name,"AppSessions",appsession_id)

    for folder in os.listdir(appsession_path):
        print(folder)
        if "AppResult" in folder:
            dsp_files_folder = os.path.join(appsession_path, folder, "Files")
            break
    vcf_file_name = ""
    vcf_file_path = ""
    for file in os.listdir(dsp_files_folder):
        if file.endswith("hard-filtered.vcf.gz"):
            vcf_file_path = os.path.join(dsp_files_folder, file)
            vcf_file_name = file
            break

    for file in os.listdir(dsp_files_folder):
        if file.endswith(".bam"):
            bam_file_path = os.path.join(dsp_files_folder, file)
            bam_file_name = file
            break

    local_vcf_file = os.path.join(annovar_folder, vcf_file_name)
    print("VCF-BS",vcf_file_path, local_vcf_file)
    copyfile(vcf_file_path, local_vcf_file)

    #Launch Annovar
    annotated_files_folder = Path.joinpath(Path(MEDIA_ROOT), project_name, "Annotated_Files", "Annovar", "TO")
    os.makedirs(annotated_files_folder, exist_ok=True)
    initiate_annovar = annovar.RunAnnovar(local_vcf_file,annotated_files_folder, "TO")
    print(initiate_annovar)

    #Launch MSI
    if "_" in project_name:
        msi_file_name = project_name.split("_")[0] +str("_MSI")
    else:
        msi_file_name = project_name + str("_MSI")
    msi_files_folder = Path.joinpath(Path(MEDIA_ROOT), project_name, "MSI")
    msi_file_name = Path.joinpath(msi_files_folder, msi_file_name)
    os.makedirs(msi_files_folder, exist_ok=True)
    initiate_msi = msisensor.RunMsiSensorTO(bam_file_path, msi_file_name)

    print(initiate_msi)

    #Launch Curation Program

    #Output Folder
    curation_output_folder = Path.joinpath(Path(MEDIA_ROOT), project_name, "DSP_Outputs", "TO")
    os.makedirs(curation_output_folder, exist_ok=True)

    #get Annotated File Path
    multianno_txt_file = ""

    for file in os.listdir(annotated_files_folder):
        if file.endswith(".txt"):
            multianno_txt_file = os.path.join(annotated_files_folder, file)


    """
    DSP Inputs
    dspantxt="/root/INDTNA28221/INDTNA28221_multianno.hg38_multianno.txt"
    #curationappath='/home/arun/wfh/v4/'
    curationappath="/root/INDTNA28221/"
    dbdata='/root/CurationV4/INTEGRATED_DCP.xlsx'
    espfile=curation(dspantxt,'/root/annovar/humandb/CosmicMutantExport.tsv','/root/CurationV4/cancer_gene_census.csv',"",
    curationappath,dbdata)
    """

    cme_path = "/home/aravind/efs/annovar/humandb/CosmicMutantExport.tsv"
    cge_path = "/home/aravind/Desktop/CurationV4/cancer_gene_census.csv"
    dcb_file = "/home/aravind/Desktop/CurationV4/INTEGRATED_DCP.xlsx"

    curation_program_to = CurationV3.curation(multianno_txt_file, cme_path, cge_path, "", str(curation_output_folder), dcb_file)
    print(curation_program_to)
















