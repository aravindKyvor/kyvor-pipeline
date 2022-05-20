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

def RunIchorCNA(bam_file, output_dir, run_type):
    print("CMD", bam_file, output_dir)

    return_data = {}

    outfile_name = str(bam_file).split("/")[-1].split(".")[0]
    wig_file_name = os.path.join(output_dir, outfile_name + "_readcount.wig")
    ichorcna_file_name = os.path.join(output_dir, outfile_name + "_ichorCNA")
    ichorcna_file = outfile_name + "_ichorCNA"
    """
    Create wig file
    
    ./readCounter -w 1000 
    /root/basespace/Projects/INDTSB72723/AppSessions.v1/INDTSB72723_DE_TO/AppResults.254195308.INDTSB72723_BS_TO/Files/INDTSB72723_BS_TO.bam 
    > /root/72723_ichor/72723_readcount.wig
    """

   # os.chdir("/root/ichorCNA/hmmcopy_utils-master/bin/")

    wig_cmd = "/home/aravind/Desktop/ichorCNA/hmmcopy_utils/bin/readCounter -w 1000 "
    wig_cmd = wig_cmd + bam_file + " > "
    wig_cmd = wig_cmd + wig_file_name

    try:
        print(wig_cmd)
        time.sleep(5)
        call_wig = os.popen(wig_cmd)
        time.sleep(10)
    except IOError as io:
        return_data["Status"] = 501
        return_data["Code"] = "Err11-01",
        return_data["Message"] = "IchorCNA - wig file creation failed"
        return_data["Reference"] = io
        return_data["Type"] = False

        return return_data

    res_wig = call_wig.read()

    if not return_data:
        """
        ichorCNA Rscript CMD TO
        Rscript /path/to/ichorCNA/scripts/runIchorCNA.R --id tumor_sample \
        --WIG /path/to/tumor.wig --estimatePloidy
        --gcWig /path/to/ichorCNA/inst/extdata/gc_hg19_1000kb.wig \
        --outDir ./
        
        Rscript runIchorCNA.R --id INDTNA55362 
        --WIG /root/ichorCNA_test/INDTNA55362_BS_TO_readcount.wig 
        --estimatePloidy true 
        --gcWig /root/ichorCNA/hmmcopy_utils-master/data/gc_hg19.wig 
        --outDir /root/ichorCNA_test
        
        """

        ichorCNA_cmd = "Rscript /home/aravind/Desktop/ichorCNA/scripts/runIchorCNA.R --id "
        ichorCNA_cmd = ichorCNA_cmd + ichorcna_file + " --WIG "
        ichorCNA_cmd = ichorCNA_cmd + wig_file_name + " --estimatePloidy true --gcWig /home/aravind/Desktop/ichorCNA/hmmcopy_utils-master/data/gc_hg19.wig --outDir "
        ichorCNA_cmd = ichorCNA_cmd + str(output_dir)

        try:
            print(ichorCNA_cmd)
            time.sleep(5)
            call_wig = os.popen(ichorCNA_cmd)
            time.sleep(10)
        except IOError as io:
            return_data["Status"] = 501
            return_data["Code"] = "Err11-02",
            return_data["Message"] = "IchorCNA - ichorCNA run failed"
            return_data["Reference"] = io
            return_data["Type"] = False

            return return_data

    res_ichorcna = call_wig.read()

    return_data["Status"] = 201
    return_data["Message"] = "AnnotSV Completed"
    return_data["Reference"] = format(res_ichorcna)
    return_data["Type"] = True

    return return_data
