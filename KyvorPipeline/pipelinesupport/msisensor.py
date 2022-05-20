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

def RunMsiSensorTO(bam_file, msi_file_name):
    print("FilePath", bam_file, msi_file_name)

    return_data = {}
    """
    MSI Command
    ./msisensor2 msi -M models_hg38/ -t 
    /home/ubuntu/basespace/Projects/CRCM4_TN/AppSessions/CRCM4_TN_TN/AppResults.237382203.CRCM4_TN_BS_TO/Files/CRCM4_TN_BS_TO.bam
     -o /home/ubuntu/efs/msisensor2/CRCM4_TN_MSI
    """

    #msi_folder = "/root/msisensor2/"


    msi_cmd = "/home/aravind/tools/msisensor2/./msisensor2 msi -M /home/aravind/tools/msisensor2/models_hg38/ -t "
    msi_cmd = msi_cmd + bam_file + "  -o "
    msi_cmd = msi_cmd + str(msi_file_name)

    try:
        print(msi_cmd)
        call_msi = os.popen(msi_cmd)
        time.sleep(10)
    except IOError as io:
        return_data["Status"] = 501
        return_data["Code"] = "Err07-02",
        return_data["Message"] = "Annovar - AvInput to Multianno txt file failed"
        return_data["Reference"] = io
        return_data["Type"] = False

        return return_data

    res_msi = call_msi.read()
    print(res_msi)

    return_data["Status"] = 501
    return_data["Message"] = "Annovar Completed"
    return_data["Reference"] = format(res_msi)
    return_data["Type"] = True

    return return_data




