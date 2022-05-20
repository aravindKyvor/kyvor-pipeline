import pandas as pd
import numpy as np
import warnings
import os

warnings.filterwarnings("ignore")
import sys, getopt
import os
import time

start_time = time.time()

def svextractor(inputfile_sv, dbdata, path):
    print('AnnotSV sv File curation started')
    head1, tail1 = os.path.split(inputfile_sv)
    tailname_sv = tail1

    sv_filename = tailname_sv.split('.')[0]

    # comvar=sv_filename.split('_sv')[0]
    svvar = sv_filename.split('AnnotSV')[0]
    svvar = svvar.replace('TN_', 'NO_')
    sv_filename_filtshape = svvar + 'Filter_Shape'
    sv_filename_PASS1 = svvar + 'PASS'
    sv_filename_PASS2 = svvar + 'PASS_2455_Gene_Alias'
    sv_filename_woPASS1 = svvar + 'Wout_PASS'

    dirName = path + "/" + svvar + 'Outputs'
    dirName2 = dirName + '/' + svvar + 'Src_curation'
    dirName_gf = dirName + '/' + svvar + 'GeneFusion_matches'
    # dirName3 = dirName_gf + '/' + svvar + 'Pre_Analysis'
    dirName4 = dirName_gf + '/' + svvar + 'Analysis'
    # dirName5 = dirName3 + '/' + svvar + 'PreAnalysis'
    # dirName9 = dirName + '/' + svvar + 'CGC_match'

    try:
        os.umask(0)
        os.makedirs(path, exist_ok=True)
        os.makedirs(dirName, exist_ok=True)
        os.makedirs(dirName2, exist_ok=True)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

    pathname_svpass1 = dirName2 + '/' + sv_filename_PASS1 + '.xlsx'
    pathname_svpass2 = dirName2 + '/' + sv_filename_PASS2 + '.xlsx'
    pathname_svwopass1 = dirName2 + '/' + sv_filename_woPASS1 + '.xlsx'
    pathname_svfiltshp = dirName2 + '/' + sv_filename_filtshape + '.xlsx'

    # dataload
    indata_sv = pd.read_csv(inputfile_sv, sep='\t')
    svcollst = list(indata_sv)
    splitvalcol = svcollst[14]

    # filter valuecounts
    filtshape = indata_sv['FILTER'].value_counts()

    writer = pd.ExcelWriter(pathname_svfiltshp, engine='xlsxwriter')
    filtshape.to_excel(writer, index=True)
    writer.save()

    # format column split
    def colsplit(indata, col, sep):
        new = indata[col].str.split(sep, expand=True)
        for i in range(0, max(new) + 1):
            indata[col + str(i)] = new[i]
            uv = indata[col + str(i)].unique()
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

    indata_sv = colsplit(indata_sv, 'FORMAT', ':')

    indata_sv_pass = indata_sv[indata_sv['FILTER'] == 'PASS']
    indata_sv_wopass = indata_sv[indata_sv['FILTER'] != 'PASS']

    indata_sv_pass = indata_sv_pass[indata_sv_pass['Annotation_mode'] == 'split']
    indata_sv_wopass = indata_sv_wopass[indata_sv_wopass['Annotation_mode'] == 'split']

    # indata_sv_pass = indata_sv_pass[indata_sv_pass['SV_type'] == 'BND']
    # indata_sv_wopass = indata_sv_wopass[indata_sv_wopass['SV_type'] == 'BND']

    dataBND = indata_sv_pass[indata_sv_pass["SV_type"] == 'BND']

    print(dataBND.shape)

    if dataBND.shape[0] > 0:

        # dataBND = dataBND.drop_duplicates(subset="ALT", keep="first")
        dataBND["MantaBNDid"] = dataBND['ID'].str.split(':', expand=True)[1]
        dataBND['Duplicate'] = dataBND['MantaBNDid'].duplicated(keep=False).map({True: 'Yes', False: 'No'})
        dataBND['altChrom'] = dataBND['ALT'].str.extract('chr([^:]*)')
        dataBND["Len"] = ''
        dataBND["Event Type"] = ''
        for row in dataBND.index:
            gene = dataBND['MantaBNDid'][row]
            checkGenes = dataBND[dataBND['MantaBNDid'] == dataBND['MantaBNDid'][row]]
            checkGenesList = checkGenes['Gene_name'].to_list()

            if len(checkGenesList) > 1:
                dataBND["Len"][row] = len(checkGenesList)
                if all(ele == dataBND['Gene_name'][row] for ele in checkGenesList):
                    if str(dataBND["SV_chrom"][row]) == str(dataBND["altChrom"][row]):
                        dataBND["Event Type"][row] = "Intrachromosomal Translocation"
                    else:
                        dataBND["Event Type"][row] = "Interchromosomal Translocation"
                else:
                    if dataBND["Len"][row] == 2:
                        dataBND["Event Type"][row] = "Gene Fusion"
                    else:
                        dataBND["Event Type"][row] = "Overlapping Gene"
            else:
                if str(dataBND["SV_chrom"][row]) == str(dataBND["altChrom"][row]):
                    dataBND["Event Type"][row] = "Intrachromosomal Translocation"
                else:
                    dataBND["Event Type"][row] = "Interchromosomal Translocation"

            print(gene, checkGenesList)

    else:
        dataBND = pd.DataFrame(columns=indata_sv_pass.columns)
        dataBND["MantaBNDid"] = ''
        dataBND['Duplicate'] = ''
        dataBND['altChrom'] = ''
        dataBND["Event Type"] = ''
        dataBND["Len"] = ''

    # dataBND = dataBND.drop(['MantaBNDid', 'altChrom', 'Duplicate'], axis=1)

    delins_list = ["DEL", "INS"]
    dataDELINS = indata_sv_pass[indata_sv_pass["SV_type"].isin(delins_list)]
    dataDELINS["Event Type"] = ''
    dataDELINS["Len"] = ''

    for row in dataDELINS.index:
        if "CIGAR" in dataDELINS['INFO'][row]:
            dataDELINS['Event Type'][row] = "Indels"
        else:
            if dataDELINS['SV_type'][row] == "DEL":
                dataDELINS['Event Type'][row] = "Deletion"
            if dataDELINS['SV_type'][row] == "INS":
                dataDELINS['Event Type'][row] = "Insertion"

    invdup_list = ["INV", "DUP"]
    dataINVDUP = indata_sv_pass[indata_sv_pass["SV_type"].isin(invdup_list)]
    dataINVDUP["Event Type"] = ''
    dataINVDUP["Len"] = ''

    for row in dataINVDUP.index:
        if dataINVDUP['SV_type'][row] == "INV":
            dataINVDUP["Event Type"] = 'Inversion'
        elif dataINVDUP['SV_type'][row] == "DUP":
            dataINVDUP["Event Type"] = 'Tandem Duplication'

    frame = pd.concat([dataBND, dataDELINS, dataINVDUP], axis=0, ignore_index=True)

    geneFusions = frame[frame["Event Type"] == "Gene Fusion"]
    geneFusions["IdSplit"] = geneFusions["ID"].str.split(':').str[-1]

    geneFusionL = geneFusions[geneFusions["IdSplit"] == "0"]

    print(sv_filename)
    brsrColumn = sv_filename.replace("_SV", "")
    print(brsrColumn)

    geneFusionL = geneFusionL.rename(columns={geneFusionL.columns[13]: 'PR:SR'})

    geneFusionR = geneFusions[geneFusions["IdSplit"] == "1"]

    geneFusionLR = pd.merge(geneFusionL, geneFusionR, left_on="MantaBNDid", right_on="MantaBNDid", how="inner")

    # geneFusionHeader =["HGene", "Hbp", "HLocation", "TGene", "Tbp", "TLocation", "PR:SR"]

    # fusionColsToKeep =["Gene name_x", "ALT_x", "location_x", "Gene name_y", "ALT_y", "location_y", "PR:SR"]
    # geneFusionLR = geneFusionLR[fusionColsToKeep]
    # geneFusionLR.columns = geneFusionHeader

    # frameList = pd.DataFrame()

    frameList = frame["Event Type"].value_counts().reset_index()
    frameList.columns = ["Values", "Counts"]
    frameList["Percentage"] = (frameList["Counts"] / frameList["Counts"].sum()) * 100
    frameList = frameList.round(2)

    SVfileName = dirName2+"/"+sv_filename + "_SVeventTypes.xlsx"
    with pd.ExcelWriter(SVfileName) as writer:
        frameList.to_excel(writer, "Counts", index=False)
        frame.to_excel(writer, "Source", index=False)
        geneFusions.to_excel(writer, "Fusions", index=False)
        geneFusionL.to_excel(writer, "FusionL", index=False)
        geneFusionR.to_excel(writer, "FusionR", index=False)
        geneFusionLR.to_excel(writer, "Fusion", index=False)

    def passwritefun(data, pathname):
        fn = pathname.split('/')[-1]
        print('writing ', fn)
        writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
        data.to_excel(writer, index=False)
        writer.save()

    passwritefun(indata_sv_pass, pathname_svpass1)
    passwritefun(indata_sv_wopass, pathname_svwopass1)

    # data_curation
    def indatacuration(indata):
        indata = indata.rename(columns={'Gene name': 'Gene_name'})
        indata = \
            (indata.set_index(indata.columns.drop('Gene_name', 1).tolist())
                 .Gene_name.str.split('/', expand=True)
                 .stack()
                 .reset_index()
                 .rename(columns={0: 'Gene_name'})
                 .loc[:, indata.columns]
                 )
        indata = indata.rename(columns={'Gene_name': 'Gene name'})
        return indata

    indata_sv_pass = indatacuration(indata_sv_pass)

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

    indata_sv_pass_2455 = pd.merge(indata_sv_pass, genedata, left_on=['Gene name'], right_on=['2455_Gene_Alias'],
                                   how='inner')

    def passwritefun(data, pathname):
        fn = pathname.split('/')[-1]
        print('writing ', fn)
        writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
        data.to_excel(writer, index=False)
        writer.save()

    passwritefun(indata_sv_pass_2455, pathname_svpass2)

    end_time = time.time() - start_time
    print("---Source_curation took %s seconds to complete---" % (end_time))

    try:
        os.mkdir(dirName_gf)
        # os.mkdir(dirName3)
        os.mkdir(dirName4)
        # os.mkdir(dirName5)
        print("Directory ", dirName_gf, " Created ")
        # print("Directory ", dirName3, " Created ")
        print("Directory ", dirName4, " Created ")
        # print("Directory " , dirName5 ,  " Created ")
    except FileExistsError:
        print("Directory ", dirName_gf, " already exists")
        # print("Directory ", dirName3, " already exists")
        print("Directory ", dirName4, " already exists")
        # print("Directory " , dirName5 ,  " already exists")

    # CIVIC GENE FUSION
    print('Civic GF match started')

    sv_filename_civcgf1 = sv_filename_PASS1 + '_Database_GF_match'
    pathname_sv_civcgf1 = dirName4 + '/' + sv_filename_civcgf1 + '.xlsx'

    dbdata_fusion = pd.read_excel(io=dbdata, sheet_name='Fusions')
    civiccolst = list(dbdata_fusion)

    indata_sv_civcgf_merge1 = pd.merge(indata_sv_pass_2455, dbdata_fusion, left_on=['Gene name'],
                                       right_on=['PSEUDOVARIANT'], how='inner')

    civcsplitgfus = dbdata_fusion['PSEUDOVARIANT'].str.split('-', expand=True)

    dbdata_fusion['PV1'] = civcsplitgfus[0]
    dbdata_fusion['PV2'] = civcsplitgfus[1]

    indata_sv_civcgf_merge2 = pd.merge(indata_sv_pass_2455, dbdata_fusion, left_on=['Gene name'], right_on=['PV1'],
                                       how='inner')
    indata_sv_civcgf_merge3 = pd.merge(indata_sv_pass_2455, dbdata_fusion, left_on=['Gene name'], right_on=['PV2'],
                                       how='inner')

    indata_sv_final_gf = pd.concat([indata_sv_civcgf_merge1, indata_sv_civcgf_merge2, indata_sv_civcgf_merge3],
                                   sort=False)
    indata_sv_final_gf = indata_sv_final_gf.drop(['PV1', 'PV2'], axis=1)

    indata_sv_final_gf = indata_sv_final_gf.drop_duplicates()

    indata_sv_final_gf = indata_sv_final_gf.drop_duplicates()

    indata_sv_final_gf = indata_sv_final_gf.astype(str)

    orginallst = list(indata_sv_final_gf)
    newlst = []
    for i in range(len(orginallst)):
        if (orginallst[i] != 'SOURCE'):
            newlst.append(orginallst[i])
    indata_sv_final_gf = indata_sv_final_gf.groupby(newlst, sort=False)['SOURCE'].apply(', '.join).reset_index()

    indata_sv_final_gf = indata_sv_final_gf.replace('nan', "")

    writer = pd.ExcelWriter(pathname_sv_civcgf1, engine='xlsxwriter')
    indata_sv_final_gf.to_excel(writer, index=False)  # output1
    writer.save()

    print("---upto GF match took %s seconds to complete---" % (time.time() - start_time))
    return pathname_svpass2
