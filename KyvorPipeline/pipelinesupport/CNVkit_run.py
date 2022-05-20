from pathlib import Path
import time
import glob
import string
from openpyxl import load_workbook
from multiprocessing import Process
import os.path
import subprocess
import fnmatch
import os
import pandas as pd
import csv
from distutils.util import strtobool
from sqlite3 import IntegrityError
from djangoprojects.settings import MEDIA_ROOT
from KyvorPipeline.pipelinesupport import basespace
from KyvorPipeline.models import Basespace, Project, Biosample, AnalysisStatus


def RunCNVkit(bam_file, bed_file, ref_genome, output_dir,run_type):
    print("CMD", bam_file, output_dir)
    print(bam_file)

    
   

    return_data = {}

    outfile_name = str(bam_file).replace("_", " ")
    
    split_bam_name = outfile_name.split()
   
    outs = split_bam_name[0]
   

    output_files = outs + ".CNN"
   

    outerjoin1 = output_files.split('/')
    print(outerjoin1[-1])
    outerjoin = outerjoin1[-1]
    print(outerjoin)

    

    CNV_cmd = "$cnvkit cnvkit.py batch "
    CNV_cmd = CNV_cmd + bam_file + " " + "-n" + " " + "-t" + " "
    CNV_cmd = CNV_cmd + bed_file + " " + "-f" + " " + ref_genome + " "
    CNV_cmd = CNV_cmd + "--output-reference " + \
        outerjoin + " " + "-d" + " " + output_dir + " " 
    CNV_cmd = CNV_cmd + "--scatter " + " " + "--diagram"

    try:
        print(CNV_cmd)

        cnvkit = os.popen(CNV_cmd)
       
    except IOError as io:
        return_data["Status"] = 501
        return_data["Code"] = "Err07-05",
        return_data["Message"] = "CNV failed"
        return_data["Reference"] = io
        return_data["Type"] = False

        return return_data

    res_cnv = cnvkit.read()

    return_data["Status"] = 501
    return_data["Message"] = "cnv Completed"
    return_data["Reference"] = format(res_cnv)
    return_data["Type"] = True
    
    return return_data
    





def RunHeatMap(project_key,filtered_vcf):
       
        time.sleep(30)
        return_data = {}

        projectData = Project.objects.get(id=project_key)
        project_name = projectData.project_name
        
        # abpath = "/home/aravind/Desktop/DjangoProjects/djangoprojects/media/media/" + \
        #     "{}".format(project_name) + "/DE_Outputs/TO/CNVkit_Outputs"
        print(abpath)
        
        abpath= Path.joinpath(
                            Path(MEDIA_ROOT), project_name, "DE_Outputs","TO","CNVkit_Outputs")

        print(abpath)

        output_dir = os.path.join(abpath)
        filter_value_cns_output= os.path.join(output_dir, str(project_name)+'_LOH.cns')
        for file1 in os.listdir(abpath):
            if file1.endswith(".cnr"):
                cnr_file = file1
                # print(file1)

        for file2 in os.listdir(abpath):
            if file2.endswith(".call.cns"):
                call_cns_file = file2
                # print(file1)

        print(cnr_file)
        print(call_cns_file)

        heatmap_path = abpath + "/"+cnr_file
        print(heatmap_path)

        paths = abpath + "/"+call_cns_file
        print(paths)
        csv_path_file = os.path.join(output_dir, str(project_name)+".csv")
        with open(paths, "r") as in_text:
            in_reader = csv.reader(in_text, delimiter='\t')
            with open(csv_path_file, "w") as out_csv:
                out_writer = csv.writer(out_csv)
                for row in in_reader:
                    out_writer.writerow(row)

        df = pd.read_csv(csv_path_file)
        print(df)
        df['gain/loss'] = df['log2'].apply(lambda x: 'gain' if x >=
                                        0.5 else ('loss' if x <= -0.5 else 'noCN'))
        df_gain = df.loc[df['gain/loss'] == 'gain']
        print(df_gain)
        df_loss = df.loc[df['gain/loss'] == 'loss']
        print(df_loss)

        try:
            outpath = os.path.join(output_dir, str(project_name)+'_cnv.xlsx')

        except Exception as e:
            print(e.message, e.args)
        with pd.ExcelWriter(outpath, engine='xlsxwriter') as writer:
            df.to_excel(writer, 'source', index=False)
            df_gain.to_excel(writer, 'Gain', index=False)
            df_loss.to_excel(writer, 'Loss', index=False)
            writer.save()

        HEAT_MAP = "$cnvkit cnvkit.py heatmap "
        HEAT_MAP = HEAT_MAP + " " + heatmap_path + " " + "-d" + " " + \
            "-o" + " " + output_dir + "/" + str(project_name) + "_CNV_heatmap.png"
        # cnvkit.py call Sample.cns -y -v Sample.vcf -o Sample.call.cns
        
        LOH_Converter= "$cnvkit cnvkit.py call "
        LOH_Converter= LOH_Converter + " "+ heatmap_path+ " " + "-y" + " " + "-v" + " " +  filtered_vcf +" " +"-o" + " " + filter_value_cns_output
        try:
            print(HEAT_MAP)

            heatmap = os.popen(HEAT_MAP)
            time.sleep(100)
            print(LOH_Converter)
            
            LOH_Converter= os.popen(LOH_Converter)
        except IOError as io:
            return_data["Status"] = 501
            return_data["Code"] = "Err07-05",
            return_data["Message"] = "failed"
            return_data["Reference"] = io
            return_data["Type"] = False

            return return_data

        res_cnv = heatmap.read()
        res_LOH = LOH_Converter.read()
        return_data["Status"] = 501
        return_data["Message"] = "Completed"
        return_data["Reference"] = format(res_cnv)
        return_data["Reference"] = format(res_LOH)
        return_data["Type"] = True

        return return_data
    
    
    
    


