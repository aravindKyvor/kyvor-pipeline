import os
from pathlib import Path
import time
import requests as re
import string
from djangoprojects.settings import MEDIA_ROOT
from distutils.util import strtobool
from sqlite3 import IntegrityError
from KyvorPipeline.pipelinesupport import basespace
from KyvorPipeline.models import Basespace, Project, Biosample, AnalysisStatus

def RunAnnovar(dsp_vcf_file, output_dir, run_type):
    print("CMD", dsp_vcf_file, output_dir)

    return_data = {}

    outfile_name = str(dsp_vcf_file).split("/")[-1].split(".")[0]
    multianno_name = os.path.join(output_dir, outfile_name + "_multianno")
    avinput_name = os.path.join(output_dir, outfile_name + ".avinput")

    avinput_cmd = "perl /home/aravind/efs/annovar/convert2annovar.pl -format "
    if run_type == "TO":
        avinput_cmd = avinput_cmd + " vcf4 "
    elif run_type == "TN":
        avinput_cmd = avinput_cmd + " vcf4old "
    avinput_cmd = avinput_cmd + dsp_vcf_file + " "
    avinput_cmd = avinput_cmd + "-outfile " + avinput_name + " "
    avinput_cmd = avinput_cmd + "-includeinfo -withzyg"

    try:
        print(avinput_cmd)
        time.sleep(5)
        call_avinput = os.popen(avinput_cmd)
        time.sleep(10)
    except IOError as io:
        return_data["Status"] = 501
        return_data["Code"] = "Err07-05",
        return_data["Message"] = "Annovar - VCF to AvInput failed"
        return_data["Reference"] = io
        return_data["Type"] = False

        return return_data

    res_avinput = call_avinput.read()
    print(res_avinput)


    """
    annovar command
    perl convert2annovar.pl -format vcf4 /root/basespace/Projects/INDKAA57861/AppSessions.v1/INDKAA57861_DSP_TO/AppResults.253230011.INDKAA57861_BS_TO/Files/
    INDKAA57861_BS_TO.hard-filtered.vcf.gz
     -outfile /root/INDKAA57861/INDKAA57861.avinput -includeinfo -withzyg
    
    "perl table_annovar.pl /home/efs/PATIENT_ID/PATIENT_ID.avinput humandb/ -buildver hg38 
    -out /home/efs/PATIENT_ID/PATIENT_ID_multianno -remove -protocol refGene,cytoband,exac03,1000g2015aug_all,1000g2015aug_afr,
    1000g2015aug_amr,1000g2015aug_sas,1000g2015aug_eur,1000g2015aug_eas,avsnp150,dbnsfp35c,cosmicv89_coding,clinvar_20190305,
    esp6500siv2_all,gnomad211_exome,intervar_20180118 -operation g,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f -polish -otherinfo -nastring ."
    """

    annovar_cmd = "perl /home/aravind/efs/annovar/table_annovar.pl "+avinput_name + " "
    annovar_cmd = annovar_cmd + "/home/aravind/efs/annovar/humandb/ -buildver hg38 -out "+multianno_name + " "
    annovar_cmd = annovar_cmd + "-remove -protocol refGene,cytoband,exac03,1000g2015aug_all,1000g2015aug_afr,"
    annovar_cmd = annovar_cmd + "1000g2015aug_amr,1000g2015aug_sas,1000g2015aug_eur,1000g2015aug_eas,avsnp150,dbnsfp35c,"
    annovar_cmd = annovar_cmd + "cosmicv89_coding,clinvar_20190305,esp6500siv2_all,gnomad211_exome,intervar_20180118"
    annovar_cmd = annovar_cmd + " -operation g,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f -polish -otherinfo -nastring ."

    try:
        print(annovar_cmd)
        call_annovar = os.popen(annovar_cmd)
        time.sleep(10)
    except IOError as io:
        return_data["Status"] = 501
        return_data["Code"] = "Err07-02",
        return_data["Message"] = "Annovar - AvInput to Multianno txt file failed"
        return_data["Reference"] = io
        return_data["Type"] = False

        return return_data

    res_annovar = call_annovar.read()
    print(res_annovar)

    return_data["Status"] = 501
    return_data["Message"] = "Annovar Completed"
    return_data["Reference"] = format(res_annovar)
    return_data["Type"] = True

    return return_data
