#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:57:30 2020

@author: arun
"""

import pandas as pd
import argparse
import requests
import time
import os
import shutil

"""
esp_path = "/home/arun/wfh/v4/INDKAA57861_DSP_Outputs/INDKAA57861_2455gene_Src_curation/INDKAA57861_EES_PASS_NS,FS,SGL_2455GeneAlias.xlsx"
sv_path = "/home/arun/wfh/v4/INDKAA57861_SV_TO/INDKAA57861_TO_SVOutputs/INDKAA57861_TO_SVSrc_curation/INDKAA57861_TO_SVPASS_2455_Gene_Alias.xlsx"
cnv_path = "/home/arun/wfh/v4/INDKAA57861_CNV_TO/INDKAA57861_TO_CNV_Outputs/INDKAA57861_TO_CNV_Src_curation/INDKAA57861_TO_CNV_PASS_2455_Gene_Alias.xlsx"


cnv_path = "/home/arun/wfh/v4/INDTNB36103_TO_CNV/INDTNB36103_TO_CNV_Outputs/INDTNB36103_TO_CNV_Src_curation/INDTNB36103_TO_CNV_PASS_2455_Gene_Alias.xlsx"
sv_path = "/home/arun/wfh/v4/INDTNB36103_TO_SV/INDTNB36103_TO_SVOutputs/INDTNB36103_TO_SVSrc_curation/INDTNB36103_TO_SVPASS_2455_Gene_Alias.xlsx"
esp_path = "/home/arun/wfh/v4/INDTNB36103_DSP_Outputs/INDTNB36103_2455gene_Src_curation/INDTNB36103_EES_PASS_NS,FS,SGL_2455GeneAlias.xlsx"

cancer_type = "Metastatic Renal Cell Carcinoma,Solid Tumor,Metastatic cancer"
patient_id = "INDKAA57861_CT"
apppath = "/home/arun/wfh/v4/"

