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
import json
import csv
from distutils.util import strtobool
from sqlite3 import IntegrityError
from djangoprojects.settings import MEDIA_ROOT



def vus_results():
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



    print('completed')









def process_clilical_files():
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

    print('completed')





def FDA_automated_results():

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

    print('completed')