def LOH_Runner(project_key):
    projectData = Project.objects.get(id=project_key)
    project_name = projectData.project_name
    path = Path.joinpath(
                            Path(MEDIA_ROOT), project_name, "DE_Outputs","TO","CNVkit_Outputs")
    for file in os.listdir(path):
        if file.endswith("_LOH.cns"):
            Loh_file = file
    abspath = os.path.join(path, Loh_file)
    print(abspath)
    print(Loh_file)
    output_file_name = str(Loh_file).replace('.', ' ')
    outs = output_file_name.split()
    outfile = outs[0]
    # outs=output_file_name
    print(outfile)
    csv_path_file = os.path.join(path, str(outfile)+'.csv')
    print(csv_path_file)

    with open(abspath, "r") as in_text:
        in_reader = csv.reader(in_text, delimiter='\t')
        with open(csv_path_file, "w") as out_csv:
            out_writer = csv.writer(out_csv)
            for row in in_reader:
                out_writer.writerow(row)

    df = pd.read_csv(csv_path_file)
    df1 = df.dropna()
    xlsx_file_output = os.path.join(path, str(outfile)+'.xlsx')

    with pd.ExcelWriter(xlsx_file_output, engine='xlsxwriter') as writer:
        df1.to_excel(writer, 'source', index=False)

        writer.save()
    df2 = pd.read_excel(xlsx_file_output)
    df3 = df2.drop(df2[df2['cn1'] == 0].index)
    df3 = df2.drop(df2[df2['cn2'] == 0].index)

    def LOH(x):
        if x['cn1'] == x['cn2']:
            return 'LOH not observed'
        return 'LOH observed'
    df3['LOH'] = df3.apply(LOH, axis=1)
    df_LOH = df3
    print(df_LOH)

    df_LOH_Observed = df_LOH.loc[df_LOH['LOH'] == 'LOH observed']
    print(df_LOH_Observed)
    df_LOH_Not_Observed = df_LOH.loc[df_LOH['LOH'] == 'LOH not observed']
    print(df_LOH_Not_Observed)
    with pd.ExcelWriter(xlsx_file_output, engine='xlsxwriter') as writer:
        df.to_excel(writer, 'Source', index=False)
        df1.to_excel(writer, 'Empty Filtered', index=False)
        df_LOH.to_excel(writer, 'LOH', index=False)
        df_LOH_Observed.to_excel(writer, 'LOH Observed', index=False)
        df_LOH_Not_Observed.to_excel(writer, 'LOH Not Observed', index=False)

        writer.save()