"""


def clinicalLauncher(sv_path,cnv_path,esp_path,cancer_type,patient_id,apppath):
    start_time = time.time()

    print("Cancer Type:", cancer_type)
    time.sleep(0.2)
    cancer_list = cancer_type.split(",")

    sv_data = pd.read_excel(sv_path, sheet_name='Sheet1')
    cnv_data = pd.read_excel(cnv_path, sheet_name='Sheet1')
    esp_data = pd.read_excel(esp_path, sheet_name='Sheet1')

    print('SV Data:', sv_data.shape)
    print('CNV Data:', cnv_data.shape)
    print('ESP Data:', esp_data.shape)
    res_columns = ['Gene', 'GeneAlias', 'CallType']

    output_filename = apppath+"/"+patient_id + "CT_Results.xlsx"

    # Curate ESP Data
    print("Curating EES_PASS_NS,FS,SGL File")
    esp_data['ExAC_ALL'] = esp_data['ExAC_ALL'].replace('.', 9999).astype(float)
    esp_001 = esp_data[esp_data['ExAC_ALL'] <= 0.01]
    esp_data['ExAC_ALL'] = esp_data['ExAC_ALL'].replace(9999, '.')
    esp_dot = esp_data[esp_data['ExAC_ALL'] == '.']
    esp_filtered = esp_001.append(esp_dot)
    # Filtered ESP Result
    esp_res = esp_filtered[['Gene.refGene', 'Gene_Alias2', 'ExonicFunc.refGene']]
    esp_res.columns = res_columns
    print('done')
    time.sleep(0.2)
    # Curate CNV Data
    print("Curating CNV File")
    cnv_data['CN'] = cnv_data['CN'].astype(int)
    cnv_filtered = cnv_data[cnv_data['CN'] >= 4].append(cnv_data[cnv_data['SV_type'] == '<DEL>'])
    cnv_res = cnv_filtered[['Gene_name', 'Gene_Alias2', 'SV_type']]
    cnv_res.columns = res_columns
    print('done')
    time.sleep(0.2)
    # Curate SV Data
    print('Curating SV File')
    sv_filtered = sv_data[sv_data['Annotation_mode'] == 'split']
    sv_res = sv_filtered[['Gene name', 'Gene_Alias2', 'SV_type']]
    sv_res.columns = res_columns
    print('done')
    time.sleep(0.2)
    print('Merging datasets')
    res_dfs = [esp_res, cnv_res, sv_res]
    #res_dfs = [esp_res, cnv_res]
    res = pd.concat(res_dfs, ignore_index=True)
    print('done')
    time.sleep(0.2)
    # remove duplicates
    print("Removing Duplicates")
    res.drop_duplicates(keep='first', inplace=True)
    # merge duplicated rows
    res = (res.drop_duplicates(['Gene', 'CallType'])
           .groupby('Gene')
           .agg(GeneAlias=('GeneAlias', lambda x: x.str.cat(sep=',')),
                CallType=('CallType', lambda x: x.str.cat(sep=','))
                )
           .reset_index()
           )
    print('Done')
    time.sleep(0.2)
    res_list = []
    # Create folder to save csv resp based on patient id
    try:
        os.umask(0)
        os.makedirs(apppath+"/studies/", exist_ok=True)
    except Exception as e:
        print(e)
        pass
    cols = ["Gene", "Gene Alias", "Call Type", "Rank", "NCT Number", "Title", "Status", "Study Results", "Conditions",
            "Interventions", "Phases", "Study Type", "Last Update Posted", "URL", "Cancer Type"]
    print("Initiating Clinical Trials Match")
    print("Gene Count: ",res.shape[0])
    for row in res.index:
        res['GeneAlias'][row] = ','.join(set(res['GeneAlias'][row].split(',')))
        for cancer in cancer_list:
            gene_row = []
            current_gene = []
            gene = str(res['Gene'][row])
            gene_alias = str(res['GeneAlias'][row])
            call_type = str(res['CallType'][row])
            url = 'https://clinicaltrials.gov/ct2/results/download_fields?down_count=10000&down_flds=shown&down_fmt=csv&'
            url = url + 'term=' + gene
            url = url + '&recrs=abde&cond=' + cancer
            url = url + '&flds=a&flds=b&flds=i&flds=f&flds=k&flds=r'

            returnFile = requests.get(url)

            if returnFile.status_code == 200:

                geneFileName = apppath+'/studies/'+ gene + '.csv'
                open(geneFileName, 'wb').write(returnFile.content)
                current_gene = pd.read_csv(geneFileName)
                current_gene.insert(0, 'gene', gene)
                df = pd.DataFrame(current_gene)
                for i in df.itertuples():
                    gene_row = []
                    gene_row.append(i[1])
                    gene_row.append(gene_alias)
                    gene_row.append(call_type)
                    gene_row.append(i[2])
                    gene_row.append(i[3])
                    gene_row.append(i[4])
                    gene_row.append(i[5])
                    gene_row.append(i[6])
                    gene_row.append(i[7])
                    gene_row.append(i[8])
                    gene_row.append(i[9])
                    gene_row.append(i[10])
                    gene_row.append(i[11])
                    gene_row.append(i[12])
                    gene_row.append(cancer)

                    print(gene_row)
                    res_list.append(gene_row)
    print('Done')
    time.sleep(0.2)

    res_list = pd.DataFrame(res_list)
    print(res_list.shape)
    print(res_list)
    res_list.columns = cols

    print('Writing Results')
    with pd.ExcelWriter(output_filename) as writer:
        res.to_excel(writer, patient_id + "source", index=False)
        for cancer in cancer_list:
            sheet_name = cancer[0:20].replace(" ", "")
            lis_cancer = res_list[res_list['Cancer Type'] == cancer]
            lis_cancer.to_excel(writer, sheet_name=sheet_name, index=False)
    print("Done")

    try:
        shutil.make_archive(apppath+"/studies", 'zip', apppath, 'studies')
    except Exception as e:
        print("Not Zipped")
        pass


    print("---Process took %s seconds to complete---" % (time.time() - start_time))

