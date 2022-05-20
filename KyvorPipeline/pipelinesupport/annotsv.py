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


def RunAnnotsv(vcf_file, output_dir, run_type):
    print("CMD", vcf_file, output_dir)

    return_data = {}

    outfile_name = str(vcf_file).split("/")[-1].split(".")[0]
    if run_type == "SV":
        out_file_name = os.path.join(output_dir, outfile_name + "_SV.tsv")
    if run_type == "CNV":
        out_file_name = os.path.join(output_dir, outfile_name + "_CNV.tsv")
    """
    AnnotSV Command
    
    $ANNOTSV/bin/AnnotSV -SVinputFile INDTNA14762_BS_TO.sv.vcf.gz -outputFile /home/ubuntu/AnnotSV/INDTNA14762_TO_DE_SV.tsv -svtBEDcol 4
    """
    
    annotsv_cmd =   "$ANNOTSV/bin/AnnotSV -SVinputFile "
    annotsv_cmd = annotsv_cmd + vcf_file + " "
    annotsv_cmd = annotsv_cmd + "-outputFile " + out_file_name + " "
    annotsv_cmd = annotsv_cmd + "-svtBEDcol 4"

    try:
        print(annotsv_cmd)
        time.sleep(5)
        call_annotsv = os.popen(annotsv_cmd)
        time.sleep(10)
    except IOError as io:
        return_data["Status"] = 501
        return_data["Code"] = "Err07-05",
        return_data["Message"] = "AnnotSV - VCF to AnnotSV Txt failed"
        return_data["Reference"] = io
        return_data["Type"] = False

        return return_data

    res_annotsv = call_annotsv.read()

    return_data["Status"] = 501
    return_data["Message"] = "AnnotSV Completed"
    return_data["Reference"] = format(res_annotsv)
    return_data["Type"] = True

    return return_data