def compare_cnv_and_re2_file(project_key,cnv_pass_file):
    projectData = Project.objects.get(id=project_key)
    project_name = projectData.project_name
    abpath= Path.joinpath(
                            Path(MEDIA_ROOT), project_name, "DE_Outputs","TO","CNVkit_Outputs")

    print(abpath)
    output_excel_file= os.path.join(abpath,str(project_name)+".Compared_CNV_&_RE2_file.xlsx")
    for file in os.listdir(abpath):
        if file.endswith("_cnv.xlsx"):
            excel_file = file
    re2_file = os.path.join(abpath, excel_file)
    print(re2_file)
    # convert input files to dataframe
    cnv_pass_df = pd.read_excel(
        cnv_pass_file, sheet_name="Sheet1")
    print(cnv_pass_df.columns)
    re2_df = pd.read_excel(re2_file, sheet_name="source", index_col=1)
    re2_gain_df = pd.read_excel(re2_file, sheet_name="Gain", index_col=1)
    re2_loss_df = pd.read_excel(re2_file, sheet_name="Loss", index_col=1)
    re2_df = re2_df.reset_index()
    # print(re2_df.columns)

    # columns to be dropped in cnv_pass_file
    columns_to_be_dropped = ['AnnotSV_ID', 'SV_chrom', 'SV_start', 'SV_end', 'SV_length', 'SV_type', 'Samples_ID', 'ID', 'REF', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'INDTSA54969_RE2_BS_TO', 'Annotation_mode', 'CytoBand', 'Gene_count', 'Tx', 'Tx_start', 'Tx_end', 'Overlapped_tx_length', 'Overlapped_CDS_length', 'Overlapped_CDS_percent', 'Frameshift', 'Exon_count', 'Location', 'Location2', 'Dist_nearest_SS', 'Nearest_SS_type', 'Intersect_start', 'Intersect_end', 'RE_gene', 'P_gain_phen', 'P_gain_hpo', 'P_gain_source', 'P_gain_coord', 'P_loss_phen', 'P_loss_hpo', 'P_loss_source', 'P_loss_coord', 'P_ins_phen', 'P_ins_hpo', 'P_ins_source', 'P_ins_coord', 'P_snvindel_nb', 'P_snvindel_phen', 'B_gain_source', 'B_gain_coord', 'B_gain_AFmax', 'B_loss_source', 'B_loss_coord', 'B_loss_AFmax', 'B_ins_source', 'B_ins_coord', 'B_ins_AFmax', 'B_inv_source', 'B_inv_coord', 'B_inv_AFmax', 'TAD_coordinate', 'ENCODE_experiment',
                             'COSMIC_ID', 'COSMIC_MUT_TYP', 'GC_content_left', 'GC_content_right', 'Repeat_coord_left', 'Repeat_type_left', 'Repeat_coord_right', 'Repeat_type_right', 'Gap_left', 'Gap_right', 'SegDup_left', 'SegDup_right', 'ENCODE_blacklist_left', 'ENCODE_blacklist_characteristics_left', 'ENCODE_blacklist_right', 'ENCODE_blacklist_characteristics_right', 'ACMG', 'HI', 'TS', 'DDD_HI_percent', 'DDD_status', 'DDD_mode', 'DDD_consequence', 'DDD_disease', 'DDD_pmid', 'ExAC_delZ', 'ExAC_dupZ', 'ExAC_cnvZ', 'ExAC_synZ', 'ExAC_misZ', 'GenCC_disease', 'GenCC_moi', 'GenCC_classification', 'GenCC_pmid', 'OMIM_ID', 'OMIM_phenotype', 'OMIM_inheritance', 'OMIM_morbid', 'OMIM_morbid_candidate', 'LOEUF_bin', 'GnomAD_pLI', 'ExAC_pLI', 'AnnotSV_ranking_score', 'AnnotSV_ranking_criteria', 'ACMG_class', 'GT', 'SM', 'BC', 'PE', 'Transcript ID', 'Chromosome', 'Strand', 'exon', 'Gene Name', 'NM', 'Gene', '2455_Gene_Source', '2455_Gene_Alias', 'Gene_Alias2']
    cnv_pass_df = cnv_pass_df.drop(columns_to_be_dropped, axis=1)
    cnv_pass_df.reset_index()

    result_list = []

    for cnv_index in cnv_pass_df.index:
        trial_list = []

        cnv_data_df = cnv_pass_df.loc[cnv_index]

        gene = cnv_data_df['Gene_name']
        print(gene)

        for re2_index in re2_df.index:
            # print(index)
    
            re2_data_df = re2_df.loc[re2_index]

            gene_data = re2_data_df['gene']

            if gene in gene_data:  # start	end	gene	log2	cn	depth	p_ttest	probes	weight	gain/loss
                print("found")
                chromosone = re2_data_df['chromosome']
                start = re2_data_df['start']
                end = re2_data_df['end']
                re2_gene = re2_data_df['gene']
                re2_cn = re2_data_df['cn']
                depth = re2_data_df['depth']
                p_ttest = re2_data_df['p_ttest']
                probes = re2_data_df['probes']
                weight = re2_data_df['weight']
                gain_loss = re2_data_df['gain/loss']
                gene_name = cnv_data_df['Gene_name']
                alt = cnv_data_df['ALT']
                cn = cnv_data_df['CN']

                trial_list.append(chromosone)
                trial_list.append(start)
                trial_list.append(end)
                trial_list.append(re2_gene)
                trial_list.append(re2_cn)
                trial_list.append(depth)
                trial_list.append(p_ttest)
                trial_list.append(probes)
                trial_list.append(weight)
                trial_list.append(gain_loss)
                trial_list.append(gene_name)
                trial_list.append(alt)
                trial_list.append(cn)

                result_list.append(trial_list)
                break

    print(result_list)

    # print(result_list)
    column_headings = ['Chromosome', 'start', 'end', 'gene_list', 'cn', 'depth',
                       'p_ttest', 'probes', 'weight', 'gain/loss', 'Pipeline_gene_name', 'Pipeline_alt', 'Pipeline_CN']
    result_df = pd.DataFrame(result_list, columns=column_headings)
    # result_df = pd.DataFrame(result_list)

    writer = pd.ExcelWriter(output_excel_file, engine='xlsxwriter')
    result_df.to_excel(writer, sheet_name="source", index=False)
    # re2_gain_df.to_excel(writer, sheet_name="Gain", index=False)
    # re2_loss_df.to_excel(writer, sheet_name="Loss", index=False)
    writer.save()

