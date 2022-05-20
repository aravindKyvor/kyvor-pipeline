import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")
import sys, getopt
import os
import time

start_time = time.time()

exonFile = "/home/aravind/Desktop/CurationV4/ncbiRefSeq.txt"
cnaFile = "/home/aravind/Desktop/CurationV4/BRCA_CNA_Genes.txt"


def cnvextractor(inputfile_cnv, dbdata, cnaFile, path):
    print('AnnotSV CNV File curation started')
    head1, tail1 = os.path.split(inputfile_cnv)
    tailname_sv = tail1
    cnv_filename = tailname_sv.split('.')[0]

    # comvar=cnv_filename.split('_CNV')[0]
    cnvvar = cnv_filename.split('AnnotSV')[0]
    cnvvar = cnvvar.replace('TN_', 'NO_')
    cnv_filename_filtshape = cnvvar + '_Filter_Shape'
    cnv_filename_PASS1 = cnvvar + '_PASS'
    cnv_filename_PASS2 = cnvvar + '_PASS_2455_Gene_Alias'
    cnv_filename_woPASS1 = cnvvar + '_Wout_PASS'
    rawFile = cnvvar + '_source'
    print(cnvvar)
    dirName = path + "/" + cnvvar + '_Outputs'
    print(dirName)
    dirName2 = dirName + '/' + cnvvar + '_Src_curation'
    dirName3 = dirName + '/' + cnvvar + '_Expression_matches'
    dirName4 = dirName3 + '/' + cnvvar + '_Analysis'
    dirName5 = dirName3 + '/' + cnvvar + '_PreAnalysis'
    dirName9 = dirName + '/' + cnvvar + '_CGC_match'
    reportFolder = dirName + '/' + cnvvar + '_Report'

    try:
        os.umask(0)
        os.makedirs(path, exist_ok=True)
        print(dirName)
        os.makedirs(dirName, exist_ok=True)
        os.makedirs(dirName2, exist_ok=True)
        os.makedirs(reportFolder, exist_ok=True)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

    pathname_cnvpass1 = dirName2 + '/' + cnv_filename_PASS1 + '.xlsx'
    pathname_cnvpass2 = dirName2 + '/' + cnv_filename_PASS2 + '.xlsx'
    pathname_cnvwopass1 = dirName2 + '/' + cnv_filename_woPASS1 + '.xlsx'
    pathname_cnvfiltshp = dirName2 + '/' + cnv_filename_filtshape + '.xlsx'
    pathname_cna = dirName3 + '/' + cnvvar + "_CNA-Matched.xlsx"
    pathname_cnaCurated = dirName2 + '/' + cnvvar + "_CNA-Curated.csv"
    reportFileName = reportFolder + '/' + cnvvar + "_Report.xlsx"

    # dataload
    indata_cnv = pd.read_csv(inputfile_cnv, sep='\t')
    cnvcollst = list(indata_cnv)
    splitvalcol = cnvcollst[14]

    # filter valuecounts
    filtshape = indata_cnv['FILTER'].value_counts()

    writer = pd.ExcelWriter(pathname_cnvfiltshp, engine='xlsxwriter')
    filtshape.to_excel(writer, index=True)
    writer.save()

    # format column split
    def colsplit(indata, col, sep):
        new = indata[col].str.split(sep, expand=True)
        for i in range(0, max(new) + 1):
            indata[col + str(i)] = new[i]
            uv = indata[col + str(i)].unique()
            print(uv)
            uvname = uv[0]
            # indata = indata.drop(columns=col + str(i))
            new2 = indata[splitvalcol].str.split(':', expand=True)

            if (len(uv) == 1):
                indata[uvname] = new2[i]
                indata = indata.drop(columns=col + str(i))
            elif (None not in uv and len(uv) == 2):
                uval = '/'.join(uv)
                indata[uval] = new2[i]
                indata1 = indata[indata[col + str(i)] == uv[0]]
                indata1[uv[0]] = indata1[uval]
                indata2 = indata[indata[col + str(i)] == uv[1]]
                indata2[uv[1]] = indata2[uval]
                indata = pd.concat([indata1, indata2], sort=False)
                indata = indata.drop(columns=col + str(i))
                indata = indata.drop(columns=uval)
            elif (None in uv):
                # elif(uv.__contains__(None)):
                indata = indata.drop(columns=col + str(i))
                newlst = []
                for i in range(len(uv)):
                    if (uv[i] != None):
                        newlst.append(uv[i])
                uvnew = newlst[0]
                indata[uvnew] = new2[i]
            else:
                print()
                indata = indata
        return indata

    indata_cnv = colsplit(indata_cnv, 'FORMAT', ':')

    rawFileName = dirName2 + "/" + rawFile + '.tsv'
    indata_cnv.to_csv(rawFileName, index=False, sep="\t")
    indata_cnv_pass = indata_cnv[indata_cnv['FILTER'] == 'PASS']
    indata_cnv_wopass = indata_cnv[indata_cnv['FILTER'] != 'PASS']

    indata_cnv_pass = indata_cnv_pass[indata_cnv_pass['Annotation_mode'] == 'split']
    indata_cnv_wopass = indata_cnv_wopass[indata_cnv_wopass['Annotation_mode'] == 'split']

    exonData = pd.read_csv(exonFile, sep="\t")

    exonData["NM"] = exonData["Transcript ID"].str.split('.', expand=True)[0]

    indata_cnv_pass = pd.merge(indata_cnv_pass, exonData, left_on=['Gene_name', 'Tx'], right_on=['Gene Name', 'NM'],
                               how='inner')
    indata_cnv_wopass = pd.merge(indata_cnv_wopass, exonData, left_on=['Gene_name', 'Tx'], right_on=['Gene Name', 'NM'],
                                 how='inner')

    indata_cnv_pass.to_csv(path + "/exonPass.csv", index=False)
    indata_cnv_wopass.to_csv(path + "/exonWoPass.csv", index=False)

    def passwritefun(data, pathname):
        fn = pathname.split('/')[-1]
        print('writing ', fn)
        writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
        data.to_excel(writer, index=False)
        writer.save()

    passwritefun(indata_cnv_pass, pathname_cnvpass1)
    passwritefun(indata_cnv_wopass, pathname_cnvwopass1)

    # data_curation
    def indatacuration(indata):
        indata = indata.rename(columns={'Gene_name': 'Gene_name'})
        indata = \
            (indata.set_index(indata.columns.drop('Gene_name', 1).tolist())
                 .Gene_name.str.split('/', expand=True)
                 .stack()
                 .reset_index()
                 .rename(columns={0: 'Gene_name'})
                 .loc[:, indata.columns]
                 )
        indata = indata.rename(columns={'Gene_name': 'Gene_name'})
        return indata

    # indata_cnv_pass.to_csv("Check Pass.tsv", index=False, sep="\t")
    indata_cnv_pass = indatacuration(indata_cnv_pass)

    # genedata = pd.read_csv('/home/vidhya/Downloads/ct_final1.csv')
    genedata = pd.read_excel(dbdata, sheet_name='2455_GeneData')
    genedata['Gene'] = genedata['Gene'].astype(str)
    genedata['2455_Gene_Alias'] = genedata['2455_Gene_Alias'].astype(str)
    genedata_ga = genedata[genedata['2455_Gene_Alias'].notnull()]

    genedata_notga = genedata.merge(genedata_ga, indicator=True, how='left').loc[lambda x: x['_merge'] != 'both']
    genedata_notga = genedata_notga.drop(['_merge'], axis=1)

    genedata_ga['2455_Gene_Alias'] = genedata_ga['Gene'] + ', ' + genedata_ga['2455_Gene_Alias']
    genedata_notga['2455_Gene_Alias'] = genedata_notga['Gene']

    genedata = pd.concat([genedata_ga, genedata_notga], sort=False)
    genedata['Gene_Alias2'] = genedata['2455_Gene_Alias']

    genedata = genedata.rename(columns={'2455_Gene_Alias': 'Gene_Alias'})
    genedata = \
        (genedata.set_index(genedata.columns.drop('Gene_Alias', 1).tolist())
             .Gene_Alias.str.split(', ', expand=True)
             .stack()
             .reset_index()
             .rename(columns={0: 'Gene_Alias'})
             .loc[:, genedata.columns]
             )
    genedata = genedata.rename(columns={'Gene_Alias': '2455_Gene_Alias'})

    indata_cnv_pass_2455 = pd.merge(indata_cnv_pass, genedata, left_on=['Gene_name'], right_on=['2455_Gene_Alias'],
                                    how='inner')

    def passwritefun(data, pathname):
        fn = pathname.split('/')[-1]
        print('writing ', fn)
        writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
        data.to_excel(writer, index=False)
        writer.save()

    passwritefun(indata_cnv_pass_2455, pathname_cnvpass2)

    end_time = time.time() - start_time
    print("---Source_curation took %s seconds to complete---" % (end_time))

    # Expression match

    try:
        os.mkdir(dirName3)
        os.mkdir(dirName4)

        print("Directory ", dirName3, " Created ")
        print("Directory ", dirName4, " Created ")

    except FileExistsError:
        print("Directory ", dirName3, " already exists")
        print("Directory ", dirName4, " already exists")

    # CIVIC_EXP_MATCH
    print('Database expression match started')
    cnv_filename_civic1 = cnv_filename_PASS1 + '_Database_Exp_match'
    pathname_cnv_civic1 = dirName5 + '/' + cnv_filename_PASS1 + '_Exp_match_PreAnalysis' + '.xlsx'
    pathname_cnv_civic2 = dirName4 + '/' + cnv_filename_PASS1 + '_Exp_match.xlsx'
    pathname_cna_civic2 = dirName4 + '/' + cnv_filename_PASS1 + 'cna_matched.xlsx'

    dbdata_exp = pd.read_excel(io=dbdata, sheet_name='Expression')
    civccolst = list(dbdata_exp)

    indata_cnv_final_g = pd.merge(indata_cnv_pass, dbdata_exp, left_on=['Gene_name'], right_on=['GENE'], how='inner')
    indata_cnv_final_g = indata_cnv_final_g.drop_duplicates()

    # gene&exp
    # cvcfiltdup=['Expression','OVEREXPRESSION','AMPLIFICATION','ITD','ALTERNATIVE TRANSCRIPT (ATI)','COPY NUMBER VARIATION','INTERNAL DUPLICATION',
    #     "5' TANDEM REPEAT",'V600E/K AMPLIFICATION','Alu insertion','Duplication','EXON 14 MUTATION + AMPLIFICATION']
    indata_cnv_civic_exp = indata_cnv_final_g[indata_cnv_final_g['PSEUDOVARIANT'] == 'Expression']
    indata_cnv_civic_altexp = indata_cnv_civic_exp[indata_cnv_civic_exp['ALT'] == '<DUP>']

    # cvcfiltdel=['UNDEREXPRESSION','LOSS-OF-FUNCTION','DELETION POLYMORPHISM','Deletion','DELETION','LOSS','T17 DELETION','LOH']
    indata_cnv_civic_del = indata_cnv_final_g[indata_cnv_final_g['PSEUDOVARIANT'] == 'Deletion']
    indata_cnv_civic_altdel = indata_cnv_civic_del[indata_cnv_civic_del['ALT'] == '<DEL>']

    indata_cnv_final_galt = pd.concat([indata_cnv_civic_altexp, indata_cnv_civic_altdel], sort=False)
    indata_cnv_final_galt = indata_cnv_final_galt.drop_duplicates()

    indata_cnv_final_g = indata_cnv_final_g.drop_duplicates()
    indata_cnv_final_galt = indata_cnv_final_galt.drop_duplicates()

    indata_cnv_final_g = indata_cnv_final_g.astype(str)
    indata_cnv_final_galt = indata_cnv_final_galt.astype(str)

    orginallst = list(indata_cnv_final_g)
    newlst = []
    for i in range(len(orginallst)):
        if (orginallst[i] != 'SOURCE'):
            newlst.append(orginallst[i])
    indata_cnv_final_g = indata_cnv_final_g.groupby(newlst, sort=False)['SOURCE'].apply(', '.join).reset_index()

    orginallst = list(indata_cnv_final_galt)
    newlst = []
    for i in range(len(orginallst)):
        if (orginallst[i] != 'SOURCE'):
            newlst.append(orginallst[i])
    indata_cnv_final_galt = indata_cnv_final_galt.groupby(newlst, sort=False)['SOURCE'].apply(', '.join).reset_index()

    print(indata_cnv_final_g.shape)
    print(indata_cnv_final_galt.shape)

    indata_cnv_final_g = indata_cnv_final_g.replace('nan', "")
    indata_cnv_final_galt = indata_cnv_final_galt.replace('nan', "")

    def curateTypes(data):

        data['location1'] = data['Location'].str.split('-', expand=True)[0]
        data['location2'] = data['Location'].str.split('-', expand=True)[1]
        data['SV event'] = ''
        data['exonNum'] = 'exon' + data['exon']
        for row in data.index:
            if data['ALT'][row] == '<DUP>':
                if ((data['location1'][row] == 'txStart') & (data['location2'][row] == 'txEnd')):
                    data['SV event'][row] = 'Full Duplication'
                elif ((data['location1'][row] == 'intron1') or (data['location1'][row] == 'txStart')):
                    if data['location2'][row] == data['exonNum'][row]:
                        data['SV event'][row] = 'Full Duplication'
                    else:
                        data['SV event'][row] = 'Partial Duplication'
                else:
                    data['SV event'][row] = 'Partial Duplication'

            elif data['ALT'][row] == '<DEL>':
                if ((data['location1'][row] == 'txStart') & (data['location2'][row] == 'txEnd')):
                    data['SV event'][row] = 'Full Deletion'
                elif ((data['location1'][row] == 'intron1') or (data['location1'][row] == 'txStart')):
                    if data['location2'][row] == data['exonNum'][row]:
                        data['SV event'][row] = 'Full Deletion'
                    else:
                        data['SV event'][row] = 'Partial Deletion'
                else:
                    data['SV event'][row] = 'Partial Deletion'
        data = data.drop(['location1', 'location2', 'exonNum'], axis=1)
        return data

    indata_cnv_final_g = curateTypes(indata_cnv_final_g)
    if indata_cnv_final_galt.shape[0] > 0:
        indata_cnv_final_galt = curateTypes(indata_cnv_final_galt)

    writer = pd.ExcelWriter(pathname_cnv_civic2, engine='xlsxwriter')
    indata_cnv_final_g.to_excel(writer, index=False, sheet_name='Exp_Gene_match')  # output1
    indata_cnv_final_galt.to_excel(writer, index=False, sheet_name='Exp_Gene_ALT_match')  # output1
    writer.save()

    if indata_cnv_final_galt.shape[0] > 0:

        ##Report Format
        reportCNV = pd.DataFrame()
        # fdaMatch[['Gene.refGene', 'AAChange']].apply(lambda x: ' '.join(x), axis=1)
        pattern = '|'.join(['<', '>'])
        indata_cnv_final_galt["SVtoReport"] = indata_cnv_final_galt['SV_type'].str.replace(pattern, '')
        reportCNV["Biomarker"] = indata_cnv_final_galt[['Gene_name', 'SVtoReport']].apply(lambda x: ' '.join(x), axis=1)
        reportCNV["Therapy"] = indata_cnv_final_galt["THERAPY"]
        reportCNV["Variant status in patient"] = ''
        reportCNV["CN"] = indata_cnv_final_galt["CN"]
        reportCNV["Cancer Type"] = indata_cnv_final_galt["CANCER TYPE"]
        reportCNV["Evidence Statement"] = indata_cnv_final_galt["EVIDENCE STATEMENT"]
        reportCNV["Reference"] = indata_cnv_final_galt["REFERENCES"]
        indata_cnv_final_galt = indata_cnv_final_galt.drop("SVtoReport", axis=1, errors='ignore')

        reportCNV = reportCNV.drop_duplicates()

        reportCNV.to_excel(reportFileName, sheet_name="Report", index=False)

        cnadata = pd.read_csv(cnaFile, sep="\t")
        print("CNA COlumns", cnadata.columns)


        for colu in cnadata.columns:
            print(colu)

        def cnadatacurate(data):
            data['SV Type'] = ''
            for row in data.index:
                if data['CNA'][row] == 'AMP':
                    data['SV Type'][row] = '<DUP>'
                elif data['CNA'][row] == 'HOMDEL':
                    data['SV Type'][row] = '<DEL>'
                else:
                    data['SV Type'][row] = ''
            return data

        cnadata = cnadatacurate(cnadata)
        cnadata.to_csv(pathname_cnaCurated, index=False)
        # cnadata['SV Type'] = cnadata.loc[(cnadata['Cytoband'] == 'AMP', 'SV Type')] = '<Dup>'
        # cnadata['SV Type'] = cnadata.loc[(cnadata['Cytoband'] == 'HOMDEL', 'SV Type')] = '<DEL>'

        indata_cnv_final_g_cna = pd.merge(indata_cnv_final_g, cnadata, left_on=['Gene_name', 'SV_type'],
                                          right_on=['Gene', 'SV Type'], how='inner')
        indata_cnv_final_galt_cna = pd.merge(indata_cnv_final_galt, cnadata, left_on=['Gene_name', 'SV_type'],
                                             right_on=['Gene', 'SV Type'], how='inner')

        writer = pd.ExcelWriter(pathname_cna, engine='xlsxwriter')
        indata_cnv_final_g_cna.to_excel(writer, index=False, sheet_name='Exp_Gene_match')  # output1
        indata_cnv_final_galt_cna.to_excel(writer, index=False, sheet_name='Exp_Gene_ALT_match')  # output1
        writer.save()
    else:
        reportCNV = pd.DataFrame()
        writer = pd.ExcelWriter(reportFileName, engine="xlsxwriter")
        reportCNV.to_excel(writer, sheet_name="Report", index=False)
        worksheet = writer.sheets['Report']
        worksheet.write(0, 0, "No data available to write in report")
        writer.save()

    print('EXp match completed')
    print("--- EXp match took %s seconds to complete---" % (time.time() - start_time))
    return pathname_cnvpass2

    # report format
