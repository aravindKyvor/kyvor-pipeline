import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")
import sys, getopt
import os
import time

start_time = time.time()


def curation(inputfile, cosdata, cgcdata, tnpatientfile,appname,dbdata):
    os.umask(0)
    if (inputfile != '' and tnpatientfile != ''):
        print(
            'You have mentioned both TN and TO patient files.Please mention either TO_Patient_file or TN_Patient_File')
        sys.exit()
    elif (inputfile == '' and tnpatientfile == ''):
        print('Please mention either TO_Patient_file or TN_Patient_File ')
        sys.exit()
    elif (inputfile == ''):
        print('TO Patient file not mentioned')
    else:
        print('TO File Sorce_curation started')
        head, tail = os.path.split(inputfile)
        tailname = tail
        filename = tailname.split('.')[0]

        var1 = filename.split('_')[0]
        srcvar2 = filename.split('multianno')[0]
        finalname_master = srcvar2 + 'Master_File'
        finalname_fun = srcvar2 + 'PASS_Other_Fun_RefGene'
        finalname_EESP_notmmatched = srcvar2 + 'EES_PASS_Notmatched_with2455GA'
        finalname_EESP1 = srcvar2 + 'EES_PASS'
        finalname_SpP2 = srcvar2 + 'Sp_PASS'
        finalname_EESP_Syn3 = srcvar2 + 'EES_PASS_Syn'
        finalname_EESP_NSFSSGL4 = srcvar2 + 'EES_PASS_NS,FS,SGL'
        finalname_EESP_NonSyn5 = srcvar2 + 'EES_PASS_NonSyn'
        finalname_EESP_FS6 = srcvar2 + 'EES_PASS_FS'
        finalname_EESP_SGL7 = srcvar2 + 'EES_PASS_SGL'
        finalname_EESP1_tmb = srcvar2 + 'TMB_Calculation'
        shape_cur = srcvar2 + 'Curation_Shapes'

        dirName = appname+"/"+srcvar2 + 'DSP_Outputs'
        dirName_PreAnalysis = dirName + '/' + srcvar2 + 'PreAnalysis'
        dirName_Analysis = dirName + '/' + srcvar2 + 'Analysis'
        dirName_Report = dirName + '/' + srcvar2 + 'Report'
        # dirName_Civic_Report = dirName_Report + '/' + srcvar2 + 'Civic_Report'
        dirName_Cosmic_Forlist_Report = dirName_Report + '/' + srcvar2 + '_Forlist_Report'
        dirName_cgcReport = dirName_Report + '/' + srcvar2 + 'CGC_Report'
        dirName_fdaReport = dirName_Report + '/' + srcvar2 + 'FDA_Report'
        dirName2 = dirName + '/' + srcvar2 + 'Src_curation'
        dirName_ARC = dirName + '/' + srcvar2 + 'Archive'
        dirName2455gene = dirName + '/' + srcvar2 + '2455gene_Src_curation'
        dirName3 = dirName_Analysis + '/' + srcvar2 + 'Civic_match'
        dirName4 = dirName_ARC + '/' + srcvar2 + 'Cosmic_match'
        dirName_newcosmic = dirName_PreAnalysis + '/' + srcvar2 + 'Cosmic_match_Status'
        # dirName5 = dirName_PreAnalysis + '/' + srcvar2 + 'Cosmic_DR'
        dirName6 = dirName_Analysis + '/' + srcvar2 + 'CGC_match'

        dirName7 = dirName4 + '/' + srcvar2 + 'Cos_Syn'
        dirName_newcos7 = dirName_newcosmic + '/' + srcvar2 + 'Cos_Syn'
        dirName8 = dirName4 + '/' + srcvar2 + 'Cos_NS,FS,SGL'
        dirName_newcos8 = dirName_newcosmic + '/' + srcvar2 + 'Cos_NS,FS,SGL'
        dirName11 = dirName4 + '/' + srcvar2 + 'Cos_Sp_PASS'
        dirName_newcos11 = dirName_newcosmic + '/' + srcvar2 + 'Cos_Sp_PASS'

        # dirName13 = dirName5 + '/' + srcvar2 + 'Cos_DR_Syn'
        # dirName14 = dirName5 + '/' + srcvar2 + 'Cos_DR_NS,FS,SGL'
        # dirName17 = dirName5 + '/' + srcvar2 + 'Cos_DR_Sp_PASS'
        dirName19 = dirName_Analysis + '/' + srcvar2 + 'Cosmic_DR_For_List'
        dirName20 = dirName_Analysis + '/' + srcvar2 + 'CosRes_MATCH'
        dirName21 = dirName_Analysis + '/' + srcvar2 + 'Database_MATCH'
        dirName22 = dirName_Analysis + '/' + srcvar2 + 'OtherDatabase_MATCH'

        try:
            os.makedirs(dirName, mode=0o777)
            os.makedirs(dirName2, mode=0o777)
            os.makedirs(dirName_ARC, mode=0o777)
            os.makedirs(dirName2455gene, mode=0o777)
            os.makedirs(dirName_Analysis, mode=0o777)
            os.makedirs(dirName_PreAnalysis, mode=0o777)
            os.makedirs(dirName_Report, mode=0o777)

            print("Directory ", dirName, " Created ")
            print("Directory ", dirName2455gene, " Created ")
        except FileExistsError:
            print("Directory ", dirName, " already exists")
            print("Directory ", dirName2455gene, " already exists")

        pathname_master = dirName_ARC + '/' + finalname_master + '.tsv'
        pathname_otherfun = dirName2 + '/' + finalname_fun + '.xlsx'
        # pathname_otherfun2 = dirName_ARC + '/' + finalname_fun + '.xlsx'
        pathname_otherfun_shape = dirName_ARC + '/' + finalname_fun + '_shapes1.xlsx'
        pathname_eesp_notmatch = dirName_ARC + '/' + finalname_EESP_notmmatched + '.xlsx'
        pathname1 = dirName2 + '/' + finalname_EESP1 + '.xlsx'
        pathname2 = dirName2 + '/' + finalname_SpP2 + '.xlsx'
        pathname3 = dirName2 + '/' + finalname_EESP_Syn3 + '.xlsx'
        pathname4 = dirName2 + '/' + finalname_EESP_NSFSSGL4 + '.xlsx'
        pathname5 = dirName2 + '/' + finalname_EESP_NonSyn5 + '.xlsx'
        pathname6 = dirName2 + '/' + finalname_EESP_FS6 + '.xlsx'
        pathname7 = dirName2 + '/' + finalname_EESP_SGL7 + '.xlsx'
        path_shape_cur = dirName2 + '/' + shape_cur + '.xlsx'
        path_tmb = dirName2 + '/' + finalname_EESP1_tmb + '.xlsx'

        ptdata = pd.read_csv(inputfile, sep="\t", header=[0])
        ptdata1 = pd.read_csv(inputfile, sep="\t", header=None, skiprows=1)

        ptcollist = list(ptdata)
        ptcollst1 = list(ptdata1)
        
        print(len(ptcollist), len(ptcollst1))
        
        ptfinlst = []
        x = 1
        for i in range(0, len(ptcollst1)):
            if (i < len(ptcollist)):
                ptfinlst.append(ptcollist[i])
            else:
                ptfinlst.append('Otherinfo' + str(x))
                x += 1
        ptdata1.columns = ptfinlst
        print('Patient data shape: ', ptdata1.shape)
        print(ptfinlst)
        ptdata1.to_csv(pathname_master, sep='\t', index=False)

        ptdata1 = ptdata1.rename(columns={'DP': 'DP1'})
        ptdata1 = ptdata1.rename(columns={'AF': 'AF1'})

        passcolumn1 = list(ptdata1)[-4]
        dpmqtlodfircolumn = list(ptdata1)[-3]
        gtadafheadcolumn = list(ptdata1)[-2]
        gtadafvalcolumn = list(ptdata1)[-1]

        # filtvalues = ['exonic', 'exonic;splicing']
        # Otherfunction = ptdata1[~ptdata1['Func.refGene'].isin(filtvalues)]
        # writer = pd.ExcelWriter(pathname_otherfun2, engine='xlsxwriter')
        # Otherfunction.to_excel(writer, index=True)
        # writer.save()

        PASSdata = ptdata1[ptdata1[passcolumn1] == 'PASS']
        print('PASS data shape: ', PASSdata.shape)

        # col split dt tlod fir
        def colsplito8(indata, col, sep):
            new = indata[col].str.split(sep, expand=True)
            for i in range(0, max(new) + 1):
                indata[col + str(i)] = new[i]
                new2 = indata[col + str(i)].str.split('=', expand=True)
                indata = indata.drop(columns=col + str(i))
                indata[col + 'uv' + str(i)] = new2[0]
                uv = indata[col + 'uv' + str(i)].unique()
                uv2 = uv[0]
                # indata = indata.drop(columns=col + 'uv')
                if (len(uv) == 1):
                    indata[uv2] = new2[1]
                    indata = indata.drop(columns=col + 'uv' + str(i))
                elif (None not in uv and len(uv) == 2):
                    uval = '/'.join(uv)
                    indata[uval] = new2[1]
                    indata1 = indata[indata[col + 'uv' + str(i)] == uv[0]]
                    indata1[uv[0]] = indata1[uval]
                    indata2 = indata[indata[col + 'uv' + str(i)] == uv[1]]
                    indata2[uv[1]] = indata2[uval]
                    indata = pd.concat([indata1, indata2], sort=False)
                    indata = indata.drop(columns=col + 'uv' + str(i))
                    indata = indata.drop(columns=uval)
                elif (None in uv):
                    # elif(uv.__contains__(None)):
                    indata = indata.drop(columns=col + 'uv' + str(i))
                    newlst = []
                    for i in range(len(uv)):
                        if (uv[i] != None):
                            newlst.append(uv[i])
                    uvnew = newlst[0]
                    indata[uvnew + str(i)] = new2[1]
                else:
                    print()
                    indata = indata
            return indata

        ptdata1 = colsplito8(PASSdata, dpmqtlodfircolumn, ';')
        ptdata1 = ptdata1.rename(columns={'DP': 'DP_Total'})

        # gtadafclsplit
        def colsplitsub1(indata, col, sep):
            new = indata[col].str.split(sep, expand=True)
            for i in range(0, 7):
                indata[col + str(i)] = new[i]
                uv = indata[col + str(i)].unique()
                uvname = uv[0]
                indata = indata.drop(columns=col + str(i))
                new2 = indata[gtadafvalcolumn].str.split(':', expand=True)
                indata[uvname] = new2[i]
            return indata

        ptdata1 = colsplitsub1(ptdata1, gtadafheadcolumn, ':')

        ptdata1 = ptdata1.rename(columns={'DP': 'DP_Sample'})
        ptdata1 = ptdata1.rename(columns={'AF': 'AF_VAF'})

        data1 = ptdata1[ptdata1['GT'].str.contains('/')]
        data2 = ptdata1[~ptdata1['GT'].str.contains('/')]

        # sbmbsplit
        def colsplitsbmb(indata):
            indata['id2'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-2])
            indata['id1'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-1])
            uniqmb = indata['id1'].unique()
            uniqsb = indata['id2'].unique()
            if (len(uniqmb) == 1 and len(uniqsb) == 1):
                indata[uniqsb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
                indata[uniqmb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
            elif (len(uniqmb) == 1):
                indata[uniqmb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
            elif (len(uniqsb) == 1):
                indata[uniqsb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
            elif (None not in uniqmb and len(uniqmb) >= 2):
                uval = '/'.join(uniqmb)
                indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
            elif (None not in uniqsb and len(uniqsb) >= 2):
                uval = '/'.join(uniqsb)
                indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
            else:
                print()
                indata = indata
            indata = indata.drop(columns=['id1', 'id2'])
            return indata

        data1 = colsplitsbmb(data1)

        # sbmbpssplit
        def colsplitps(indata):
            if ((indata.shape)[0] != 0):
                indata['id1'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-1])
                indata['id2'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-2])
                indata['id3'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-3])
                uniqps = indata['id1'].unique()
                uniqmb = indata['id2'].unique()
                uniqsb = indata['id3'].unique()
                if (len(uniqps) == 1 and len(uniqmb) == 1 and len(uniqsb) == 1):
                    indata[uniqps[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
                    indata[uniqsb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-3])
                    indata[uniqmb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
                elif (len(uniqps) == 1):
                    indata[uniqps[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
                elif (len(uniqmb) == 1):
                    indata[uniqmb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
                elif (len(uniqsb) == 1):
                    indata[uniqsb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-3])
                elif (None not in uniqps and len(uniqps) >= 2):
                    uval = '/'.join(uniqps)
                    indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
                elif (None not in uniqmb and len(uniqmb) >= 2):
                    uval = '/'.join(uniqmb)
                    indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
                elif (None not in uniqsb and len(uniqsb) >= 2):
                    uval = '/'.join(uniqsb)
                    indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-3])
                else:
                    print()
                    indata = indata
                indata = indata.drop(columns=['id1', 'id2', 'id3'])
            return indata

        data2 = colsplitps(data2)

        ptdata1 = pd.concat([data1, data2], sort=False)

        ptdata1 = ptdata1.rename(columns={'DP1': 'DP'})
        ptdata1 = ptdata1.rename(columns={'AF1': 'AF'})
        print('patient data shape after pass and otherinfo split: ', ptdata1.shape)

        filtvalues = ['exonic', 'exonic;splicing']
        Exonic_PASS = ptdata1[ptdata1['Func.refGene'].isin(filtvalues)]

        Splicing_PASS = ptdata1[ptdata1['Func.refGene'] == 'splicing']

        Exonic_PASS_Syn = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'] == 'synonymous SNV']

        Exonic_PASS_WithOut_Syn = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'] != 'synonymous SNV']

        Exonic_PASS_NonSyn = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'] == 'nonsynonymous SNV']

        filtvalues2 = ['frameshift deletion', 'frameshift insertion', 'nonframeshift deletion',
                       'nonframeshift insertion']
        Exonic_PASS_FS = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'].isin(filtvalues2)]

        filtvalues3 = ['stopgain', 'stoploss']
        Exonic_PASS_SGL = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'].isin(filtvalues3)]

        # otherfunction in Func.refGene
        Otherfunction = ptdata1[~ptdata1['Func.refGene'].isin(filtvalues)]

        filtshape = Otherfunction['Func.refGene'].value_counts()

        writer = pd.ExcelWriter(pathname_otherfun_shape, engine='xlsxwriter')
        filtshape.to_excel(writer, index=True)
        writer.save()

        outshape1 = Exonic_PASS.shape
        outshape2 = Splicing_PASS.shape
        outshape3 = Exonic_PASS_Syn.shape
        outshape4 = Exonic_PASS_WithOut_Syn.shape
        outshape5 = Exonic_PASS_NonSyn.shape
        outshape6 = Exonic_PASS_FS.shape
        outshape7 = Exonic_PASS_SGL.shape

        def writefun(data, pathname):
            fn = pathname.split('/')[-1]
            print('writing ', fn)
            writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
            data.to_excel(writer, index=False)
            writer.book.use_zip64()
            writer.save()

        writefun(Otherfunction, pathname_otherfun)
        writefun(Exonic_PASS, pathname1)
        writefun(Splicing_PASS, pathname2)
        writefun(Exonic_PASS_Syn, pathname3)
        writefun(Exonic_PASS_WithOut_Syn, pathname4)

        def srcgenesplit(indata):
            indata = indata.rename(columns={'Gene.refGene': 'Gene_refGene'})
            indata = \
                (indata.set_index(indata.columns.drop('Gene_refGene', 1).tolist())
                     .Gene_refGene.str.split(';', expand=True)
                     .stack()
                     .reset_index()
                     .rename(columns={0: 'Gene_refGene'})
                     .loc[:, indata.columns]
                     )
            indata = indata.rename(columns={'Gene_refGene': 'Gene.refGene'})
            return indata

        Exonic_PASS = srcgenesplit(Exonic_PASS)
        Splicing_PASS = srcgenesplit(Splicing_PASS)
        Exonic_PASS_Syn = srcgenesplit(Exonic_PASS_Syn)
        Exonic_PASS_WithOut_Syn = srcgenesplit(Exonic_PASS_WithOut_Syn)
        Exonic_PASS_NonSyn = srcgenesplit(Exonic_PASS_NonSyn)
        Exonic_PASS_FS = srcgenesplit(Exonic_PASS_FS)
        Exonic_PASS_SGL = srcgenesplit(Exonic_PASS_SGL)

        # 2455_gene alias match
        genedata = pd.read_excel(io=dbdata, sheet_name='2455_GeneData')

        genedata['Gene'] = genedata['Gene'].astype(str)

        genedata_ga = genedata[genedata['2455_Gene_Alias'].notnull()]
        genedata_notga = genedata.merge(genedata_ga, indicator=True, how='left').loc[lambda x: x['_merge'] != 'both']
        genedata_notga = genedata_notga.drop(['_merge'], axis=1)

        genedata_notga['2455_Gene_Alias'] = genedata_notga['Gene']

        genedata_ga['2455_Gene_Alias'] = genedata_ga['2455_Gene_Alias'].astype(str)
        genedata_ga['2455_Gene_Alias'] = genedata_ga['Gene'] + ', ' + genedata_ga['2455_Gene_Alias']

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

        Exonic_PASS_2455 = pd.merge(Exonic_PASS, genedata, left_on=['Gene.refGene'], right_on=['2455_Gene_Alias'],
                                    how='inner')
        Splicing_PASS_2455 = pd.merge(Splicing_PASS, genedata, left_on=['Gene.refGene'], right_on=['2455_Gene_Alias'],
                                      how='inner')
        Exonic_PASS_Syn_2455 = pd.merge(Exonic_PASS_Syn, genedata, left_on=['Gene.refGene'],
                                        right_on=['2455_Gene_Alias'],
                                        how='inner')
        Exonic_PASS_WithOut_Syn_2455 = pd.merge(Exonic_PASS_WithOut_Syn, genedata, left_on=['Gene.refGene'],
                                                right_on=['2455_Gene_Alias'], how='inner')
        Exonic_PASS_NonSyn_2455 = pd.merge(Exonic_PASS_NonSyn, genedata, left_on=['Gene.refGene'],
                                           right_on=['2455_Gene_Alias'], how='inner')
        Exonic_PASS_FS_2455 = pd.merge(Exonic_PASS_FS, genedata, left_on=['Gene.refGene'], right_on=['2455_Gene_Alias'],
                                       how='inner')
        Exonic_PASS_SGL_2455 = pd.merge(Exonic_PASS_SGL, genedata, left_on=['Gene.refGene'],
                                        right_on=['2455_Gene_Alias'],
                                        how='inner')

        # not match EESP
        eespnotmatch = Exonic_PASS.merge(Exonic_PASS_2455, indicator=True, how='left').loc[
            lambda x: x['_merge'] != 'both']
        eespnotmatch = eespnotmatch.drop(['_merge'], axis=1)

        writer = pd.ExcelWriter(pathname_eesp_notmatch, engine='xlsxwriter')
        eespnotmatch.to_excel(writer, index=False, sheet_name='NOTMATCH_Gene_EESP')
        writer.save()

        Exonic_PASS_2455 = Exonic_PASS_2455.drop_duplicates()
        Splicing_PASS_2455 = Splicing_PASS_2455.drop_duplicates()
        Exonic_PASS_Syn_2455 = Exonic_PASS_Syn_2455.drop_duplicates()
        Exonic_PASS_WithOut_Syn_2455 = Exonic_PASS_WithOut_Syn_2455.drop_duplicates()
        Exonic_PASS_NonSyn_2455 = Exonic_PASS_NonSyn_2455.drop_duplicates()
        Exonic_PASS_FS_2455 = Exonic_PASS_FS_2455.drop_duplicates()
        Exonic_PASS_SGL_2455 = Exonic_PASS_SGL_2455.drop_duplicates()

        outshape1_2455 = Exonic_PASS_2455.shape
        outshape2_2455 = Splicing_PASS_2455.shape
        outshape3_2455 = Exonic_PASS_Syn_2455.shape
        outshape4_2455 = Exonic_PASS_WithOut_Syn_2455.shape

        finalname_EESP1_2455 = finalname_EESP1 + '_2455GeneAlias'
        finalname_SpP2_2455 = finalname_SpP2 + '_2455GeneAlias'
        finalname_EESP_Syn3_2455 = finalname_EESP_Syn3 + '_2455GeneAlias'
        finalname_EESP_NSFSSGL4_2455 = finalname_EESP_NSFSSGL4 + '_2455GeneAlias'
        shape_cur_2455 = shape_cur + '_2455GeneAlias'

        pathname1_2455 = dirName2455gene + '/' + finalname_EESP1_2455 + '.xlsx'
        pathname2_2455 = dirName2455gene + '/' + finalname_SpP2_2455 + '.xlsx'
        pathname3_2455 = dirName2455gene + '/' + finalname_EESP_Syn3_2455 + '.xlsx'
        pathname4_2455 = dirName2455gene + '/' + finalname_EESP_NSFSSGL4_2455 + '.xlsx'
        path_shape_cur_2455 = dirName2455gene + '/' + shape_cur_2455 + '.xlsx'

        filenamelist = [finalname_EESP1, finalname_SpP2, finalname_EESP_Syn3, finalname_EESP_NSFSSGL4,
                        finalname_EESP_NonSyn5, finalname_EESP_FS6, finalname_EESP_SGL7, finalname_EESP1_2455,
                        finalname_SpP2_2455, finalname_EESP_Syn3_2455, finalname_EESP_NSFSSGL4_2455]
        rowlist = [outshape1[0], outshape2[0], outshape3[0], outshape4[0], outshape5[0], outshape6[0], outshape7[0],
                   outshape1_2455[0], outshape2_2455[0], outshape3_2455[0], outshape4_2455[0]]
        collist = [outshape1[1], outshape2[1], outshape3[1], outshape4[1], outshape5[1], outshape6[1], outshape7[1],
                   outshape1_2455[1], outshape2_2455[1], outshape3_2455[1], outshape4_2455[1]]

        shapedf_src_curation = pd.DataFrame(
            {'Filename': filenamelist,
             'No of rows': rowlist,
             'No of columns': collist
             })

        def writefun(data, pathname):
            fn = pathname.split('/')[-1]
            print('writing ', fn)
            writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
            data.to_excel(writer, index=False)
            writer.save()

        writefun(Exonic_PASS_2455, pathname1_2455)
        writefun(Splicing_PASS_2455, pathname2_2455)
        writefun(Exonic_PASS_Syn_2455, pathname3_2455)
        writefun(Exonic_PASS_WithOut_Syn_2455, pathname4_2455)
        writefun(shapedf_src_curation, path_shape_cur_2455)

        def indatacuration(indata):
            if ((indata.shape)[0] != 0):
                def cosidocursplit(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    if (max(new) == 1):
                        indata['cosmic_id'] = new[0]
                        indata['cosmic_occurence'] = new[1]
                    else:
                        indata['cosmic_id'] = new[0]
                        indata['cosmic_occurence'] = new[0]
                    return indata

                indata = cosidocursplit(indata, 'cosmicv89_coding', ";")

                def cosidcolsplit(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    indata.drop(columns=[col], inplace=True)
                    if (max(new) == 1):
                        indata['cosmic_id_data'] = new[1]
                    else:
                        indata['cosmic_id_data'] = new[0]
                    return indata

                indata = cosidcolsplit(indata, 'cosmic_id', '=')

                # rowsplit function
                def rowsplitcosid(indata, col, sep):
                    s = indata.assign(cosmic_id=indata[col].str.split(sep)).explode('cosmic_id')
                    indata.drop(columns=[col], inplace=True)
                    i = s.index.get_level_values(0)
                    indata = indata.loc[i].copy()
                    indata["cosmic_id"] = s['cosmic_id']
                    return indata

                indata = rowsplitcosid(indata, 'cosmic_id_data', ',')

                indata = indata.rename(columns={'Gene.refGene': 'Gene_refGene'})
                indata = \
                    (indata.set_index(indata.columns.drop('Gene_refGene', 1).tolist())
                         .Gene_refGene.str.split(';', expand=True)
                         .stack()
                         .reset_index()
                         .rename(columns={0: 'Gene_refGene'})
                         .loc[:, indata.columns]
                         )
                indata = indata.rename(columns={'Gene_refGene': 'Gene.refGene'})

                # AAChange.refgene row split
                indata = indata.rename(columns={'AAChange.refGene': 'AAChange_refGene'})
                indata = \
                    (indata.set_index(indata.columns.drop('AAChange_refGene', 1).tolist())
                         .AAChange_refGene.str.split(',', expand=True)
                         .stack()
                         .reset_index()
                         .rename(columns={0: 'AAChange_refGene'})
                         .loc[:, indata.columns]
                         )
                indata = indata.rename(columns={'AAChange_refGene': 'AAChange.refGene'})

                # colsplit
                def aachangecolsplit1(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    if (max(new) == 1):
                        indata['AAChange'] = new[1]
                        indata['AAChange_ref'] = new[0]
                    else:
                        indata['AAChange'] = new[0]
                        indata['AAChange_ref'] = new[0]
                    return indata

                indata = aachangecolsplit1(indata, 'AAChange.refGene', ":p.")

                # colsplit2
                def aachangecolsplit2(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    if (max(new) == 1):
                        indata['AAChange_CDS'] = new[1]
                        indata['AAChange_ref2'] = new[0]
                        indata = indata.drop(['AAChange_ref'], axis=1)
                    else:
                        indata['AAChange_CDS'] = new[0]
                        indata['AAChange_ref2'] = new[0]
                        indata = indata.drop(['AAChange_ref'], axis=1)
                    return indata

                indata = aachangecolsplit2(indata, 'AAChange_ref', ":c.")

                # colsplit3
                def aachangecolsplit2(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    if (max(new) == 2):
                        indata['AAChange_Exon'] = new[2]
                        indata = indata.drop(['AAChange_ref2'], axis=1)
                    else:
                        indata['AAChange_Exon'] = new[0]
                        indata = indata.drop(['AAChange_ref2'], axis=1)
                    return indata

                indata = aachangecolsplit2(indata, 'AAChange_ref2', ":")

            else:
                indata['cosmic_id'] = indata['cosmicv89_coding']
                indata['cosmic_occurence'] = indata['cosmicv89_coding']
                indata['AAChange'] = indata['AAChange.refGene']
                indata['AAChange_CDS'] = indata['AAChange.refGene']
                indata['AAChange_Exon'] = indata['AAChange.refGene']

            cols = list(indata)
            cols.insert(7, cols.pop(cols.index('AAChange')))
            cols.insert(8, cols.pop(cols.index('AAChange_Exon')))
            cols.insert(9, cols.pop(cols.index('AAChange_CDS')))
            indata = indata.loc[:, cols]

            return indata

        Exonic_PASS_2455 = indatacuration(Exonic_PASS_2455)
        Splicing_PASS_2455 = indatacuration(Splicing_PASS_2455)
        Exonic_PASS_Syn_2455 = indatacuration(Exonic_PASS_Syn_2455)
        Exonic_PASS_WithOut_Syn_2455 = indatacuration(Exonic_PASS_WithOut_Syn_2455)
        Exonic_PASS_NonSyn_2455 = indatacuration(Exonic_PASS_NonSyn_2455)
        Exonic_PASS_FS_2455 = indatacuration(Exonic_PASS_FS_2455)
        Exonic_PASS_SGL_2455 = indatacuration(Exonic_PASS_SGL_2455)

        # pathogenic single column
        def pathognicprdctn(data):
            if ((data.shape)[0] != 0):

                data['MutationAssessor_pred'] = data['MutationAssessor_pred'].replace('H', "D")

                data['MutPred_score'] = data['MutPred_score'].astype(str)
                data['MutPred_score'] = data['MutPred_score'].replace('.', "0")
                data['MutPred_score'] = data['MutPred_score'].replace('-', "0")
                data['MutPred_score'] = data['MutPred_score'].astype(float)
                data['MutPred_score'] = data['MutPred_score'] > 0.5
                data['MutPred_score'] = data['MutPred_score'].replace(True, "D")
                data['MutPred_score'] = data['MutPred_score'].replace(False, "")

                addlst = ['SIFT_pred', 'LRT_pred', 'MutationTaster_pred', 'MutationAssessor_pred', 'FATHMM_pred',
                          'PROVEAN_pred', 'MetaSVM_pred', 'MetaLR_pred', 'M-CAP_pred', 'fathmm-MKL_coding_pred',
                          'MutPred_score']
                if ('D' in data[addlst].values):
                    count = data[addlst].apply(lambda colnames: colnames.value_counts(), axis=1)[['D']]
                    data = pd.concat([data, count.fillna(0)], axis=1)
                    print('ifpart')
                else:
                    data['D'] = 0
                    print('elsepart')

                data['D'] = data['D'].astype(str)
                data['D'] = '(' + data['D'] + '/11)'

                data['SIFT_pred1'] = data['SIFT_pred']
                data['SIFT_pred1'] = data['SIFT_pred'] == 'D'
                data['SIFT_pred1'] = data['SIFT_pred1'].replace(True, "SIFT_pred")
                data['SIFT_pred1'] = data['SIFT_pred1'].replace(False, "")

                data['LRT_pred1'] = data['LRT_pred']
                data['LRT_pred1'] = data['LRT_pred'] == 'D'
                data['LRT_pred1'] = data['LRT_pred1'].replace(True, "LRT_pred")
                data['LRT_pred1'] = data['LRT_pred1'].replace(False, "")

                data['MutationTaster_pred1'] = data['MutationTaster_pred']
                data['MutationTaster_pred1'] = data['MutationTaster_pred'] == 'D'
                data['MutationTaster_pred1'] = data['MutationTaster_pred1'].replace(True, "MutationTaster_pred")
                data['MutationTaster_pred1'] = data['MutationTaster_pred1'].replace(False, "")

                data['MutationAssessor_pred1'] = data['MutationAssessor_pred']
                data['MutationAssessor_pred1'] = data['MutationAssessor_pred'] == 'D'
                data['MutationAssessor_pred1'] = data['MutationAssessor_pred1'].replace(True, "MutationAssessor_pred")
                data['MutationAssessor_pred1'] = data['MutationAssessor_pred1'].replace(False, "")

                data['FATHMM_pred1'] = data['FATHMM_pred']
                data['FATHMM_pred1'] = data['FATHMM_pred'] == 'D'
                data['FATHMM_pred1'] = data['FATHMM_pred1'].replace(True, "FATHMM_pred")
                data['FATHMM_pred1'] = data['FATHMM_pred1'].replace(False, "")

                data['PROVEAN_pred1'] = data['PROVEAN_pred']
                data['PROVEAN_pred1'] = data['PROVEAN_pred'] == 'D'
                data['PROVEAN_pred1'] = data['PROVEAN_pred1'].replace(True, "PROVEAN_pred")
                data['PROVEAN_pred1'] = data['PROVEAN_pred1'].replace(False, "")

                data['MetaSVM_pred1'] = data['MetaSVM_pred']
                data['MetaSVM_pred1'] = data['MetaSVM_pred'] == 'D'
                data['MetaSVM_pred1'] = data['MetaSVM_pred1'].replace(True, "MetaSVM_pred")
                data['MetaSVM_pred1'] = data['MetaSVM_pred1'].replace(False, "")

                data['MetaLR_pred1'] = data['MetaLR_pred']
                data['MetaLR_pred1'] = data['MetaLR_pred'] == 'D'
                data['MetaLR_pred1'] = data['MetaLR_pred1'].replace(True, "MetaLR_pred")
                data['MetaLR_pred1'] = data['MetaLR_pred1'].replace(False, "")

                data['M-CAP_pred1'] = data['M-CAP_pred']
                data['M-CAP_pred1'] = data['M-CAP_pred'] == 'D'
                data['M-CAP_pred1'] = data['M-CAP_pred1'].replace(True, "M-CAP_pred")
                data['M-CAP_pred1'] = data['M-CAP_pred1'].replace(False, "")

                data['fathmm-MKL_coding_pred1'] = data['fathmm-MKL_coding_pred']
                data['fathmm-MKL_coding_pred1'] = data['fathmm-MKL_coding_pred'] == 'D'
                data['fathmm-MKL_coding_pred1'] = data['fathmm-MKL_coding_pred1'].replace(True,
                                                                                          "fathmm-MKL_coding_pred")
                data['fathmm-MKL_coding_pred1'] = data['fathmm-MKL_coding_pred1'].replace(False, "")

                data['MutPred_score1'] = data['MutPred_score']
                data['MutPred_score1'] = data['MutPred_score1'].replace('D', "MutPred_score")

                data['ppcolname'] = data['SIFT_pred1'] + data['LRT_pred1'] + data['MutationTaster_pred1'] + data[
                    'MutationAssessor_pred1'] + data['FATHMM_pred1'] + data['PROVEAN_pred1'] + data['MetaSVM_pred1'] + \
                                    data[
                                        'MetaLR_pred1'] \
                                    + data['M-CAP_pred1'] + data['fathmm-MKL_coding_pred1'] + data['MutPred_score1']

                DRPLST = ['SIFT_pred1', 'LRT_pred1', 'MutationTaster_pred1', 'MutationAssessor_pred1', 'FATHMM_pred1',
                          'PROVEAN_pred1', 'MetaSVM_pred1', 'MetaLR_pred1', 'M-CAP_pred1', 'fathmm-MKL_coding_pred1',
                          'MutPred_score1']
                data = data.drop(DRPLST, axis=1)

                data['ppcolname'] = data['ppcolname'].str.replace(r'pred', r'pred, ')
                data['ppcolname'] = data['ppcolname'].str.replace(r'score', r'score, ')

                data['PathogenicPrediction'] = data['D'] + ', ' + data['ppcolname']
                data['PathogenicPrediction'] = data['PathogenicPrediction'].map(lambda x: str(x)[:-2])

                data = data.drop(['D', 'ppcolname'], axis=1)
            else:
                data['PathogenicPrediction'] = ''
            return data

        Exonic_PASS_2455 = pathognicprdctn(Exonic_PASS_2455)
        Splicing_PASS_2455 = pathognicprdctn(Splicing_PASS_2455)
        Exonic_PASS_Syn_2455 = pathognicprdctn(Exonic_PASS_Syn_2455)
        Exonic_PASS_WithOut_Syn_2455 = pathognicprdctn(Exonic_PASS_WithOut_Syn_2455)
        Exonic_PASS_NonSyn_2455 = pathognicprdctn(Exonic_PASS_NonSyn_2455)
        Exonic_PASS_FS_2455 = pathognicprdctn(Exonic_PASS_FS_2455)
        Exonic_PASS_SGL_2455 = pathognicprdctn(Exonic_PASS_SGL_2455)

        def maffilter(indata):
            # Exac_all_filter
            indata_dots = indata[indata['ExAC_ALL'] == '.']
            indata_vals = indata[indata['ExAC_ALL'] != '.']
            indata_vals['ExAC_ALL'] = indata_vals['ExAC_ALL'].astype(float)
            indata_vals = indata_vals[indata_vals['ExAC_ALL'] <= 0.01]
            indata = pd.concat([indata_dots, indata_vals], sort=False)

            # 1000g2015aug_all
            indata_dots = indata[indata['1000g2015aug_all'] == '.']
            indata_vals = indata[indata['1000g2015aug_all'] != '.']
            indata_vals['1000g2015aug_all'] = indata_vals['1000g2015aug_all'].astype(float)
            indata_vals = indata_vals[indata_vals['1000g2015aug_all'] <= 0.01]
            indata = pd.concat([indata_dots, indata_vals], sort=False)

            # AF
            indata_dots = indata[indata['AF'] == '.']
            indata_vals = indata[indata['AF'] != '.']
            indata_vals['AF'] = indata_vals['AF'].astype(float)
            indata_vals = indata_vals[indata_vals['AF'] <= 0.01]
            indata = pd.concat([indata_dots, indata_vals], sort=False)

            droplist = ['GeneDetail.refGene', 'AAChange.refGene', 'ExAC_AFR', 'ExAC_AMR', 'ExAC_EAS', 'ExAC_FIN',
                        'ExAC_NFE', 'ExAC_OTH', 'ExAC_SAS', '1000g2015aug_afr', '1000g2015aug_amr', '1000g2015aug_sas',
                        '1000g2015aug_eur', '1000g2015aug_eas',
                        'SIFT_score', 'SIFT_converted_rankscore', 'SIFT_pred', 'LRT_score', 'LRT_converted_rankscore',
                        'LRT_pred', 'MutationTaster_score', 'MutationTaster_converted_rankscore', 'MutationTaster_pred',
                        'MutationAssessor_score', 'MutationAssessor_score_rankscore', 'MutationAssessor_pred',
                        'FATHMM_score', 'FATHMM_converted_rankscore', 'FATHMM_pred', 'PROVEAN_score',
                        'PROVEAN_converted_rankscore',
                        'PROVEAN_pred', 'MetaSVM_score', 'MetaSVM_rankscore', 'MetaSVM_pred', 'MetaLR_score',
                        'MetaLR_rankscore', 'MetaLR_pred', 'M-CAP_score', 'M-CAP_rankscore', 'M-CAP_pred',
                        'MutPred_score',
                        'MutPred_rankscore',
                        'fathmm-MKL_coding_rankscore', 'Eigen_coding_or_noncoding', 'Eigen-raw', 'Eigen-PC-raw',
                        'GenoCanyon_score', 'GenoCanyon_score_rankscore', 'integrated_fitCons_score',
                        'integrated_fitCons_score_rankscore', 'integrated_confidence_value', 'GERP++_RS',
                        'GERP++_RS_rankscore', 'phyloP100way_vertebrate', 'phyloP100way_vertebrate_rankscore',
                        'phyloP20way_mammalian',
                        'phyloP20way_mammalian_rankscore', 'phastCons100way_vertebrate',
                        'phastCons100way_vertebrate_rankscore', 'phastCons20way_mammalian',
                        'phastCons20way_mammalian_rankscore', 'SiPhy_29way_logOdds',
                        'SiPhy_29way_logOdds_rankscore', 'GTEx_V6p_gene', 'GTEx_V6p_tissue', 'PVS1', 'PS1', 'PS2',
                        'PS3',
                        'PS4', 'PM1', 'PM2', 'PM3', 'PM4', 'PM5', 'PM6', 'PP1', 'PP2', 'PP3', 'PP4',
                        'PP5', 'BA1', 'BS1', 'BS2', 'BS3', 'BS4', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7',
                        'AF_popmax', 'AF_male', 'AF_female', 'AF_raw', 'AF_afr', 'AF_sas', 'AF_amr', 'AF_eas', 'AF_nfe',
                        'AF_fin',
                        'AF_asj', 'AF_oth', 'non_topmed_AF_popmax', 'non_neuro_AF_popmax', 'non_cancer_AF_popmax',
                        'controls_AF_popmax', 'Otherinfo1', 'Otherinfo2', 'Otherinfo3', 'Otherinfo4', 'Otherinfo5',
                        'Otherinfo6', 'Otherinfo7',
                        'Otherinfo8', 'Otherinfo9', 'Otherinfo10']

            indata = indata.drop(droplist, axis=1)

            return indata

        Exonic_PASS_2455_maf = maffilter(Exonic_PASS_2455)
        Splicing_PASS_2455_maf = maffilter(Splicing_PASS_2455)
        Exonic_PASS_Syn_2455_maf = maffilter(Exonic_PASS_Syn_2455)
        Exonic_PASS_WithOut_Syn_2455_maf = maffilter(Exonic_PASS_WithOut_Syn_2455)
        Exonic_PASS_NonSyn_2455_maf = maffilter(Exonic_PASS_NonSyn_2455)
        Exonic_PASS_FS_2455_maf = maffilter(Exonic_PASS_FS_2455)
        Exonic_PASS_SGL_2455_maf = maffilter(Exonic_PASS_SGL_2455)

        # TMB_Calculation
        if (inputfile == '' and tnpatientfile == ''):
            print('Please mention either TO_Patient_file or TN_Patient_File ')
            sys.exit()
        elif (dbdata == ''):
            print('TMB_Calculation will not done')
        else:
            print('TMB_Calculation started')

            def indatacuration(indata):
                # filter
                indata = indata[indata['avsnp150'] == '.']
                # filter
                indata = indata[indata['cosmicv89_coding'] == '.']
                # filter
                indata['AF_VAF'] = indata['AF_VAF'].astype(float)
                #indata = indata[(indata['AF_VAF'] >= 0.1) & (indata['AF_VAF'] <= 0.75)]
                indata = indata[indata['AF_VAF'] <= 0.5]
                return indata

            tmb_indata = indatacuration(Exonic_PASS)

            # tumor suppressor genes
            tsgdata = pd.read_excel(io=dbdata, sheet_name='MSK-Genes')

            tsgdata = tsgdata[tsgdata['Is Tumor Suppressor Gene'] == 'Yes']
            tsg = tsgdata['Hugo Symbol'].unique()

            tmbfiltvalues3 = ['stopgain', 'stoploss']
            tmb_indata_sgl = tmb_indata[tmb_indata['ExonicFunc.refGene'].isin(tmbfiltvalues3)]
            tmb_indata_sgl_un = tmb_indata_sgl[tmb_indata_sgl['Gene.refGene'].isin(tsg)]

            # difference
            tmbout1 = tmb_indata.merge(tmb_indata_sgl_un, indicator=True, how='left').loc[
                lambda x: x['_merge'] != 'both']
            tmbout1 = tmbout1.drop(['_merge'], axis=1)

            # tmbout1 = tmb_indata[~tmb_indata_sgl_un]
            tmb_out1_shape = tmbout1.shape

            tmb_value = tmb_out1_shape[0] / 39
            tmb_value = round(tmb_value, 5)
            fintmbval = str(tmb_value) + ' ' + 'Mut/Mb'
            print("TMB_Value is (>0.5)", fintmbval)

            if (tmb_value > 20):
                tmbstat = 'High'
            else:
                tmbstat = 'Low'

            fieldlist = ['Total Rows', 'Size of coding Region', 'TMB', 'STATUS', '', '', 'Legend:',
                         'TMB High>20 Mut/Mb',
                         'TMB Low<=20 Mut/Mb']
            valuelist = [tmb_out1_shape[0], 39, fintmbval, tmbstat]
            s1 = pd.Series(fieldlist, name='TMB Calculation')
            s2 = pd.Series(valuelist, name='')
            tmb_shapedf = pd.concat([s1, s2], axis=1)
            tmb_shapedf = tmb_shapedf.style.set_properties(**{'text-align': 'left'})

            print('writing ', finalname_EESP1_tmb)
            writer = pd.ExcelWriter(path_tmb, engine='xlsxwriter')
            tmb_shapedf.to_excel(writer, index=False)
            writer.save()

        print("---Source_curation took %s seconds to complete---" % (time.time() - start_time))

    if (tnpatientfile == ''):
        print('TN Patient file is not mentioned')
    else:
        print('TN file Sorce_curation started')
        head, tail = os.path.split(tnpatientfile)
        tailname = tail
        filename = tailname.split('.')[0]
        var1 = filename.split('_')[0]
        srcvar2 = filename.split('multianno')[0]
        finalname_master = srcvar2 + 'Master_File'
        finalname_fun = srcvar2 + 'PASS_Other_Fun_RefGene'
        finalname_EESP_notmmatched = srcvar2 + 'EES_PASS_Notmatched_with2455GA'
        finalname_EESP1 = srcvar2 + 'EES_PASS'
        finalname_SpP2 = srcvar2 + 'Sp_PASS'
        finalname_EESP_Syn3 = srcvar2 + 'EES_PASS_Syn'
        finalname_EESP_NSFSSGL4 = srcvar2 + 'EES_PASS_NS,FS,SGL'
        finalname_EESP_NonSyn5 = srcvar2 + 'EES_PASS_NonSyn'
        finalname_EESP_FS6 = srcvar2 + 'EES_PASS_FS'
        finalname_EESP_SGL7 = srcvar2 + 'EES_PASS_SGL'
        shape_cur = srcvar2 + 'Curation_Shapes'
        finalname_EESP1_tmb = srcvar2 + 'TMB_Calculation'

        dirName = appname+"/"+srcvar2 + 'DSP_Outputs'
        dirName_PreAnalysis = dirName + '/' + srcvar2 + 'PreAnalysis'
        dirName_Analysis = dirName + '/' + srcvar2 + 'Analysis'
        dirName_Report = dirName + '/' + srcvar2 + 'Report'
        dirName_Civic_Report = dirName_Report + '/' + srcvar2 + 'Civic_Report'
        dirName_Cosmic_Forlist_Report = dirName_Report + '/' + srcvar2 + 'Forlist_Report'
        dirName_cgcReport = dirName_Report + '/' + srcvar2 + 'CGC_Report'
        dirName_fdaReport = dirName_Report + '/' + srcvar2 + 'FDA_Report'
        dirName2 = dirName + '/' + srcvar2 + 'Src_curation'
        dirName_ARC = dirName + '/' + srcvar2 + 'Archive'
        dirName2455gene = dirName + '/' + srcvar2 + '2455gene_Src_curation'
        # dirName3 = dirName_Analysis + '/' + srcvar2 + 'Civic_match'
        dirName4 = dirName_ARC + '/' + srcvar2 + 'Cosmic_match'
        dirName5 = dirName_PreAnalysis + '/' + srcvar2 + 'Cosmic_DR'
        dirName6 = dirName_Analysis + '/' + srcvar2 + 'CGC_match'

        dirName_newcosmic = dirName_PreAnalysis + '/' + srcvar2 + 'Cosmic_match_Status'
        dirName_newcos7 = dirName_newcosmic + '/' + srcvar2 + 'Cos_Syn'
        dirName_newcos8 = dirName_newcosmic + '/' + srcvar2 + 'Cos_NS,FS,SGL'
        dirName_newcos11 = dirName_newcosmic + '/' + srcvar2 + 'Cos_Sp_PASS'

        dirName7 = dirName4 + '/' + srcvar2 + 'Cos_Syn'
        dirName8 = dirName4 + '/' + srcvar2 + 'Cos_NS,FS,SGL'
        dirName11 = dirName4 + '/' + srcvar2 + 'Cos_Sp_PASS'

        dirName13 = dirName5 + '/' + srcvar2 + 'Cos_DR_Syn'
        dirName14 = dirName5 + '/' + srcvar2 + 'Cos_DR_NS,FS,SGL'
        dirName17 = dirName5 + '/' + srcvar2 + 'Cos_DR_Sp_PASS'
        dirName19 = dirName_Analysis + '/' + srcvar2 + 'Cosmic_DR_For_List'
        dirName20 = dirName_Analysis + '/' + srcvar2 + 'CosRes_MATCH'
        dirName21 = dirName_Analysis + '/' + srcvar2 + 'Database_MATCH'
        dirName22 = dirName_Analysis + '/' + srcvar2 + 'OtherDatabase_MATCH'

        try:
            os.makedirs(dirName, mode=0o777)
            os.makedirs(dirName2, mode=0o777)
            os.makedirs(dirName_ARC, mode=0o777)
            os.makedirs(dirName2455gene, mode=0o777)
            os.makedirs(dirName_Analysis, mode=0o777)
            os.makedirs(dirName_PreAnalysis, mode=0o777)
            os.makedirs(dirName_Report, mode=0o777)
            print("Directory ", dirName, " Created ")
            print("Directory ", dirName2455gene, " Created ")
        except FileExistsError:
            print("Directory ", dirName, " already exists")
            print("Directory ", dirName2455gene, " already exists")

        pathname_master = dirName_ARC + '/' + finalname_master + '.tsv'
        pathname_otherfun = dirName2 + '/' + finalname_fun + '.xlsx'
        pathname_otherfun_shape = dirName_ARC + '/' + finalname_fun + '_shapes1.xlsx'
        pathname_eesp_notmatch = dirName_ARC + '/' + finalname_EESP_notmmatched + '.xlsx'
        pathname1 = dirName2 + '/' + finalname_EESP1 + '.xlsx'
        pathname2 = dirName2 + '/' + finalname_SpP2 + '.xlsx'
        pathname3 = dirName2 + '/' + finalname_EESP_Syn3 + '.xlsx'
        pathname4 = dirName2 + '/' + finalname_EESP_NSFSSGL4 + '.xlsx'
        pathname5 = dirName2 + '/' + finalname_EESP_NonSyn5 + '.xlsx'
        pathname6 = dirName2 + '/' + finalname_EESP_FS6 + '.xlsx'
        pathname7 = dirName2 + '/' + finalname_EESP_SGL7 + '.xlsx'
        path_shape_cur = dirName2 + '/' + shape_cur + '.xlsx'
        path_tmb = dirName2 + '/' + finalname_EESP1_tmb + '.xlsx'

        ptdata = pd.read_csv(tnpatientfile, sep="\t", header=[0])
        ptdata1 = pd.read_csv(tnpatientfile, sep="\t", header=None, skiprows=1)

        ptcollist = list(ptdata)
        ptcollst1 = list(ptdata1)

        ptfinlst = []
        x = 1
        for i in range(0, len(ptcollst1)):
            if (i < len(ptcollist)):
                ptfinlst.append(ptcollist[i])
            else:
                ptfinlst.append('Otherinfo' + str(x))
                x += 1
        ptdata1.columns = ptfinlst
        print('Patient data shape: ', ptdata1.shape)

        ptdata1.to_csv(pathname_master, sep='\t', index=False)

        ptdata1 = ptdata1.rename(columns={'DP': 'DP1'})
        ptdata1 = ptdata1.rename(columns={'AF': 'AF1'})

        passcolumn1 = list(ptdata1)[-5]
        dpmqtlodfircolumn = list(ptdata1)[-4]
        gtadafheadcolumn = list(ptdata1)[-3]
        gtadafvalcolumn = list(ptdata1)[-1]

        PASSdata = ptdata1[ptdata1[passcolumn1] == 'PASS']

        # col split dt tlod fir
        def colsplito8(indata, col, sep):
            new = indata[col].str.split(sep, expand=True)
            for i in range(0, max(new) + 1):
                indata[col + str(i)] = new[i]
                new2 = indata[col + str(i)].str.split('=', expand=True)
                indata = indata.drop(columns=col + str(i))
                indata[col + 'uv' + str(i)] = new2[0]
                uv = indata[col + 'uv' + str(i)].unique()
                uv2 = uv[0]
                # indata = indata.drop(columns=col + 'uv')
                if (len(uv) == 1):
                    indata[uv2] = new2[1]
                    indata = indata.drop(columns=col + 'uv' + str(i))
                elif (None not in uv and len(uv) == 2):
                    uval = '/'.join(uv)
                    indata[uval] = new2[1]
                    indata1 = indata[indata[col + 'uv' + str(i)] == uv[0]]
                    indata1[uv[0]] = indata1[uval]
                    indata2 = indata[indata[col + 'uv' + str(i)] == uv[1]]
                    indata2[uv[1]] = indata2[uval]
                    indata = pd.concat([indata1, indata2], sort=False)
                    indata = indata.drop(columns=col + 'uv' + str(i))
                    indata = indata.drop(columns=uval)
                elif (None in uv):
                    # elif(uv.__contains__(None)):
                    indata = indata.drop(columns=col + 'uv' + str(i))
                    newlst = []
                    for i in range(len(uv)):
                        if (uv[i] != None):
                            newlst.append(uv[i])
                    uvnew = newlst[0]
                    indata[uvnew + str(i)] = new2[1]
                else:
                    print()
                    indata = indata
            return indata

        ptdata1 = colsplito8(PASSdata, dpmqtlodfircolumn, ';')
        ptdata1 = ptdata1.rename(columns={'DP': 'DP_Total'})

        # gtadafclsplit
        def colsplitsub1(indata, col, sep):
            new = indata[col].str.split(sep, expand=True)
            for i in range(0, 7):
                indata[col + str(i)] = new[i]
                uv = indata[col + str(i)].unique()
                uvname = uv[0]
                indata = indata.drop(columns=col + str(i))
                new2 = indata[gtadafvalcolumn].str.split(':', expand=True)
                indata[uvname] = new2[i]
            return indata

        ptdata1 = colsplitsub1(ptdata1, gtadafheadcolumn, ':')

        ptdata1 = ptdata1.rename(columns={'DP': 'DP_Sample'})
        ptdata1 = ptdata1.rename(columns={'AF': 'AF_VAF'})

        data1 = ptdata1[ptdata1['GT'].str.contains('/')]
        data2 = ptdata1[~ptdata1['GT'].str.contains('/')]

        # sbmbsplit
        def colsplitsbmb(indata):
            indata['id2'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-2])
            indata['id1'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-1])
            uniqmb = indata['id1'].unique()
            uniqsb = indata['id2'].unique()
            if (len(uniqmb) == 1 and len(uniqsb) == 1):
                indata[uniqsb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
                indata[uniqmb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
            elif (len(uniqmb) == 1):
                indata[uniqmb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
            elif (len(uniqsb) == 1):
                indata[uniqsb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
            elif (None not in uniqmb and len(uniqmb) >= 2):
                uval = '/'.join(uniqmb)
                indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
            elif (None not in uniqsb and len(uniqsb) >= 2):
                uval = '/'.join(uniqsb)
                indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
            else:
                print()
                indata = indata
            indata = indata.drop(columns=['id1', 'id2'])
            return indata

        data1 = colsplitsbmb(data1)

        # sbmbpssplit
        def colsplitps(indata):
            if ((indata.shape)[0] != 0):
                indata['id1'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-1])
                indata['id2'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-2])
                indata['id3'] = indata[gtadafheadcolumn].apply(lambda x: x.split(':')[-3])
                uniqps = indata['id1'].unique()
                uniqmb = indata['id2'].unique()
                uniqsb = indata['id3'].unique()
                if (len(uniqps) == 1 and len(uniqmb) == 1 and len(uniqsb) == 1):
                    indata[uniqps[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
                    indata[uniqsb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-3])
                    indata[uniqmb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
                elif (len(uniqps) == 1):
                    indata[uniqps[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
                elif (len(uniqmb) == 1):
                    indata[uniqmb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
                elif (len(uniqsb) == 1):
                    indata[uniqsb[0]] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-3])
                elif (None not in uniqps and len(uniqps) >= 2):
                    uval = '/'.join(uniqps)
                    indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-1])
                elif (None not in uniqmb and len(uniqmb) >= 2):
                    uval = '/'.join(uniqmb)
                    indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-2])
                elif (None not in uniqsb and len(uniqsb) >= 2):
                    uval = '/'.join(uniqsb)
                    indata[uval] = indata[gtadafvalcolumn].apply(lambda x: x.split(':')[-3])
                else:
                    print()
                    indata = indata
                indata = indata.drop(columns=['id1', 'id2', 'id3'])
            return indata

        data2 = colsplitps(data2)

        ptdata1 = pd.concat([data1, data2], sort=False)

        ptdata1 = ptdata1.rename(columns={'DP1': 'DP'})
        ptdata1 = ptdata1.rename(columns={'AF1': 'AF'})
        print('patient data shape after pass and otherinfo split: ', ptdata1.shape)

        filtvalues = ['exonic', 'exonic;splicing']
        Exonic_PASS = ptdata1[ptdata1['Func.refGene'].isin(filtvalues)]

        Splicing_PASS = ptdata1[ptdata1['Func.refGene'] == 'splicing']

        Exonic_PASS_Syn = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'] == 'synonymous SNV']

        Exonic_PASS_WithOut_Syn = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'] != 'synonymous SNV']

        Exonic_PASS_NonSyn = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'] == 'nonsynonymous SNV']

        filtvalues2 = ['frameshift deletion', 'frameshift insertion', 'nonframeshift deletion',
                       'nonframeshift insertion']
        Exonic_PASS_FS = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'].isin(filtvalues2)]

        filtvalues3 = ['stopgain', 'stoploss']
        Exonic_PASS_SGL = Exonic_PASS[Exonic_PASS['ExonicFunc.refGene'].isin(filtvalues3)]

        # otherfunction in Func.refGene
        Otherfunction = ptdata1[~ptdata1['Func.refGene'].isin(filtvalues)]

        filtshape = Otherfunction['Func.refGene'].value_counts()

        writer = pd.ExcelWriter(pathname_otherfun_shape, engine='xlsxwriter')
        filtshape.to_excel(writer, index=True)
        writer.save()

        outshape1 = Exonic_PASS.shape
        outshape2 = Splicing_PASS.shape
        outshape3 = Exonic_PASS_Syn.shape
        outshape4 = Exonic_PASS_WithOut_Syn.shape
        outshape5 = Exonic_PASS_NonSyn.shape
        outshape6 = Exonic_PASS_FS.shape
        outshape7 = Exonic_PASS_SGL.shape

        def writefun(data, pathname):
            fn = pathname.split('/')[-1]
            print('writing ', fn)
            writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
            data.to_excel(writer, index=False)
            writer.save()

        writefun(Otherfunction, pathname_otherfun)
        writefun(Exonic_PASS, pathname1)
        writefun(Splicing_PASS, pathname2)
        writefun(Exonic_PASS_Syn, pathname3)
        writefun(Exonic_PASS_WithOut_Syn, pathname4)

        def srcgenesplit(indata):
            indata = indata.rename(columns={'Gene.refGene': 'Gene_refGene'})
            indata = \
                (indata.set_index(indata.columns.drop('Gene_refGene', 1).tolist())
                     .Gene_refGene.str.split(';', expand=True)
                     .stack()
                     .reset_index()
                     .rename(columns={0: 'Gene_refGene'})
                     .loc[:, indata.columns]
                     )
            indata = indata.rename(columns={'Gene_refGene': 'Gene.refGene'})
            return indata

        Exonic_PASS = srcgenesplit(Exonic_PASS)
        if Splicing_PASS.shape[0] > 0:
            Splicing_PASS = srcgenesplit(Splicing_PASS)
        
        Exonic_PASS_Syn = srcgenesplit(Exonic_PASS_Syn)
        Exonic_PASS_WithOut_Syn = srcgenesplit(Exonic_PASS_WithOut_Syn)
        Exonic_PASS_NonSyn = srcgenesplit(Exonic_PASS_NonSyn)
        Exonic_PASS_FS = srcgenesplit(Exonic_PASS_FS)
        Exonic_PASS_SGL = srcgenesplit(Exonic_PASS_SGL)

        # genedata = pd.read_excel('/home/vidhya/Downloads/GENE LIST_SOURCES.xlsx', sheet_name='Appended List_Source')
        # genedata = pd.read_csv('/home/vidhya/Downloads/DatabaseInputs/ncbi_alias_final1.csv')
        genedata = pd.read_excel(io=dbdata, sheet_name='2455_GeneData')

        genedata['Gene'] = genedata['Gene'].astype(str)

        genedata_ga = genedata[genedata['2455_Gene_Alias'].notnull()]
        genedata_notga = genedata.merge(genedata_ga, indicator=True, how='left').loc[lambda x: x['_merge'] != 'both']
        genedata_notga = genedata_notga.drop(['_merge'], axis=1)

        genedata_notga['2455_Gene_Alias'] = genedata_notga['Gene']

        genedata_ga['2455_Gene_Alias'] = genedata_ga['2455_Gene_Alias'].astype(str)
        genedata_ga['2455_Gene_Alias'] = genedata_ga['Gene'] + ', ' + genedata_ga['2455_Gene_Alias']

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

        Exonic_PASS_2455 = pd.merge(Exonic_PASS, genedata, left_on=['Gene.refGene'], right_on=['2455_Gene_Alias'],
                                    how='inner')
        Splicing_PASS_2455 = pd.merge(Splicing_PASS, genedata, left_on=['Gene.refGene'], right_on=['2455_Gene_Alias'],
                                      how='inner')
        Exonic_PASS_Syn_2455 = pd.merge(Exonic_PASS_Syn, genedata, left_on=['Gene.refGene'],
                                        right_on=['2455_Gene_Alias'],
                                        how='inner')
        Exonic_PASS_WithOut_Syn_2455 = pd.merge(Exonic_PASS_WithOut_Syn, genedata, left_on=['Gene.refGene'],
                                                right_on=['2455_Gene_Alias'], how='inner')
        Exonic_PASS_NonSyn_2455 = pd.merge(Exonic_PASS_NonSyn, genedata, left_on=['Gene.refGene'],
                                           right_on=['2455_Gene_Alias'], how='inner')
        Exonic_PASS_FS_2455 = pd.merge(Exonic_PASS_FS, genedata, left_on=['Gene.refGene'], right_on=['2455_Gene_Alias'],
                                       how='inner')
        Exonic_PASS_SGL_2455 = pd.merge(Exonic_PASS_SGL, genedata, left_on=['Gene.refGene'],
                                        right_on=['2455_Gene_Alias'],
                                        how='inner')

        eespnotmatch = Exonic_PASS.merge(Exonic_PASS_2455, indicator=True, how='left').loc[
            lambda x: x['_merge'] != 'both']
        eespnotmatch = eespnotmatch.drop(['_merge'], axis=1)

        writer = pd.ExcelWriter(pathname_eesp_notmatch, engine='xlsxwriter')
        eespnotmatch.to_excel(writer, index=False, sheet_name='NOTMATCH_Gene_EESP')
        writer.save()

        Exonic_PASS_2455 = Exonic_PASS_2455.drop_duplicates()
        Splicing_PASS_2455 = Splicing_PASS_2455.drop_duplicates()
        Exonic_PASS_Syn_2455 = Exonic_PASS_Syn_2455.drop_duplicates()
        Exonic_PASS_WithOut_Syn_2455 = Exonic_PASS_WithOut_Syn_2455.drop_duplicates()
        Exonic_PASS_NonSyn_2455 = Exonic_PASS_NonSyn_2455.drop_duplicates()
        Exonic_PASS_FS_2455 = Exonic_PASS_FS_2455.drop_duplicates()
        Exonic_PASS_SGL_2455 = Exonic_PASS_SGL_2455.drop_duplicates()

        outshape1_2455 = Exonic_PASS_2455.shape
        outshape2_2455 = Splicing_PASS_2455.shape
        outshape3_2455 = Exonic_PASS_Syn_2455.shape
        outshape4_2455 = Exonic_PASS_WithOut_Syn_2455.shape

        finalname_EESP1_2455 = finalname_EESP1 + '_2455GeneAlias'
        finalname_SpP2_2455 = finalname_SpP2 + '_2455GeneAlias'
        finalname_EESP_Syn3_2455 = finalname_EESP_Syn3 + '_2455GeneAlias'
        finalname_EESP_NSFSSGL4_2455 = finalname_EESP_NSFSSGL4 + '_2455GeneAlias'
        shape_cur_2455 = shape_cur + '_2455GeneAlias'

        pathname1_2455 = dirName2455gene + '/' + finalname_EESP1_2455 + '.xlsx'
        pathname2_2455 = dirName2455gene + '/' + finalname_SpP2_2455 + '.xlsx'
        pathname3_2455 = dirName2455gene + '/' + finalname_EESP_Syn3_2455 + '.xlsx'
        pathname4_2455 = dirName2455gene + '/' + finalname_EESP_NSFSSGL4_2455 + '.xlsx'
        path_shape_cur_2455 = dirName2455gene + '/' + shape_cur_2455 + '.xlsx'

        filenamelist = [finalname_EESP1, finalname_SpP2, finalname_EESP_Syn3, finalname_EESP_NSFSSGL4,
                        finalname_EESP_NonSyn5, finalname_EESP_FS6, finalname_EESP_SGL7, finalname_EESP1_2455,
                        finalname_SpP2_2455, finalname_EESP_Syn3_2455, finalname_EESP_NSFSSGL4_2455]
        rowlist = [outshape1[0], outshape2[0], outshape3[0], outshape4[0], outshape5[0], outshape6[0], outshape7[0],
                   outshape1_2455[0], outshape2_2455[0], outshape3_2455[0], outshape4_2455[0]]
        collist = [outshape1[1], outshape2[1], outshape3[1], outshape4[1], outshape5[1], outshape6[1], outshape7[1],
                   outshape1_2455[1], outshape2_2455[1], outshape3_2455[1], outshape4_2455[1]]

        shapedf_src_curation = pd.DataFrame(
            {'Filename': filenamelist,
             'No of rows': rowlist,
             'No of columns': collist,
             })

        def writefun(data, pathname):
            fn = pathname.split('/')[-1]
            print('writing ', fn)
            writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
            data.to_excel(writer, index=False)
            writer.save()

        writefun(Exonic_PASS_2455, pathname1_2455)
        writefun(Splicing_PASS_2455, pathname2_2455)
        writefun(Exonic_PASS_Syn_2455, pathname3_2455)
        writefun(Exonic_PASS_WithOut_Syn_2455, pathname4_2455)
        writefun(shapedf_src_curation, path_shape_cur_2455)

        def indatacuration(indata):
            if ((indata.shape)[0] != 0):
                def cosidocursplit(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    if (max(new) == 1):
                        indata['cosmic_id'] = new[0]
                        indata['cosmic_occurence'] = new[1]
                    else:
                        indata['cosmic_id'] = new[0]
                        indata['cosmic_occurence'] = new[0]
                    return indata

                indata = cosidocursplit(indata, 'cosmicv89_coding', ";")

                def cosidcolsplit(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    indata.drop(columns=[col], inplace=True)
                    if (max(new) == 1):
                        indata['cosmic_id_data'] = new[1]
                    else:
                        indata['cosmic_id_data'] = new[0]
                    return indata

                indata = cosidcolsplit(indata, 'cosmic_id', '=')

                # rowsplit function
                def rowsplitcosid(indata, col, sep):
                    s = indata.assign(cosmic_id=indata[col].str.split(sep)).explode('cosmic_id')
                    indata.drop(columns=[col], inplace=True)
                    i = s.index.get_level_values(0)
                    indata = indata.loc[i].copy()
                    indata["cosmic_id"] = s['cosmic_id']
                    return indata

                indata = rowsplitcosid(indata, 'cosmic_id_data', ',')

                indata = indata.rename(columns={'Gene.refGene': 'Gene_refGene'})
                indata = \
                    (indata.set_index(indata.columns.drop('Gene_refGene', 1).tolist())
                         .Gene_refGene.str.split(';', expand=True)
                         .stack()
                         .reset_index()
                         .rename(columns={0: 'Gene_refGene'})
                         .loc[:, indata.columns]
                         )
                indata = indata.rename(columns={'Gene_refGene': 'Gene.refGene'})

                # AAChange.refgene row split
                indata = indata.rename(columns={'AAChange.refGene': 'AAChange_refGene'})
                indata = \
                    (indata.set_index(indata.columns.drop('AAChange_refGene', 1).tolist())
                         .AAChange_refGene.str.split(',', expand=True)
                         .stack()
                         .reset_index()
                         .rename(columns={0: 'AAChange_refGene'})
                         .loc[:, indata.columns]
                         )
                indata = indata.rename(columns={'AAChange_refGene': 'AAChange.refGene'})

                # colsplit
                def aachangecolsplit1(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    if (max(new) == 1):
                        indata['AAChange'] = new[1]
                        indata['AAChange_ref'] = new[0]
                    else:
                        indata['AAChange'] = new[0]
                        indata['AAChange_ref'] = new[0]
                    return indata

                indata = aachangecolsplit1(indata, 'AAChange.refGene', ":p.")

                # colsplit2
                def aachangecolsplit2(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    if (max(new) == 1):
                        indata['AAChange_CDS'] = new[1]
                        indata['AAChange_ref2'] = new[0]
                        indata = indata.drop(['AAChange_ref'], axis=1)
                    else:
                        indata['AAChange_CDS'] = new[0]
                        indata['AAChange_ref2'] = new[0]
                        indata = indata.drop(['AAChange_ref'], axis=1)
                    return indata

                indata = aachangecolsplit2(indata, 'AAChange_ref', ":c.")

                # colsplit3
                def aachangecolsplit2(indata, col, sep):
                    new = indata[col].str.split(sep, expand=True)
                    if (max(new) == 2):
                        indata['AAChange_Exon'] = new[2]
                        indata = indata.drop(['AAChange_ref2'], axis=1)
                    else:
                        indata['AAChange_Exon'] = new[0]
                        indata = indata.drop(['AAChange_ref2'], axis=1)
                    return indata

                indata = aachangecolsplit2(indata, 'AAChange_ref2', ":")

            else:
                indata['cosmic_id'] = indata['cosmicv89_coding']
                indata['cosmic_occurence'] = indata['cosmicv89_coding']
                indata['AAChange'] = indata['AAChange.refGene']
                indata['AAChange_CDS'] = indata['AAChange.refGene']
                indata['AAChange_Exon'] = indata['AAChange.refGene']

            cols = list(indata)
            cols.insert(7, cols.pop(cols.index('AAChange')))
            cols.insert(8, cols.pop(cols.index('AAChange_Exon')))
            cols.insert(9, cols.pop(cols.index('AAChange_CDS')))
            indata = indata.loc[:, cols]
            return indata

        Exonic_PASS_2455 = indatacuration(Exonic_PASS_2455)
        Splicing_PASS_2455 = indatacuration(Splicing_PASS_2455)
        Exonic_PASS_Syn_2455 = indatacuration(Exonic_PASS_Syn_2455)
        Exonic_PASS_WithOut_Syn_2455 = indatacuration(Exonic_PASS_WithOut_Syn_2455)
        Exonic_PASS_NonSyn_2455 = indatacuration(Exonic_PASS_NonSyn_2455)
        Exonic_PASS_FS_2455 = indatacuration(Exonic_PASS_FS_2455)
        Exonic_PASS_SGL_2455 = indatacuration(Exonic_PASS_SGL_2455)

        # pathogenic single column
        def pathognicprdctn(data):
            if ((data.shape)[0] != 0):

                data['MutationAssessor_pred'] = data['MutationAssessor_pred'].replace('H', "D")

                data['MutPred_score'] = data['MutPred_score'].astype(str)
                data['MutPred_score'] = data['MutPred_score'].replace('.', "0")
                data['MutPred_score'] = data['MutPred_score'].astype(float)
                data['MutPred_score'] = data['MutPred_score'] > 0.5
                data['MutPred_score'] = data['MutPred_score'].replace(True, "D")
                data['MutPred_score'] = data['MutPred_score'].replace(False, "")

                addlst = ['SIFT_pred', 'LRT_pred', 'MutationTaster_pred', 'MutationAssessor_pred', 'FATHMM_pred',
                          'PROVEAN_pred', 'MetaSVM_pred', 'MetaLR_pred', 'M-CAP_pred', 'fathmm-MKL_coding_pred',
                          'MutPred_score']
                if ('D' in data[addlst].values):
                    count = data[addlst].apply(lambda colnames: colnames.value_counts(), axis=1)[['D']]
                    data = pd.concat([data, count.fillna(0)], axis=1)
                    print('ifpart')
                else:
                    data['D'] = 0
                    print('elsepart')

                data['D'] = data['D'].astype(str)
                data['D'] = '(' + data['D'] + '/11)'

                data['SIFT_pred1'] = data['SIFT_pred']
                data['SIFT_pred1'] = data['SIFT_pred'] == 'D'
                data['SIFT_pred1'] = data['SIFT_pred1'].replace(True, "SIFT_pred")
                data['SIFT_pred1'] = data['SIFT_pred1'].replace(False, "")

                data['LRT_pred1'] = data['LRT_pred']
                data['LRT_pred1'] = data['LRT_pred'] == 'D'
                data['LRT_pred1'] = data['LRT_pred1'].replace(True, "LRT_pred")
                data['LRT_pred1'] = data['LRT_pred1'].replace(False, "")

                data['MutationTaster_pred1'] = data['MutationTaster_pred']
                data['MutationTaster_pred1'] = data['MutationTaster_pred'] == 'D'
                data['MutationTaster_pred1'] = data['MutationTaster_pred1'].replace(True, "MutationTaster_pred")
                data['MutationTaster_pred1'] = data['MutationTaster_pred1'].replace(False, "")

                data['MutationAssessor_pred1'] = data['MutationAssessor_pred']
                data['MutationAssessor_pred1'] = data['MutationAssessor_pred'] == 'D'
                data['MutationAssessor_pred1'] = data['MutationAssessor_pred1'].replace(True, "MutationAssessor_pred")
                data['MutationAssessor_pred1'] = data['MutationAssessor_pred1'].replace(False, "")

                data['FATHMM_pred1'] = data['FATHMM_pred']
                data['FATHMM_pred1'] = data['FATHMM_pred'] == 'D'
                data['FATHMM_pred1'] = data['FATHMM_pred1'].replace(True, "FATHMM_pred")
                data['FATHMM_pred1'] = data['FATHMM_pred1'].replace(False, "")

                data['PROVEAN_pred1'] = data['PROVEAN_pred']
                data['PROVEAN_pred1'] = data['PROVEAN_pred'] == 'D'
                data['PROVEAN_pred1'] = data['PROVEAN_pred1'].replace(True, "PROVEAN_pred")
                data['PROVEAN_pred1'] = data['PROVEAN_pred1'].replace(False, "")

                data['MetaSVM_pred1'] = data['MetaSVM_pred']
                data['MetaSVM_pred1'] = data['MetaSVM_pred'] == 'D'
                data['MetaSVM_pred1'] = data['MetaSVM_pred1'].replace(True, "MetaSVM_pred")
                data['MetaSVM_pred1'] = data['MetaSVM_pred1'].replace(False, "")

                data['MetaLR_pred1'] = data['MetaLR_pred']
                data['MetaLR_pred1'] = data['MetaLR_pred'] == 'D'
                data['MetaLR_pred1'] = data['MetaLR_pred1'].replace(True, "MetaLR_pred")
                data['MetaLR_pred1'] = data['MetaLR_pred1'].replace(False, "")

                data['M-CAP_pred1'] = data['M-CAP_pred']
                data['M-CAP_pred1'] = data['M-CAP_pred'] == 'D'
                data['M-CAP_pred1'] = data['M-CAP_pred1'].replace(True, "M-CAP_pred")
                data['M-CAP_pred1'] = data['M-CAP_pred1'].replace(False, "")

                data['fathmm-MKL_coding_pred1'] = data['fathmm-MKL_coding_pred']
                data['fathmm-MKL_coding_pred1'] = data['fathmm-MKL_coding_pred'] == 'D'
                data['fathmm-MKL_coding_pred1'] = data['fathmm-MKL_coding_pred1'].replace(True,
                                                                                          "fathmm-MKL_coding_pred")
                data['fathmm-MKL_coding_pred1'] = data['fathmm-MKL_coding_pred1'].replace(False, "")

                data['MutPred_score1'] = data['MutPred_score']
                data['MutPred_score1'] = data['MutPred_score1'].replace('D', "MutPred_score")

                data['ppcolname'] = data['SIFT_pred1'] + data['LRT_pred1'] + data['MutationTaster_pred1'] + data[
                    'MutationAssessor_pred1'] + data['FATHMM_pred1'] + data['PROVEAN_pred1'] + data['MetaSVM_pred1'] + \
                                    data[
                                        'MetaLR_pred1'] \
                                    + data['M-CAP_pred1'] + data['fathmm-MKL_coding_pred1'] + data['MutPred_score1']

                DRPLST = ['SIFT_pred1', 'LRT_pred1', 'MutationTaster_pred1', 'MutationAssessor_pred1', 'FATHMM_pred1',
                          'PROVEAN_pred1', 'MetaSVM_pred1', 'MetaLR_pred1', 'M-CAP_pred1', 'fathmm-MKL_coding_pred1',
                          'MutPred_score1']
                data = data.drop(DRPLST, axis=1)

                data['ppcolname'] = data['ppcolname'].str.replace(r'pred', r'pred, ')
                data['ppcolname'] = data['ppcolname'].str.replace(r'score', r'score, ')

                data['PathogenicPrediction'] = data['D'] + ', ' + data['ppcolname']
                data['PathogenicPrediction'] = data['PathogenicPrediction'].map(lambda x: str(x)[:-2])

                data = data.drop(['D', 'ppcolname'], axis=1)
            else:
                data['PathogenicPrediction'] = ''
            return data

        Exonic_PASS_2455 = pathognicprdctn(Exonic_PASS_2455)
        Splicing_PASS_2455 = pathognicprdctn(Splicing_PASS_2455)
        Exonic_PASS_Syn_2455 = pathognicprdctn(Exonic_PASS_Syn_2455)
        Exonic_PASS_WithOut_Syn_2455 = pathognicprdctn(Exonic_PASS_WithOut_Syn_2455)
        Exonic_PASS_NonSyn_2455 = pathognicprdctn(Exonic_PASS_NonSyn_2455)
        Exonic_PASS_FS_2455 = pathognicprdctn(Exonic_PASS_FS_2455)
        Exonic_PASS_SGL_2455 = pathognicprdctn(Exonic_PASS_SGL_2455)

        def maffilter(indata):
            # Exac_all_filter
            # indata_dots = indata[indata['ExAC_ALL'] == '.']
            # indata_vals = indata[indata['ExAC_ALL'] != '.']
            # indata_vals['ExAC_ALL'] = indata_vals['ExAC_ALL'].astype(float)
            # indata_vals = indata_vals[indata_vals['ExAC_ALL'] <= 0.01]
            # indata = pd.concat([indata_dots, indata_vals], sort=False)
            #
            # # 1000g2015aug_all
            # indata_dots = indata[indata['1000g2015aug_all'] == '.']
            # indata_vals = indata[indata['1000g2015aug_all'] != '.']
            # indata_vals['1000g2015aug_all'] = indata_vals['1000g2015aug_all'].astype(float)
            # indata_vals = indata_vals[indata_vals['1000g2015aug_all'] <= 0.01]
            # indata = pd.concat([indata_dots, indata_vals], sort=False)
            #
            # # AF
            # indata_dots = indata[indata['AF'] == '.']
            # indata_vals = indata[indata['AF'] != '.']
            # indata_vals['AF'] = indata_vals['AF'].astype(float)
            # indata_vals = indata_vals[indata_vals['AF'] <= 0.01]
            # indata = pd.concat([indata_dots, indata_vals], sort=False)

            droplist = ['GeneDetail.refGene', 'AAChange.refGene', 'ExAC_AFR', 'ExAC_AMR', 'ExAC_EAS', 'ExAC_FIN',
                        'ExAC_NFE', 'ExAC_OTH', 'ExAC_SAS', '1000g2015aug_afr', '1000g2015aug_amr', '1000g2015aug_sas',
                        '1000g2015aug_eur', '1000g2015aug_eas',
                        'SIFT_score', 'SIFT_converted_rankscore', 'SIFT_pred', 'LRT_score', 'LRT_converted_rankscore',
                        'LRT_pred', 'MutationTaster_score', 'MutationTaster_converted_rankscore', 'MutationTaster_pred',
                        'MutationAssessor_score', 'MutationAssessor_score_rankscore', 'MutationAssessor_pred',
                        'FATHMM_score', 'FATHMM_converted_rankscore', 'FATHMM_pred', 'PROVEAN_score',
                        'PROVEAN_converted_rankscore',
                        'PROVEAN_pred', 'MetaSVM_score', 'MetaSVM_rankscore', 'MetaSVM_pred', 'MetaLR_score',
                        'MetaLR_rankscore', 'MetaLR_pred', 'M-CAP_score', 'M-CAP_rankscore', 'M-CAP_pred',
                        'MutPred_score',
                        'MutPred_rankscore',
                        'fathmm-MKL_coding_rankscore', 'Eigen_coding_or_noncoding', 'Eigen-raw', 'Eigen-PC-raw',
                        'GenoCanyon_score', 'GenoCanyon_score_rankscore', 'integrated_fitCons_score',
                        'integrated_fitCons_score_rankscore', 'integrated_confidence_value', 'GERP++_RS',
                        'GERP++_RS_rankscore', 'phyloP100way_vertebrate', 'phyloP100way_vertebrate_rankscore',
                        'phyloP20way_mammalian',
                        'phyloP20way_mammalian_rankscore', 'phastCons100way_vertebrate',
                        'phastCons100way_vertebrate_rankscore', 'phastCons20way_mammalian',
                        'phastCons20way_mammalian_rankscore', 'SiPhy_29way_logOdds',
                        'SiPhy_29way_logOdds_rankscore', 'GTEx_V6p_gene', 'GTEx_V6p_tissue', 'PVS1', 'PS1', 'PS2',
                        'PS3',
                        'PS4', 'PM1', 'PM2', 'PM3', 'PM4', 'PM5', 'PM6', 'PP1', 'PP2', 'PP3', 'PP4',
                        'PP5', 'BA1', 'BS1', 'BS2', 'BS3', 'BS4', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7',
                        'AF_popmax', 'AF_male', 'AF_female', 'AF_raw', 'AF_afr', 'AF_sas', 'AF_amr', 'AF_eas', 'AF_nfe',
                        'AF_fin',
                        'AF_asj', 'AF_oth', 'non_topmed_AF_popmax', 'non_neuro_AF_popmax', 'non_cancer_AF_popmax',
                        'controls_AF_popmax', 'Otherinfo1', 'Otherinfo2', 'Otherinfo3', 'Otherinfo4', 'Otherinfo5',
                        'Otherinfo6', 'Otherinfo7',
                        'Otherinfo8', 'Otherinfo9', 'Otherinfo10']

            indata = indata.drop(droplist, axis=1)

            return indata


        Exonic_PASS_2455.to_csv('before_filter.tsv', sep='\t')
        Exonic_PASS_2455_maf = maffilter(Exonic_PASS_2455)
        Exonic_PASS_2455_maf.to_csv('after_filter.tsv', sep='\t')
        Splicing_PASS_2455_maf = maffilter(Splicing_PASS_2455)
        Exonic_PASS_Syn_2455_maf = maffilter(Exonic_PASS_Syn_2455)
        Exonic_PASS_WithOut_Syn_2455_maf = maffilter(Exonic_PASS_WithOut_Syn_2455)
        Exonic_PASS_NonSyn_2455_maf = maffilter(Exonic_PASS_NonSyn_2455)
        Exonic_PASS_FS_2455_maf = maffilter(Exonic_PASS_FS_2455)
        Exonic_PASS_SGL_2455_maf = maffilter(Exonic_PASS_SGL_2455)

        # TMB_Calculation
        if (inputfile == '' and tnpatientfile == ''):
            print('Please mention either TO_Patient_file or TN_Patient_File ')
            sys.exit()
        elif (dbdata == ''):
            print('TMB_Calculation will not done')
        else:
            print('TMB_Calculation started')

            def indatacuration(indata):
                # filter
                indata = indata[indata['avsnp150'] == '.']
                # filter
                indata = indata[indata['cosmicv89_coding'] == '.']
                # filter
                indata['AF_VAF'] = indata['AF_VAF'].astype(float)
                #indata = indata[(indata['AF_VAF'] >= 0.1) & (indata['AF_VAF'] <= 0.75)]
                #indata = indata(indata['AF_VAF'] >= 0.4)
                return indata

            tmb_indata = indatacuration(Exonic_PASS)

            # tumor suppressor genes
            tsgdata = pd.read_excel(io=dbdata, sheet_name='MSK-Genes')

            tsgdata = tsgdata[tsgdata['Is Tumor Suppressor Gene'] == 'Yes']
            tsg = tsgdata['Hugo Symbol'].unique()

            tmbfiltvalues3 = ['stopgain', 'stoploss']
            tmb_indata_sgl = tmb_indata[tmb_indata['ExonicFunc.refGene'].isin(tmbfiltvalues3)]
            tmb_indata_sgl_un = tmb_indata_sgl[tmb_indata_sgl['Gene.refGene'].isin(tsg)]

            # difference
            tmbout1 = tmb_indata.merge(tmb_indata_sgl_un, indicator=True, how='left').loc[
                lambda x: x['_merge'] != 'both']
            tmbout1 = tmbout1.drop(['_merge'], axis=1)

            # tmbout1 = tmb_indata[~tmb_indata_sgl_un]
            tmb_out1_shape = tmbout1.shape

            tmb_value = tmb_out1_shape[0] / 39
            tmb_value = round(tmb_value, 5)
            fintmbval = str(tmb_value) + ' ' + 'Mut/Mb'
            print("TMB_Value is ", fintmbval)

            if (tmb_value > 20):
                tmbstat = 'High'
            else:
                tmbstat = 'Low'

            fieldlist = ['Total Rows', 'Size of coding Region', 'TMB', 'STATUS', '', '', 'Legend:',
                         'TMB High>20 Mut/Mb',
                         'TMB Low<=20 Mut/Mb']
            valuelist = [tmb_out1_shape[0], 39, fintmbval, tmbstat]
            s1 = pd.Series(fieldlist, name='TMB Calculation')
            s2 = pd.Series(valuelist, name='')
            tmb_shapedf = pd.concat([s1, s2], axis=1)
            tmb_shapedf = tmb_shapedf.style.set_properties(**{'text-align': 'left'})

            print('writing ', finalname_EESP1_tmb)
            writer = pd.ExcelWriter(path_tmb, engine='xlsxwriter')
            tmb_shapedf.to_excel(writer, index=False)
            writer.save()

        print("---Source_curation took %s seconds to complete---" % (time.time() - start_time))

    # cosmic(new and old)
    if (inputfile == '' and tnpatientfile == ''):
        print('Please mention either TO_Patient_file or TN_Patient_File ')
        sys.exit()
    elif (cosdata == ''):
        print('Cosmic_match will not done')
    else:
        print('cosmic_match started')
        try:
            os.makedirs(dirName_newcosmic, mode=0o777)
            os.makedirs(dirName_newcos7, mode=0o777)
            os.makedirs(dirName_newcos8, mode=0o777)
            os.makedirs(dirName_newcos11, mode=0o777)
            os.makedirs(dirName4, mode=0o777)
            os.makedirs(dirName7, mode=0o777)
            os.makedirs(dirName8, mode=0o777)
            os.makedirs(dirName11, mode=0o777)

            print("Directory ", dirName_newcosmic, " Created ")
            print("Directory ", dirName4, " Created ")
        except FileExistsError:
            print("Directory ", dirName_newcosmic, " already exists")
            print("Directory ", dirName4, " already exists")

        def cosfinalfilename(filename, dname, dname2):
            var1 = filename.split('EES')[0]
            var2 = filename.split('_')[-1]
            master = var1 + 'CG_Mast_' + var2
            finalname1 = var1 + 'CG_' + var2 + '_Y'
            finalname2 = var1 + 'CG_' + var2 + '_N'
            finalname3 = var1 + 'CG_' + var2 + '_B'
            finalname4 = var1 + 'CG_' + var2 + '_WO_CosID'
            finalname5 = var1 + 'CG_NotMatch' + var2
            finalname1_new = var1 + 'CG_' + var2 + '_new_Y_D'
            finalname2_new = var1 + 'CG_' + var2 + '_new_N'
            finalname3_new = var1 + 'CG_' + var2 + '_new_B'
            pathname1_new = dname2 + '/' + finalname1_new + '.xlsx'
            pathname1 = dname + '/' + finalname1 + '.xlsx'
            pathname2_new = dname2 + '/' + finalname2_new + '.xlsx'
            pathname2 = dname + '/' + finalname2 + '.xlsx'
            pathname3_new = dname2 + '/' + finalname3_new + '.xlsx'
            pathname3 = dname + '/' + finalname3 + '.xlsx'
            pathname4_new = dname2 + '/' + finalname4 + '.xlsx'
            # pathnameMAST = dname + '/' + master + '.xlsx'
            pathname5_new = dname2 + '/' + finalname5 + '.xlsx'
            return [master, finalname1, finalname2, finalname3, finalname4, finalname5, pathname1, pathname2, pathname3,
                    pathname1_new, pathname2_new, pathname3_new, pathname4_new, pathname5_new, finalname1_new,
                    finalname2_new, finalname3_new]

        cosfilename1 = cosfinalfilename(finalname_EESP_Syn3, dirName7, dirName_newcos7)
        cosfilename2 = cosfinalfilename(finalname_EESP_NSFSSGL4, dirName8, dirName_newcos8)
        cosfilename3 = cosfinalfilename(finalname_EESP_NonSyn5, dirName8, dirName_newcos8)
        cosfilename4 = cosfinalfilename(finalname_EESP_FS6, dirName8, dirName_newcos8)
        cosfilename6 = cosfinalfilename(finalname_EESP_SGL7, dirName8, dirName_newcos8)

        def cosfinalfilenamesp(filename, dname, dname2):
            var1 = filename.split('Sp')[0]
            var2 = 'SP_PASS'
            master = var1 + 'CG_Mast_' + var2
            finalname1 = var1 + 'CG_' + var2 + '_Y'
            finalname2 = var1 + 'CG_' + var2 + '_N'
            finalname3 = var1 + 'CG_' + var2 + '_B'
            finalname4 = var1 + 'CG_' + var2 + '_WO_CosID'
            finalname5 = var1 + 'CG_NotMatch' + var2
            finalname1_new = var1 + 'CG_' + var2 + '_new_Y_D'
            finalname2_new = var1 + 'CG_' + var2 + '_new_N'
            finalname3_new = var1 + 'CG_' + var2 + '_new_B'
            pathname1_new = dname2 + '/' + finalname1_new + '.xlsx'
            pathname1 = dname + '/' + finalname1 + '.xlsx'
            pathname2_new = dname2 + '/' + finalname2_new + '.xlsx'
            pathname2 = dname + '/' + finalname2 + '.xlsx'
            pathname3_new = dname2 + '/' + finalname3_new + '.xlsx'
            pathname3 = dname + '/' + finalname3 + '.xlsx'
            pathname4_new = dname2 + '/' + finalname4 + '.xlsx'
            # pathnameMAST = dname + '/' + master + '.xlsx'
            pathname5_new = dname2 + '/' + finalname5 + '.xlsx'
            return [master, finalname1, finalname2, finalname3, finalname4, finalname5, pathname1, pathname2, pathname3,
                    pathname1_new, pathname2_new, pathname3_new, pathname4_new, pathname5_new, finalname1_new,
                    finalname2_new, finalname3_new]

        cosfilename5 = cosfinalfilenamesp(finalname_SpP2, dirName11, dirName_newcos11)

        cosshapename = var1 + 'CG_Shapes'
        cosshapepn_new = dirName_newcosmic + '/' + cosshapename + '.xlsx'
        cosshapepn = dirName4 + '/' + cosshapename + '.xlsx'

        # cosinputs
        cos_indata1 = Exonic_PASS_Syn_2455_maf
        cos_indata2 = Exonic_PASS_WithOut_Syn_2455_maf
        cos_indata3 = Exonic_PASS_NonSyn_2455_maf
        cos_indata4 = Exonic_PASS_FS_2455_maf
        cos_indata5 = Splicing_PASS_2455_maf
        cos_indata6 = Exonic_PASS_SGL_2455_maf

        def filtcos(data):
            if ((data.shape)[0] != 0):
                data = data[data['cosmicv89_coding'] == '.']
            else:
                print('')
            return data

        cos_indata1_syn_wcos = filtcos(cos_indata1)
        cos_indata2_wotsyn_wcos = filtcos(cos_indata2)
        cos_indata3_nonsyn_wcos = filtcos(cos_indata3)
        cos_indata4_fs_wcos = filtcos(cos_indata4)
        cos_indata5_spps_wcos = filtcos(cos_indata5)
        cos_indata6_sgl_wcos = filtcos(cos_indata6)

        cos_indata1_syn_wcos['Cosmic_SNP_Status'] = 'No Cosmic_ID'
        cos_indata2_wotsyn_wcos['Cosmic_SNP_Status'] = 'No Cosmic_ID'
        cos_indata3_nonsyn_wcos['Cosmic_SNP_Status'] = 'No Cosmic_ID'
        cos_indata4_fs_wcos['Cosmic_SNP_Status'] = 'No Cosmic_ID'
        cos_indata5_spps_wcos['Cosmic_SNP_Status'] = 'No Cosmic_ID'
        cos_indata6_sgl_wcos['Cosmic_SNP_Status'] = 'No Cosmic_ID'

        def writeYfun_wcos(data, pathname):
            writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
            data.to_excel(writer, index=False)
            writer.save()

        writeYfun_wcos(cos_indata1_syn_wcos, cosfilename1[12])
        writeYfun_wcos(cos_indata2_wotsyn_wcos, cosfilename2[12])
        writeYfun_wcos(cos_indata5_spps_wcos, cosfilename5[12])

        cos_indata1['Gene_Alias3'] = cos_indata1['Gene_Alias2']
        cos_indata2['Gene_Alias3'] = cos_indata2['Gene_Alias2']
        cos_indata3['Gene_Alias3'] = cos_indata3['Gene_Alias2']
        cos_indata4['Gene_Alias3'] = cos_indata4['Gene_Alias2']
        cos_indata5['Gene_Alias3'] = cos_indata5['Gene_Alias2']
        cos_indata6['Gene_Alias3'] = cos_indata6['Gene_Alias2']

        def rowsplitgene(genedata):
            if (genedata.shape[0] != 0):
                genedata = \
                    (genedata.set_index(genedata.columns.drop('Gene_Alias2', 1).tolist())
                         .Gene_Alias2.str.split(', ', expand=True)
                         .stack()
                         .reset_index()
                         .rename(columns={0: 'Gene_Alias2'})
                         .loc[:, genedata.columns]
                         )
            else:
                print('')
                genedata['Gene_Alias2'] = genedata['Gene_Alias2']
            return genedata

        cos_indata1 = rowsplitgene(cos_indata1)
        cos_indata2 = rowsplitgene(cos_indata2)
        cos_indata3 = rowsplitgene(cos_indata3)
        cos_indata4 = rowsplitgene(cos_indata4)
        cos_indata5 = rowsplitgene(cos_indata5)
        cos_indata6 = rowsplitgene(cos_indata6)

        # loading cosmic mutant file
        cosdata = pd.read_csv(cosdata, delimiter='\t', encoding='utf-8')
        print('cosmic data shape: ', cosdata.shape)

        # gene col split
        def colsplitcosdata(cosdata, col, sep):
            new = cosdata[col].str.split(sep, expand=True)
            cosdata['Gene_name1'] = new[0]
            return cosdata

        #cosdata = colsplitcosdata(cosdata, 'Gene name', "_")

        # variant col split
        def colsplitmutaa(cosdata, col, sep):
            new = cosdata[col].str.split(sep, expand=True)
            cosdata['Mutation_AA'] = new[1]
            return cosdata

        #cosdata = colsplitmutaa(cosdata, 'Mutation AA', "p.")
        print('cosmic data shape: ', cosdata.shape)

        cosdtacolist = list(cosdata)

        # merge function
        def cosmastmergefun(indata):
            # merg=pd.merge(indata,cosdata,left_on=['Gene.refGene','AAChange','cosmic_id'],right_on=['Gene_name1','Mutation_AA','Mutation ID'],how='inner')
            # merg = pd.merge(indata, cosdata, left_on=['Gene.refGene','cosmic_id'], right_on=['Gene_name1','Mutation ID'],how='inner')
            indata['Gene_Alias2'] = indata['Gene_Alias2'].astype(str)
            indata['cosmic_id'] = indata['cosmic_id'].astype(str)
            cosdata['Gene_name1'] = cosdata['Gene_name1'].astype(str)
            cosdata['Mutation ID'] = cosdata['Mutation ID'].astype(str)
            merg = pd.merge(indata, cosdata, left_on=['Gene_Alias2', 'cosmic_id'],
                            right_on=['Gene_name1', 'Mutation ID'],
                            how='inner')
            return merg

        cos_mstr_merg1 = cosmastmergefun(cos_indata1)
        cos_mstr_merg2 = cosmastmergefun(cos_indata2)
        cos_mstr_merg3 = cosmastmergefun(cos_indata3)
        cos_mstr_merg4 = cosmastmergefun(cos_indata4)
        cos_mstr_merg5 = cosmastmergefun(cos_indata5)
        cos_mstr_merg6 = cosmastmergefun(cos_indata6)

        cos_mstr_merg1 = cos_mstr_merg1.drop_duplicates()
        cos_mstr_merg2 = cos_mstr_merg2.drop_duplicates()
        cos_mstr_merg3 = cos_mstr_merg3.drop_duplicates()
        cos_mstr_merg4 = cos_mstr_merg4.drop_duplicates()
        cos_mstr_merg5 = cos_mstr_merg5.drop_duplicates()
        cos_mstr_merg6 = cos_mstr_merg6.drop_duplicates()

        def cosmicnotmatchfun(indata, mergedata):
            indata = indata.drop(['Gene_Alias2'], axis=1)
            mergedata = mergedata.drop(['Gene_Alias2'], axis=1)
            notmatchdata = indata.merge(mergedata, indicator=True, how='left').loc[lambda x: x['_merge'] != 'both']
            notmatchdata = notmatchdata.drop(['_merge'], axis=1)
            notmatchdata = notmatchdata.drop_duplicates()
            notmatchdata['Gene_Alias2'] = notmatchdata['Gene_Alias3']
            notmatchdata = notmatchdata.drop(['Gene_Alias3'], axis=1)
            notmatchdata = notmatchdata[notmatchdata['cosmicv89_coding'] != '.']
            notmatchdata['Cosmic_SNP_Status'] = 'Not matched data'
            notmatchdata = notmatchdata.drop(cosdtacolist, axis=1)
            return notmatchdata

        cos_notmatch_syn1 = cosmicnotmatchfun(cos_indata1, cos_mstr_merg1)
        cos_notmatch_wotsyn2 = cosmicnotmatchfun(cos_indata2, cos_mstr_merg2)
        cos_notmatch_nonsyn3 = cosmicnotmatchfun(cos_indata3, cos_mstr_merg3)
        cos_notmatch_fs4 = cosmicnotmatchfun(cos_indata4, cos_mstr_merg4)
        cos_notmatch_spps5 = cosmicnotmatchfun(cos_indata5, cos_mstr_merg5)
        cos_notmatch_sgl6 = cosmicnotmatchfun(cos_indata6, cos_mstr_merg6)

        def writeYfun_cosnm(data, pathname):
            writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
            data.to_excel(writer, index=False)
            writer.save()

        writeYfun_cosnm(cos_notmatch_syn1, cosfilename1[13])
        writeYfun_cosnm(cos_notmatch_wotsyn2, cosfilename2[13])
        writeYfun_cosnm(cos_notmatch_spps5, cosfilename5[13])

        def cosuvalfun(merge):
            shape = merge.shape
            ug = len(merge['Gene.refGene'].unique())
            uc = len(merge['cosmic_id'].unique())
            return [shape, ug, uc]

        cos_result1 = cosuvalfun(cos_mstr_merg1)
        cos_result2 = cosuvalfun(cos_mstr_merg2)
        cos_result3 = cosuvalfun(cos_mstr_merg3)
        cos_result4 = cosuvalfun(cos_mstr_merg4)
        cos_result5 = cosuvalfun(cos_mstr_merg5)
        cos_result6 = cosuvalfun(cos_mstr_merg6)

        cos_result_nm1 = cosuvalfun(cos_notmatch_syn1)
        cos_result_nm2 = cosuvalfun(cos_notmatch_wotsyn2)
        cos_result_nm3 = cosuvalfun(cos_notmatch_nonsyn3)
        cos_result_nm4 = cosuvalfun(cos_notmatch_fs4)
        cos_result_nm5 = cosuvalfun(cos_notmatch_spps5)
        cos_result_nm6 = cosuvalfun(cos_notmatch_sgl6)

        cos_result_syn_wcos1 = cosuvalfun(cos_indata1_syn_wcos)
        cos_result_wotsyn_wcos2 = cosuvalfun(cos_indata2_wotsyn_wcos)
        cos_result_nonsyn_wcos3 = cosuvalfun(cos_indata3_nonsyn_wcos)
        cos_result_fs_wcos4 = cosuvalfun(cos_indata4_fs_wcos)
        cos_result_spps_wcos5 = cosuvalfun(cos_indata5_spps_wcos)
        cos_result_sgl_wcos6 = cosuvalfun(cos_indata6_sgl_wcos)

        # FILTERING merge DATASET based on SNP
        def cosmergeYfiltfun(merg1):
            mergout = merg1[merg1['SNP'] == 'y']
            return mergout

        mergfiltY1 = cosmergeYfiltfun(cos_mstr_merg1)
        mergfiltY2 = cosmergeYfiltfun(cos_mstr_merg2)
        mergfiltY3 = cosmergeYfiltfun(cos_mstr_merg3)
        mergfiltY4 = cosmergeYfiltfun(cos_mstr_merg4)
        mergfiltY5 = cosmergeYfiltfun(cos_mstr_merg5)
        mergfiltY6 = cosmergeYfiltfun(cos_mstr_merg6)

        def cosmergeNfiltfun(merg1):
            mergout = merg1[merg1['SNP'] == 'n']
            return mergout

        mergfiltN1 = cosmergeNfiltfun(cos_mstr_merg1)
        mergfiltN2 = cosmergeNfiltfun(cos_mstr_merg2)
        mergfiltN3 = cosmergeNfiltfun(cos_mstr_merg3)
        mergfiltN4 = cosmergeNfiltfun(cos_mstr_merg4)
        mergfiltN5 = cosmergeNfiltfun(cos_mstr_merg5)
        mergfiltN6 = cosmergeNfiltfun(cos_mstr_merg6)

        def cosmergeBfiltfun(merg1):
            filtvalues = ['y', 'n']
            mergout = merg1[~merg1['SNP'].isin(filtvalues)]
            mergout['SNP'] = 'Blank'
            return mergout

        mergfiltB1 = cosmergeBfiltfun(cos_mstr_merg1)
        mergfiltB2 = cosmergeBfiltfun(cos_mstr_merg2)
        mergfiltB3 = cosmergeBfiltfun(cos_mstr_merg3)
        mergfiltB4 = cosmergeBfiltfun(cos_mstr_merg4)
        mergfiltB5 = cosmergeBfiltfun(cos_mstr_merg5)
        mergfiltB6 = cosmergeBfiltfun(cos_mstr_merg6)

        def cosmicuvalYfun(merge):
            shape = merge.shape
            ug = len(merge['Gene.refGene'].unique())
            uc = len(merge['cosmic_id'].unique())
            return [shape, ug, uc]

        resultY1 = cosmicuvalYfun(mergfiltY1)
        resultY2 = cosmicuvalYfun(mergfiltY2)
        resultY3 = cosmicuvalYfun(mergfiltY3)
        resultY4 = cosmicuvalYfun(mergfiltY4)
        resultY5 = cosmicuvalYfun(mergfiltY5)
        resultY6 = cosmicuvalYfun(mergfiltY6)

        resultN1 = cosmicuvalYfun(mergfiltN1)
        resultN2 = cosmicuvalYfun(mergfiltN2)
        resultN3 = cosmicuvalYfun(mergfiltN3)
        resultN4 = cosmicuvalYfun(mergfiltN4)
        resultN5 = cosmicuvalYfun(mergfiltN5)
        resultN6 = cosmicuvalYfun(mergfiltN6)

        resultB1 = cosmicuvalYfun(mergfiltB1)
        resultB2 = cosmicuvalYfun(mergfiltB2)
        resultB3 = cosmicuvalYfun(mergfiltB3)
        resultB4 = cosmicuvalYfun(mergfiltB4)
        resultB5 = cosmicuvalYfun(mergfiltB5)
        resultB6 = cosmicuvalYfun(mergfiltB6)

        def writeYNBfun(result, merge, pathname):
            fn = pathname.split('/')[-1]
            # new_names = [(i, 'Cosmic_' + i) for i in merge.iloc[:, -37:].columns.values]
            # merge.rename(columns=dict(new_names), inplace=True)
            if (result != 0):
                print('writing ', fn)
                writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
                merge.to_excel(writer, index=False)
                writer.save()
            else:
                print(fn + ' is empty dataframe')
                mergcol = list(merge)
                merge = merge.drop(mergcol, axis=1)
                merge['No_Matches_Found'] = ''  # DOUBT
                writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
                merge.to_excel(writer, index=False)
                writer.save()

        writeYNBfun(resultY1[0][0], mergfiltY1, cosfilename1[6])
        writeYNBfun(resultY2[0][0], mergfiltY2, cosfilename2[6])
        writeYNBfun(resultY5[0][0], mergfiltY5, cosfilename5[6])

        writeYNBfun(resultN1[0][0], mergfiltN1, cosfilename1[7])
        writeYNBfun(resultN2[0][0], mergfiltN2, cosfilename2[7])
        writeYNBfun(resultN5[0][0], mergfiltN5, cosfilename5[7])

        writeYNBfun(resultB1[0][0], mergfiltB1, cosfilename1[8])
        writeYNBfun(resultB2[0][0], mergfiltB2, cosfilename2[8])
        writeYNBfun(resultB5[0][0], mergfiltB5, cosfilename5[8])

        def dropcolfun(indata1):
            orginallst = list(cosdata)
            newlst = []
            for i in range(len(orginallst)):
                if (orginallst[i] != 'SNP'):
                    newlst.append(orginallst[i])
            indata1 = indata1.drop(newlst, axis=1)
            indata1 = indata1.drop_duplicates()
            print(list(indata1))
            indata1['Cosmic_SNP_Status'] = indata1['SNP']
            print(indata1['Cosmic_SNP_Status'])
            indata1["Cosmic_SNP_Status"] = indata1["Cosmic_SNP_Status"].replace('y', "Polymorphism")
            indata1["Cosmic_SNP_Status"] = indata1["Cosmic_SNP_Status"].replace('n', "Mutation")
            indata1 = indata1.drop('SNP', axis=1)
            return indata1

        mergfilt_newY1 = dropcolfun(mergfiltY1)
        mergfilt_newY2 = dropcolfun(mergfiltY2)
        mergfilt_newY3 = dropcolfun(mergfiltY3)
        mergfilt_newY4 = dropcolfun(mergfiltY4)
        mergfilt_newY5 = dropcolfun(mergfiltY5)
        mergfilt_newY6 = dropcolfun(mergfiltY6)

        mergfilt_newN1 = dropcolfun(mergfiltN1)
        mergfilt_newN2 = dropcolfun(mergfiltN2)
        mergfilt_newN3 = dropcolfun(mergfiltN3)
        mergfilt_newN4 = dropcolfun(mergfiltN4)
        mergfilt_newN5 = dropcolfun(mergfiltN5)
        mergfilt_newN6 = dropcolfun(mergfiltN6)

        def dropcolfunb(indata1):
            orginallst = list(cosdata)
            newlst = []
            for i in range(len(orginallst)):
                if (orginallst[i] != 'SNP'):
                    newlst.append(orginallst[i])
            indata1 = indata1.drop(newlst, axis=1)
            indata1 = indata1.drop_duplicates()
            fsflvl = ['frameshift deletion', 'nonframeshift deletion', 'nonframeshift insertion',
                      'frameshift insertion']

            indata_indel = indata1[indata1['ExonicFunc.refGene'].isin(fsflvl)]
            indata_indel["Cosmic_SNP_Status"] = 'Indel'

            indata_syn = indata1[indata1['ExonicFunc.refGene'] == 'synonymous SNV']
            indata_syn["Cosmic_SNP_Status"] = 'synonymous SNV Blank'

            indata_nonsyn = indata1[indata1['ExonicFunc.refGene'] == 'nonsynonymous SNV']
            indata_nonsyn["Cosmic_SNP_Status"] = 'nonsynonymous SNV Blank'

            indata_sg = indata1[indata1['ExonicFunc.refGene'] == 'stopgain']
            indata_sg["Cosmic_SNP_Status"] = 'stopgain Blank'

            indata_sl = indata1[indata1['ExonicFunc.refGene'] == 'stoploss']
            indata_sl["Cosmic_SNP_Status"] = 'stoploss Blank'

            indata_ukn = indata1[indata1['ExonicFunc.refGene'] == 'unknown']
            indata_ukn["Cosmic_SNP_Status"] = 'unknown Blank'

            indata1 = pd.concat([indata_indel, indata_syn, indata_nonsyn, indata_sg, indata_sl, indata_ukn], sort=False)
            indata1 = indata1.drop('SNP', axis=1)

            return indata1

        mergfilt_newB1 = dropcolfunb(mergfiltB1)
        mergfilt_newB2 = dropcolfunb(mergfiltB2)
        mergfilt_newB3 = dropcolfunb(mergfiltB3)
        mergfilt_newB4 = dropcolfunb(mergfiltB4)
        mergfilt_newB5 = dropcolfunb(mergfiltB5)
        mergfilt_newB6 = dropcolfunb(mergfiltB6)

        mergfilt_newY1 = mergfilt_newY1[mergfilt_newY1['fathmm-MKL_coding_pred'] == 'D']
        mergfilt_newY2 = mergfilt_newY2[mergfilt_newY2['fathmm-MKL_coding_pred'] == 'D']
        mergfilt_newY3 = mergfilt_newY3[mergfilt_newY3['fathmm-MKL_coding_pred'] == 'D']
        mergfilt_newY4 = mergfilt_newY4[mergfilt_newY4['fathmm-MKL_coding_pred'] == 'D']
        mergfilt_newY5 = mergfilt_newY5[mergfilt_newY5['fathmm-MKL_coding_pred'] == 'D']
        mergfilt_newY6 = mergfilt_newY6[mergfilt_newY6['fathmm-MKL_coding_pred'] == 'D']

        def cosmicuvalnewYnbfun(merge):
            shape = merge.shape
            ug = len(merge['Gene.refGene'].unique())
            uc = len(merge['cosmic_id'].unique())
            return [shape, ug, uc]

        newresultY1d = cosmicuvalnewYnbfun(mergfilt_newY1)
        newresultY2d = cosmicuvalnewYnbfun(mergfilt_newY2)
        newresultY3d = cosmicuvalnewYnbfun(mergfilt_newY3)
        newresultY4d = cosmicuvalnewYnbfun(mergfilt_newY4)
        newresultY5d = cosmicuvalnewYnbfun(mergfilt_newY5)
        newresultY6d = cosmicuvalnewYnbfun(mergfilt_newY6)

        newresultN1 = cosmicuvalnewYnbfun(mergfilt_newN1)
        newresultN2 = cosmicuvalnewYnbfun(mergfilt_newN2)
        newresultN3 = cosmicuvalnewYnbfun(mergfilt_newN3)
        newresultN4 = cosmicuvalnewYnbfun(mergfilt_newN4)
        newresultN5 = cosmicuvalnewYnbfun(mergfilt_newN5)
        newresultN6 = cosmicuvalnewYnbfun(mergfilt_newN6)

        newresultB1 = cosmicuvalnewYnbfun(mergfilt_newB1)
        newresultB2 = cosmicuvalnewYnbfun(mergfilt_newB2)
        newresultB3 = cosmicuvalnewYnbfun(mergfilt_newB3)
        newresultB4 = cosmicuvalnewYnbfun(mergfilt_newB4)
        newresultB5 = cosmicuvalnewYnbfun(mergfilt_newB5)
        newresultB6 = cosmicuvalnewYnbfun(mergfilt_newB6)

        def writenewYNBfun(result, merge, pathname):
            merge = merge.drop_duplicates()
            fn = pathname.split('/')[-1]
            if (result != 0):
                print('writing ', fn)
                writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
                merge.to_excel(writer, index=False)
                writer.save()
            else:
                print(fn + ' is empty dataframe')
                writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
                merge.to_excel(writer, index=False)
                writer.save()

        writenewYNBfun(resultY1[0][0], mergfilt_newY1, cosfilename1[9])
        writenewYNBfun(resultY2[0][0], mergfilt_newY2, cosfilename2[9])
        writenewYNBfun(resultY5[0][0], mergfilt_newY5, cosfilename5[9])

        writenewYNBfun(resultN1[0][0], mergfilt_newN1, cosfilename1[10])
        writenewYNBfun(resultN2[0][0], mergfilt_newN2, cosfilename2[10])
        writenewYNBfun(resultN5[0][0], mergfilt_newN5, cosfilename5[10])

        writenewYNBfun(resultB1[0][0], mergfilt_newB1, cosfilename1[11])
        writenewYNBfun(resultB2[0][0], mergfilt_newB2, cosfilename2[11])
        writenewYNBfun(resultB5[0][0], mergfilt_newB5, cosfilename5[11])

        filenamelist = [cosfilename1[0], cosfilename2[0], cosfilename3[0], cosfilename4[0], cosfilename5[0],
                        cosfilename6[0], '',
                        cosfilename1[1], cosfilename2[1], cosfilename3[1], cosfilename4[1], cosfilename5[1],
                        cosfilename6[1], '',
                        cosfilename1[2], cosfilename2[2], cosfilename3[2], cosfilename4[2], cosfilename5[2],
                        cosfilename6[2], '',
                        cosfilename1[3], cosfilename2[3], cosfilename3[3], cosfilename4[3], cosfilename5[3],
                        cosfilename6[3], '',
                        cosfilename1[4], cosfilename2[4], cosfilename3[4], cosfilename4[4], cosfilename5[4],
                        cosfilename6[4], '',
                        cosfilename1[5], cosfilename2[5], cosfilename3[5], cosfilename4[5], cosfilename5[5],
                        cosfilename6[5], '',
                        cosfilename1[14], cosfilename2[14], cosfilename3[14], cosfilename4[14], cosfilename5[14],
                        cosfilename6[14], '',
                        cosfilename1[15], cosfilename2[15], cosfilename3[15], cosfilename4[15], cosfilename5[15],
                        cosfilename6[15], '',
                        cosfilename1[16], cosfilename2[16], cosfilename3[16], cosfilename4[16], cosfilename5[16],
                        cosfilename6[16]]

        rowlist = [cos_result1[0][0], cos_result2[0][0], cos_result3[0][0], cos_result4[0][0], cos_result5[0][0],
                   cos_result6[0][0], '',
                   resultY1[0][0], resultY2[0][0], resultY3[0][0], resultY4[0][0], resultY5[0][0], resultY6[0][0], '',
                   resultN1[0][0], resultN2[0][0], resultN3[0][0], resultN4[0][0], resultN5[0][0], resultN6[0][0], '',
                   resultB1[0][0], resultB2[0][0], resultB3[0][0], resultB4[0][0], resultB5[0][0], resultB6[0][0], '',
                   cos_result_syn_wcos1[0][0], cos_result_wotsyn_wcos2[0][0], cos_result_nonsyn_wcos3[0][0],
                   cos_result_fs_wcos4[0][0], cos_result_spps_wcos5[0][0], cos_result_sgl_wcos6[0][0], '',
                   cos_result_nm1[0][0], cos_result_nm2[0][0], cos_result_nm3[0][0], cos_result_nm4[0][0],
                   cos_result_nm5[0][0], cos_result_nm6[0][0], '',
                   newresultY1d[0][0], newresultY2d[0][0], newresultY3d[0][0], newresultY4d[0][0], newresultY5d[0][0],
                   newresultY6d[0][0], '',
                   newresultN1[0][0], newresultN2[0][0], newresultN3[0][0], newresultN4[0][0], newresultN5[0][0],
                   newresultN6[0][0], '',
                   newresultB1[0][0], newresultB2[0][0], newresultB3[0][0], newresultB4[0][0], newresultB5[0][0],
                   newresultB6[0][0]]

        collist = [cos_result1[0][1], cos_result2[0][1], cos_result3[0][1], cos_result4[0][1], cos_result5[0][1],
                   cos_result6[0][1], '',
                   resultY1[0][1], resultY2[0][1], resultY3[0][1], resultY4[0][1], resultY5[0][1], resultY6[0][1], '',
                   resultN1[0][1], resultN2[0][1], resultN3[0][1], resultN4[0][1], resultN5[0][1], resultN6[0][1], '',
                   resultB1[0][1], resultB2[0][1], resultB3[0][1], resultB4[0][1], resultB5[0][1], resultB6[0][1], '',
                   cos_result_syn_wcos1[0][1], cos_result_wotsyn_wcos2[0][1], cos_result_nonsyn_wcos3[0][1],
                   cos_result_fs_wcos4[0][1], cos_result_spps_wcos5[0][1], cos_result_sgl_wcos6[0][1], '',
                   cos_result_nm1[0][1], cos_result_nm2[0][1], cos_result_nm3[0][1], cos_result_nm4[0][1],
                   cos_result_nm5[0][1], cos_result_nm6[0][1], '',
                   newresultY1d[0][1], newresultY2d[0][1], newresultY3d[0][1], newresultY4d[0][1], newresultY5d[0][1],
                   newresultY6d[0][1], '',
                   newresultN1[0][1], newresultN2[0][1], newresultN3[0][1], newresultN4[0][1], newresultN5[0][1],
                   newresultN6[0][1], '',
                   newresultB1[0][1], newresultB2[0][1], newresultB3[0][1], newresultB4[0][1], newresultB5[0][1],
                   newresultB6[0][1]]

        genelist = [cos_result1[1], cos_result2[1], cos_result3[1], cos_result4[1], cos_result5[1], cos_result6[1], '',
                    resultY1[1], resultY2[1], resultY3[1], resultY4[1], resultY5[1], resultY6[1], '',
                    resultN1[1], resultN2[1], resultN3[1], resultN4[1], resultN5[1], resultN6[1], '',
                    resultB1[1], resultB2[1], resultB3[1], resultB4[1], resultB5[1], resultB6[1], '',
                    cos_result_syn_wcos1[1], cos_result_wotsyn_wcos2[1], cos_result_nonsyn_wcos3[1],
                    cos_result_fs_wcos4[1],
                    cos_result_spps_wcos5[1], cos_result_sgl_wcos6[1], '',
                    cos_result_nm1[1], cos_result_nm2[1], cos_result_nm3[1], cos_result_nm4[1], cos_result_nm5[1],
                    cos_result_nm6[1], '',
                    newresultY1d[1], newresultY2d[1], newresultY3d[1], newresultY4d[1], newresultY5d[1],
                    newresultY6d[1],
                    '',
                    newresultN1[1], newresultN2[1], newresultN3[1], newresultN4[1], newresultN5[1], newresultN6[1], '',
                    newresultB1[1], newresultB2[1], newresultB3[1], newresultB4[1], newresultB5[1], newresultB6[1]]

        cosidlist = [cos_result1[2], cos_result2[2], cos_result3[2], cos_result4[2], cos_result5[2], cos_result6[2], '',
                     resultY1[2], resultY2[2], resultY3[2], resultY4[2], resultY5[2], resultY6[2], '',
                     resultN1[2], resultN2[2], resultN3[2], resultN4[2], resultN5[2], resultN6[2], '',
                     resultB1[2], resultB2[2], resultB3[2], resultB4[2], resultB5[2], resultB6[2], '',
                     cos_result_syn_wcos1[2], cos_result_wotsyn_wcos2[2], cos_result_nonsyn_wcos3[2],
                     cos_result_fs_wcos4[2], cos_result_spps_wcos5[2], cos_result_sgl_wcos6[2], '',
                     cos_result_nm1[2], cos_result_nm2[2], cos_result_nm3[2], cos_result_nm4[2], cos_result_nm5[2],
                     cos_result_nm6[2], '',
                     newresultY1d[2], newresultY2d[2], newresultY3d[2], newresultY4d[2], newresultY5d[2],
                     newresultY6d[2],
                     '',
                     newresultN1[2], newresultN2[2], newresultN3[2], newresultN4[2], newresultN5[2], newresultN6[2], '',
                     newresultB1[2], newresultB2[2], newresultB3[2], newresultB4[2], newresultB5[2], newresultB6[2]]

        cosshapedf = pd.DataFrame(
            {'Filename': filenamelist,
             'No.of.rows': rowlist,
             'No.of.columns': collist,
             'Unique_Gene': genelist,
             'Unique_Cosmic_ID': cosidlist
             })

        writer = pd.ExcelWriter(cosshapepn, engine='xlsxwriter')
        cosshapedf.to_excel(writer, index=False)  # output1
        writer.save()

        print("---cosmic_match took %s seconds to complete---" % (time.time() - start_time))
        print('cosmic_match completed')

        # FOR_LIST_CONCEPT
        print('For_list started')
        try:
            os.makedirs(dirName_Cosmic_Forlist_Report, mode=0o777)
            os.makedirs(dirName19, mode=0o777)
            print("Directory ", dirName19, " Created ")
        except FileExistsError:
            print("Directory ", dirName19, " already exists")

        fsflvl = ['frameshift deletion', 'nonframeshift deletion', 'nonframeshift insertion', 'frameshift insertion']
        snvflvl = ['synonymous SNV', 'nonsynonymous SNV', 'stopgain', 'stoploss']

        bdata = mergfiltN2[mergfiltN2['ExonicFunc.refGene'].isin(fsflvl)]
        b2data = mergfiltB2[mergfiltB2['ExonicFunc.refGene'].isin(fsflvl)]
        b_indeldata = bdata.append(b2data, sort=False)

        b_data_wocos = cos_indata2_wotsyn_wcos[cos_indata2_wotsyn_wcos['ExonicFunc.refGene'].isin(fsflvl)]
        n_data_wocos = cos_indata2_wotsyn_wcos[cos_indata2_wotsyn_wcos['ExonicFunc.refGene'].isin(snvflvl)]

        snvdata = mergfiltN2[mergfiltN2['ExonicFunc.refGene'].isin(snvflvl)]
        snv2data = mergfiltB2[mergfiltB2['ExonicFunc.refGene'].isin(snvflvl)]
        n_snv = snvdata.append(snv2data, sort=False)

        def forlistfilename(filename, data):
            outfile1name = filename + '_FOR_LIST'
            nwocosname = filename + '_N_FOR_LIST'
            bwocosname = filename + '_B_FOR_LIST'
            pathname1 = dirName19 + '/' + outfile1name + '.xlsx'
            pathname2 = dirName19 + '/' + outfile1name + '.xlsx'
            pathname3nwocos = dirName19 + '/' + nwocosname + '.xlsx'
            pathname4bwocos = dirName19 + '/' + bwocosname + '.xlsx'
            datashape = data.shape
            report_flename = dirName_Cosmic_Forlist_Report + '/' + outfile1name + '_Report' + '.xlsx'
            return [outfile1name, pathname1, datashape, report_flename, pathname2, nwocosname, bwocosname,
                    pathname3nwocos,
                    pathname4bwocos]

        forlstname1 = forlistfilename(cosfilename2[2], n_snv)
        forlstname2 = forlistfilename(cosfilename2[3], b_indeldata)
        yumname = forlistfilename(cosfilename2[1], mergfiltY2)
        nwocosforlstname1 = forlistfilename(cosfilename2[4], n_data_wocos)
        bwocosforlstname2 = forlistfilename(cosfilename2[4], b_data_wocos)

        def forlistwritefun(indata, pathname):
            fn = pathname.split('/')[-1]
            print('writing ', fn)
            writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
            indata.to_excel(writer, index=False)
            writer.save()

        forlistwritefun(n_snv, forlstname1[1])
        forlistwritefun(b_indeldata, forlstname2[1])
        forlistwritefun(mergfiltY2, yumname[4])
        forlistwritefun(n_data_wocos, nwocosforlstname1[7])
        forlistwritefun(b_data_wocos, bwocosforlstname2[8])

        # forlist_report_process
        def flcuration(result, indata):
            # drop_columns
            orginallst = list(indata)
            keeplst = ['Chr', 'Start', 'End', 'Ref', 'Alt', 'Gene.refGene', 'AAChange', 'fathmm-MKL_coding_score',
                       'AAChange_CDS', 'cosmic_id']

            def diff(l1, l2):
                return (list(set(l1) - set(l2)))

            droplst = diff(orginallst, keeplst)
            indata = indata.drop(droplst, axis=1)
            return indata

        forlist_report_n = flcuration(forlstname1[2][0], n_snv)
        forlist_report_b = flcuration(forlstname2[2][0], b_indeldata)
        forlist_report_nwocos = flcuration(nwocosforlstname1[2][0], n_data_wocos)
        forlist_report_bwocos = flcuration(bwocosforlstname2[2][0], b_data_wocos)

        def curateForList_N_B(data):
            data = data.drop_duplicates(keep='first')
            data['RefCol'] = data['Chr'].astype(str) + data['Start'].astype(str) + data['End'].astype(str) + data[
                'Ref'].astype(str) + \
                             data['Gene.refGene'].astype(str)
            data['RefColCount'] = np.where(data['RefCol'].duplicated(keep=False),
                                           data.groupby('RefCol').cumcount().add(1).astype(str),
                                           "0")
            data1 = data.groupby(['RefCol'])['RefColCount'].max().reset_index()
            merged = data.merge(data1, on=["RefColCount", "RefCol"])
            merged = merged.drop(["RefColCount", "RefCol"], axis=1)
            return merged

        def curateForList_N_B_dropCols(data):
            if 'fathmm-MKL_coding_score' in data.columns:
                data = data.drop(
                    ['Chr', 'Start', 'End', 'Ref', 'Alt', 'cosmic_id', 'Report_Decision', 'fathmm-MKL_coding_score'],
                    axis=1)
            else:
                data = data.drop(['Chr', 'Start', 'End', 'Ref', 'Alt', 'cosmic_id', 'Report_Decision'], axis=1)
            data = data.rename(columns={"AAChange_CDS": "CDS"})
            return data

        def fpforlstn(data):
            data = data[data['fathmm-MKL_coding_score'] != '.']
            data = data[data['fathmm-MKL_coding_score'] != 0]
            data = data.drop_duplicates()
            col = list(data)
            data = data[[col for col in data.columns if col != 'cosmic_id'] + ['cosmic_id']]
            data['Report_Decision'] = ''
            return data

        forlist_report_n = fpforlstn(forlist_report_n)
        forlist_report_nwocos = fpforlstn(forlist_report_nwocos)

        def fpforlstb(data):
            data = data.drop('fathmm-MKL_coding_score', axis=1)
            data = data.drop_duplicates()
            col = list(data)
            data = data[[col for col in data.columns if col != 'cosmic_id'] + ['cosmic_id']]
            data['Report_Decision'] = ''
            return data

        forlist_report_b = fpforlstb(forlist_report_b)
        forlist_report_bwocos = fpforlstb(forlist_report_bwocos)

        forlist_report_n = pd.concat([forlist_report_n, forlist_report_nwocos], sort=False)
        forlist_report_b = pd.concat([forlist_report_b, forlist_report_bwocos], sort=False)

        forlist_report_n_dup_rem = curateForList_N_B(forlist_report_n)
        forlist_report_b_dup_rem = curateForList_N_B(forlist_report_b)

        forlist_report_n_rem_col = curateForList_N_B_dropCols(forlist_report_n_dup_rem)
        forlist_report_b_rem_col = curateForList_N_B_dropCols(forlist_report_b_dup_rem)

        def cgcwritefun2(merge, dup_rem, drop_col, pathname):
            fn = pathname.split('/')[-1]
            print('writing ', fn)
            writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
            merge.to_excel(writer, index=False, sheet_name="Source")
            dup_rem.to_excel(writer, index=False, sheet_name="Duplicates Removed")
            drop_col.to_excel(writer, index=False, sheet_name="Cols Sorted")
            writer.save()

        cgcwritefun2(forlist_report_n, forlist_report_n_dup_rem, forlist_report_n_rem_col, forlstname1[3])
        cgcwritefun2(forlist_report_b, forlist_report_b_dup_rem, forlist_report_b_rem_col, forlstname2[3])

        print("---for_list took %s seconds to complete---" % (time.time() - start_time))
        print('for_list completed')
        # CGC_match
        if (cgcdata == ''):
            print('CGC_match will not done')
        else:
            print('CGC_match started')
            try:
                os.makedirs(dirName6, mode=0o777)
                os.makedirs(dirName_cgcReport, mode=0o777)
                print("Directory ", dirName6, " Created ")
            except FileExistsError:
                print("Directory ", dirName6, " already exists")

            def cgcfinalfilename(filename):
                filename1 = filename + '_CGC'
                filename2 = filename + '_WO_Cosid_CGC'
                pathname = dirName6 + '/' + filename1 + '.xlsx'
                pathname2 = dirName6 + '/' + filename2 + '.xlsx'
                return [filename1, pathname, filename2, pathname2]

            cgcfn1 = cgcfinalfilename(finalname_EESP_NSFSSGL4)
            cgcfn2 = cgcfinalfilename(cosfilename2[1])
            cgcfn3 = cgcfinalfilename(forlstname1[0])
            cgcfn4 = cgcfinalfilename(forlstname2[0])

            def cgc_report_filename(filename):
                filename = filename + '_report'
                pathname = dirName_cgcReport + '/' + filename + '.xlsx'
                return [filename, pathname]

            cgc_report_eesp_fn1 = cgc_report_filename(cgcfn1[2])
            cgc_report_fn1 = cgc_report_filename(cgcfn3[0])
            cgc_report_fn2 = cgc_report_filename(cgcfn4[0])

            cgcvar1 = finalname_EESP_NSFSSGL4.split('_')[0]
            cgcshapename = cgcvar1 + '_CGC_MATCH_Shapes'
            cgcout2filename = finalname_EESP_NSFSSGL4 + '_UCGC'
            cgcout3filename = finalname_EESP_NSFSSGL4 + '_UCGC_splitted'

            cgcinput1 = Exonic_PASS_WithOut_Syn_2455
            cgcinput1_wcosid = cgcinput1[cgcinput1['cosmicv89_coding'] == '.']

            # cgcdata
            cgcdata = pd.read_csv(cgcdata, header=0)
            print('CGC data shape: ', cgcdata.shape)

            def cgcmergefun(indata):
                merg = pd.merge(indata, cgcdata, left_on=['Gene.refGene'], right_on=['Gene Symbol'], how='inner')
                return merg

            cgcout1 = cgcmergefun(cgcinput1)
            cgcout1_wcosid = cgcmergefun(cgcinput1_wcosid)
            cgcout2 = cgcmergefun(mergfiltY2)
            cgcout3 = cgcmergefun(n_snv)
            cgcout4 = cgcmergefun(b_indeldata)

            def cgcuvalfun(merge):
                shape = merge.shape
                ug_val = merge['Gene.refGene'].unique()
                ug_len = len(merge['Gene.refGene'].unique())
                return [shape, ug_val, ug_len]

            cgcresult1 = cgcuvalfun(cgcout1)
            cgcresult1_wcosid = cgcuvalfun(cgcout1_wcosid)
            cgcresult2 = cgcuvalfun(cgcout2)
            cgcresult3 = cgcuvalfun(cgcout3)
            cgcresult4 = cgcuvalfun(cgcout4)

            def cgcwritefun(result, merge, pathname):
                fn = pathname.split('/')[-1]
                print('writing ', fn)
                if (result != 0):
                    writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
                    merge.to_excel(writer, index=False)
                    writer.save()
                else:
                    print(fn + ' is empty dataframe')
                    merge = merge.drop(merge, axis=1)
                    merge['No_Matches_Found'] = ''
                    writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
                    merge.to_excel(writer, index=False)
                    writer.save()

            cgcwritefun(cgcresult1[0][0], cgcout1, cgcfn1[1])
            cgcwritefun(cgcresult1_wcosid[0][0], cgcout1_wcosid, cgcfn1[3])
            cgcwritefun(cgcresult2[0][0], cgcout2, cgcfn2[1])
            cgcwritefun(cgcresult3[0][0], cgcout3, cgcfn3[1])
            cgcwritefun(cgcresult4[0][0], cgcout4, cgcfn4[1])

            # cgc forlist_report_process
            def cgcflcuration(result, indata):
                # drop_columns
                orginallst = list(indata)

                keeplst = ['Chr', 'Start', 'End', 'Ref', 'Alt', 'fathmm-MKL_coding_pred', 'Gene.refGene', 'AAChange',
                           'AAChange_CDS', 'cosmic_id', 'fathmm-MKL_coding_score', 'Primary site', 'AF_VAF']

                def diff(l1, l2):
                    return (list(set(l1) - set(l2)))

                droplst = diff(orginallst, keeplst)
                indata = indata.drop(droplst, axis=1)

                cols = list(indata)
                cols.insert(6, cols.pop(cols.index('AAChange')))
                indata = indata.loc[:, cols]

                return indata

            forlistcgc_report_n = cgcflcuration(cgcresult3[0][0], cgcout3)
            forlistcgc_report_b = cgcflcuration(cgcresult4[0][0], cgcout4)
            eesp_cgc_report = cgcflcuration(cgcresult1_wcosid[0][0], cgcout1_wcosid)

            # filter process
            forlistcgc_report_n = forlistcgc_report_n[forlistcgc_report_n['fathmm-MKL_coding_score'] != '.']
            forlistcgc_report_n = forlistcgc_report_n[forlistcgc_report_n['fathmm-MKL_coding_score'] != 0]
            forlistcgc_report_n = forlistcgc_report_n.drop_duplicates()
            col = list(forlistcgc_report_n)
            forlistcgc_report_n = forlistcgc_report_n[
                [col for col in forlistcgc_report_n.columns if col != 'cosmic_id'] + ['cosmic_id']]
            forlistcgc_report_n['Report_Decision'] = ''

            eesp_cgc_report = eesp_cgc_report[eesp_cgc_report['fathmm-MKL_coding_score'] != '.']
            eesp_cgc_report = eesp_cgc_report[eesp_cgc_report['fathmm-MKL_coding_score'] != 0]
            eesp_cgc_report = eesp_cgc_report.drop_duplicates()
            col = list(eesp_cgc_report)
            eesp_cgc_report = eesp_cgc_report[
                [col for col in eesp_cgc_report.columns if col != 'cosmic_id'] + ['cosmic_id']]
            eesp_cgc_report['Report_Decision'] = ''

            # drop column
            forlistcgc_report_b = forlistcgc_report_b.drop('fathmm-MKL_coding_score', axis=1)
            forlistcgc_report_b = forlistcgc_report_b.drop_duplicates()
            col = list(forlistcgc_report_b)
            forlistcgc_report_b = forlistcgc_report_b[
                [col for col in forlistcgc_report_b.columns if col != 'cosmic_id'] + ['cosmic_id']]
            forlistcgc_report_b['Report_Decision'] = ''

            def cgcwritefun2(merge, pathname):
                fn = pathname.split('/')[-1]
                print('writing ', fn)
                writer = pd.ExcelWriter(pathname, engine='xlsxwriter')
                merge.to_excel(writer, index=False)
                writer.save()

            cgcwritefun2(forlistcgc_report_n, cgc_report_fn1[1])
            cgcwritefun2(forlistcgc_report_b, cgc_report_fn2[1])
            cgcwritefun2(eesp_cgc_report, cgc_report_eesp_fn1[1])

            filenamelist = [cgcfn1[0], cgcfn1[2], cgcfn2[0], cgcfn3[0], cgcfn4[0]]
            rowlist = [cgcresult1[0][0], cgcresult1_wcosid[0][0], cgcresult2[0][0], cgcresult3[0][0], cgcresult4[0][0]]
            collist = [cgcresult1[0][1], cgcresult1_wcosid[0][1], cgcresult2[0][1], cgcresult3[0][1], cgcresult4[0][1]]
            genelist = [cgcresult1[2], cgcresult1_wcosid[2], cgcresult2[2], cgcresult3[2], cgcresult4[2]]

            cgcshapedf = pd.DataFrame(
                {'Filename': filenamelist,
                 'No of rows': rowlist,
                 'No of columns': collist,
                 'Unique_Gene': genelist
                 })
            writer = pd.ExcelWriter(dirName6 + '/' + cgcshapename + '.xlsx', engine='xlsxwriter')
            cgcshapedf.to_excel(writer, index=False)  # output1
            writer.save()
            print("---CGC_match took %s seconds to complete---" % (time.time() - start_time))
            print('CGC_match completed')

    # dbMATCH
    # NEW db MATCH FORMAT
    if (dbdata == ''):
        print('Database match will not done')
    else:
        print('Database match Started')
        try:
            os.makedirs(dirName21, mode=0o777)
            os.makedirs(dirName_fdaReport, mode=0o777)
            print("Directory ", dirName21, " Created ")
            print("Directory ", dirName_fdaReport, " Created ")
        except FileExistsError:
            print("Directory ", dirName21, " already exists")
            print("Directory ", dirName_fdaReport, " already exists")

        newcvc_indata_syn_y1 = mergfilt_newY1
        newcvc_indata_syn_n1 = mergfilt_newN1
        newcvc_indata_syn_b1 = mergfilt_newB1
        newcvc_indata_syn_wc1 = cos_indata1_syn_wcos
        newcvc_indata_syn_nm1 = cos_notmatch_syn1
        newcvc_indata_wosyn_y2 = mergfilt_newY2
        newcvc_indata_wosyn_n2 = mergfilt_newN2
        newcvc_indata_wosyn_b2 = mergfilt_newB2
        newcvc_indata_wosyn_wc2 = cos_indata2_wotsyn_wcos
        newcvc_indata_wosyn_nm2 = cos_notmatch_wotsyn2

        indata_dbinput = pd.concat(
            [newcvc_indata_syn_y1, newcvc_indata_syn_n1, newcvc_indata_syn_b1, newcvc_indata_syn_wc1,
             newcvc_indata_syn_nm1,
             newcvc_indata_wosyn_y2, newcvc_indata_wosyn_n2, newcvc_indata_wosyn_b2, newcvc_indata_wosyn_wc2,
             newcvc_indata_wosyn_nm2], sort=False)

        # # Msk_tumor supressor genes
        # msk_GENES = pd.read_excel(io=dbdata, sheet_name='MSK-Genes')
        # msk_tumsupgene_merg = pd.merge(indata_dbinput, msk_GENES, left_on=['Gene.refGene'], right_on=['Hugo Symbol'],
        #                                how='inner')
        # msk_tumsupgene_merg = msk_tumsupgene_merg.drop_duplicates()

        # MSK_MATCH
        # MSK_ACTIONABLE
        dbdata_snv = pd.read_excel(io=dbdata, sheet_name='SNVNFSFS')
        # mskdata_Act2 = pd.read_excel(io=dbdata, sheet_name='Actionable_December2019')
        # mskdata_csv = pd.read_excel(io=dbdata, sheet_name='Clinical Sig_August2019')

        # MSKmerg1_GENE_ACT1 = pd.merge(indata_dbinput, dbdata_snv, left_on=['Gene.refGene'], right_on=['Hugo Symbol'],
        #                               how='inner')
        # MSKmerg1_GENE_ACT1 = MSKmerg1_GENE_ACT1.drop_duplicates()
        #
        # MSKmerg1_GENE_ACT = MSKmerg1_GENE_ACT1

        ptdatacollist = list(indata_dbinput)

        def gvnotexonmacthfun(ptdata, data, ptgenecol, ptaacol, datagenecol, datapvcol, dataexoncol, matchdatacollist):
            if (data.shape[0] != 0):
                data_exon = data[data[dataexoncol].notnull()]
                data_notexon = data.merge(data_exon, indicator=True, how='left').loc[lambda x: x['_merge'] != 'both']
                data_notexon = data_notexon.drop(['_merge'], axis=1)

                ptdata[ptgenecol] = ptdata[ptgenecol].astype(str)
                ptdata[ptaacol] = ptdata[ptaacol].astype(str)

                data_notexon[datagenecol] = data_notexon[datagenecol].astype(str)
                data_notexon[datapvcol] = data_notexon[datapvcol].astype(str)
                # data_notexon[dataexoncol]=data_notexon[dataexoncol].astype(str)

                # Common match without checking anything
                merg_all = pd.merge(ptdata, data_notexon, left_on=[ptgenecol, ptaacol],
                                    right_on=[datagenecol, datapvcol],
                                    how='inner')

                # genematch
                uniquegens = data_notexon[datagenecol].unique()
                data_uniquegens = data_notexon[data_notexon[datapvcol].isin(uniquegens)]
                merg_uniquegens = pd.merge(ptdata, data_uniquegens, left_on=[ptgenecol], right_on=[datagenecol],
                                           how='inner')

                # MEHOD1(JANYU)
                data_JANYU1 = data_notexon[data_notexon[datapvcol].str.contains('JANYU', na=False)]
                merg_JANYU1 = pd.merge(ptdata, data_JANYU1, left_on=[ptgenecol], right_on=[datagenecol], how='inner')

                # METHOD2(V561U)
                uformat = data_notexon[data_notexon[datapvcol].str.endswith('U', na=False)]
                Uformat2 = uformat[~uformat[datapvcol].str.contains('J', na=False)]
                Uformat2['Pseudo Variant1'] = Uformat2[datapvcol].map(lambda x: str(x)[:-1])
                ptdata['AAChange1'] = ptdata[ptaacol].map(lambda x: str(x)[:-1])
                merg_Uformat2 = pd.merge(ptdata, Uformat2, left_on=[ptgenecol, 'AAChange1'],
                                         right_on=[datagenecol, 'Pseudo Variant1'], how='inner')

                # METHOD3(J61U)
                juformat = data_notexon[data_notexon[datapvcol].str.contains('J', na=False)]
                juformat = juformat[~juformat[datapvcol].str.endswith('U', na=False)]
                jnumuformat = juformat[~juformat[datapvcol].str.contains('ANY', na=False)]
                jnumuformat['pvlastremove'] = jnumuformat[datapvcol].map(lambda x: str(x)[:-1])
                jnumuformat['pvnum'] = jnumuformat['pvlastremove'].map(lambda x: str(x)[1:])
                ptdata['AAChangenum'] = ptdata['AAChange1'].map(lambda x: str(x)[1:])
                merg_jnumuformat3 = pd.merge(ptdata, jnumuformat, left_on=[ptgenecol, 'AAChangenum'],
                                             right_on=[datagenecol, 'pvnum'], how='inner')

                # method4(DANYV)(EanyX)
                anyformat = data_notexon[data_notexon[datapvcol].str.contains('ANY', na=False)]
                anyformat = anyformat[~anyformat[datapvcol].str.contains('J', na=False)]
                splitany = anyformat[datapvcol].str.split('ANY', expand=True)
                if (splitany.shape[0] != 0):
                    anyformat['PV1'] = splitany[0]
                    anyformat['PV2'] = splitany[1]
                else:
                    anyformat['PV1'] = anyformat[datapvcol]
                    anyformat['PV2'] = anyformat[datapvcol]
                ptdata['AAChange_char1'] = [x[0] if isinstance(x, str) else np.nan for x in ptdata[ptaacol]]
                ptdata['AAChange_char2'] = [x[-1] if isinstance(x, str) else np.nan for x in ptdata[ptaacol]]
                merg_anyformat4 = pd.merge(ptdata, anyformat, left_on=[ptgenecol, 'AAChange_char1', 'AAChange_char2'],
                                           right_on=[datagenecol, 'PV1', 'PV2'], how='inner')

                # method5(JANYUfs)
                JANYUfs_format = data_notexon[data_notexon[datapvcol].str.contains('JANYUfs', na=False)]
                ptdata_fs = ptdata[ptdata[ptaacol].str.endswith('fs', na=False)]
                merg_JANYUfs5 = pd.merge(ptdata_fs, JANYUfs_format, left_on=[ptgenecol], right_on=[datagenecol],
                                         how='inner')

                # method6(J281fs)
                Jnumfs_format = data_notexon[data_notexon[datapvcol].str.contains('J', na=False)]
                Jnumfs_format = Jnumfs_format[Jnumfs_format[datapvcol].str.endswith('fs', na=False)]
                filtvaljfs = ['JANYUfs', 'JANYUfs*any', 'JANYU']
                Jnumfs_format = Jnumfs_format[~Jnumfs_format[datapvcol].isin(filtvaljfs)]
                Jnumfs_format['PVNUM1'] = Jnumfs_format[datapvcol].map(lambda x: str(x)[:-2])
                Jnumfs_format['PVNUM1'] = Jnumfs_format['PVNUM1'].map(lambda x: str(x)[1:])
                ptdata_fs['AACh1'] = ptdata_fs[ptaacol].map(lambda x: str(x)[:-2])
                ptdata_fs['AACh1'] = ptdata_fs['AACh1'].map(lambda x: str(x)[1:])
                merg_Jnumfs6 = pd.merge(ptdata_fs, Jnumfs_format, left_on=[ptgenecol, 'AACh1'],
                                        right_on=[datagenecol, 'PVNUM1'], how='inner')

                # Method7(J58Ufs)
                JnumUfs_format = Jnumfs_format[Jnumfs_format[datapvcol].str.contains('U', na=False)]
                JnumUfs_format['PVNUM1'] = JnumUfs_format[datapvcol].map(lambda x: str(x)[:-3])
                JnumUfs_format['PVNUM1'] = JnumUfs_format['PVNUM1'].map(lambda x: str(x)[1:])
                ptdata_fs['AACh1'] = ptdata_fs[ptaacol].map(lambda x: str(x)[:-3])
                ptdata_fs['AACh1'] = ptdata_fs['AACh1'].map(lambda x: str(x)[1:])
                merg_JnumUfs7 = pd.merge(ptdata_fs, JnumUfs_format, left_on=[ptgenecol, 'AACh1'],
                                         right_on=[datagenecol, 'PVNUM1'], how='inner')

                # Method8(M1FS*ANY)
                endstarany_format = data_notexon[data_notexon[datapvcol].str.endswith('*ANY', na=False)]
                splitendstarany = endstarany_format[datapvcol].str.split('*', expand=True)
                if (splitendstarany.shape[0] != 0):
                    endstarany_format['PVdata'] = splitendstarany[0]
                else:
                    endstarany_format['PVdata'] = endstarany_format[datapvcol]
                ptdatafsstar = ptdata[ptdata[ptaacol].str.contains('fs*', na=False)]
                ptdatafsstar_splitstar = ptdatafsstar[ptaacol].str.split('*', expand=True)
                if (ptdatafsstar_splitstar.shape[0] != 0):
                    ptdatafsstar['AAChangefs'] = ptdatafsstar_splitstar[0]
                else:
                    ptdatafsstar['AAChangefs'] = ptdatafsstar[ptaacol]
                merg_endstarany_format8 = pd.merge(ptdatafsstar, endstarany_format, left_on=[ptgenecol, 'AAChangefs'],
                                                   right_on=[datagenecol, 'PVdata'], how='inner')

                # Method9(JanyUfs*any)
                JANYUfsstarany_format = data_notexon[data_notexon[datapvcol] == 'JANYUfs*ANY']
                indataendfsstr = ptdatafsstar[ptdatafsstar[ptaacol].str.endswith('fs*', na=False)]
                uniendfsstr = indataendfsstr[ptaacol].unique()
                indatafsstarany = ptdatafsstar[~ptdatafsstar[ptaacol].isin(uniendfsstr)]
                merg_JANYUfsstarany9 = pd.merge(indatafsstarany, JANYUfsstarany_format, left_on=[ptgenecol],
                                                right_on=[datagenecol], how='inner')

                # METHOD10 (JANYX)
                janyx_format = data_notexon[data_notexon[datapvcol] == 'JANYX']
                indata_endx = ptdata[ptdata[ptaacol].str.endswith('X', na=False)]
                merge_janyx10 = pd.merge(indata_endx, janyx_format, left_on=[ptgenecol], right_on=[datagenecol],
                                         how='inner')

                # METHOD11(c.1934dupG)
                CDS_format = data_notexon[data_notexon[datapvcol].str.contains('c.', na=False)]
                CDS_format['PVcds'] = CDS_format[datapvcol].map(lambda x: str(x)[2:])
                merg_cds11 = pd.merge(ptdata, CDS_format, left_on=[ptgenecol, 'AAChange_CDS'],
                                      right_on=[datagenecol, 'PVcds'], how='inner')

                # METHOD12(V600E+V600M+etc upto 5 compound mutation)
                def plusFilter(string, substr):
                    return [str for str in string if any(sub in str for sub in substr)]

                substr = ['+']
                plusvariants = plusFilter(data_notexon[datapvcol], substr)

                plusformat = data_notexon[data_notexon[datapvcol].isin(plusvariants)]
                plusformat = plusformat[~plusformat[datapvcol].str.contains('>', na=False)]
                splitplus = plusformat[datapvcol].str.split('+', expand=True)
                if (splitplus.shape[0] != 0 and max(splitplus) == 1):
                    plusformat['PV_plus1'] = splitplus[0]
                    plusformat['PV_plus2'] = splitplus[1]
                    merg_plusformat12 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol, ptaacol],
                                                 right_on=[datagenecol, 'PV_plus1', 'PV_plus2'], how='inner')
                elif (splitplus.shape[0] != 0 and max(splitplus) == 2):
                    plusformat['PV_plus1'] = splitplus[0]
                    plusformat['PV_plus2'] = splitplus[1]
                    plusformat['PV_plus3'] = splitplus[2]
                    merg_plusformat12 = pd.merge(ptdata, plusformat,
                                                 left_on=[ptgenecol, ptaacol, ptaacol, ptaacol],
                                                 right_on=[datagenecol, 'PV_plus1', 'PV_plus2', 'PV_plus3'],
                                                 how='inner')
                elif (splitplus.shape[0] != 0 and max(splitplus) == 3):
                    plusformat['PV_plus1'] = splitplus[0]
                    plusformat['PV_plus2'] = splitplus[1]
                    plusformat['PV_plus3'] = splitplus[2]
                    plusformat['PV_plus4'] = splitplus[3]
                    merg_plusformat12 = pd.merge(ptdata, plusformat,
                                                 left_on=[ptgenecol, ptaacol, ptaacol, ptaacol, ptaacol],
                                                 right_on=[datagenecol, 'PV_plus1', 'PV_plus2', 'PV_plus3', 'PV_plus4'],
                                                 how='inner')
                elif (splitplus.shape[0] != 0 and max(splitplus) == 4):
                    plusformat['PV_plus1'] = splitplus[0]
                    plusformat['PV_plus2'] = splitplus[1]
                    plusformat['PV_plus3'] = splitplus[2]
                    plusformat['PV_plus4'] = splitplus[3]
                    plusformat['PV_plus5'] = splitplus[4]
                    merg_plusformat12 = pd.merge(ptdata, plusformat,
                                                 left_on=[ptgenecol, ptaacol, ptaacol, ptaacol, ptaacol, ptaacol],
                                                 right_on=[datagenecol, 'PV_plus1', 'PV_plus2', 'PV_plus3', 'PV_plus4',
                                                           'PV_plus5'], how='inner')
                else:
                    plusformat['PV_plus1'] = plusformat[datapvcol]
                    plusformat['PV_plus2'] = plusformat[datapvcol]
                    merg_plusformat12 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol],
                                                 right_on=[datagenecol, datapvcol], how='inner')

                # SUBMethod1(S609fs+L1819U)for 12(compound mutation)
                # var1
                if (plusformat.shape[0] != 0):
                    anyformat = plusformat[plusformat['PV_plus1'].str.endswith('U', na=False)]
                    anyformat = anyformat[~anyformat['PV_plus1'].str.contains('J', na=False)]
                    if (anyformat.shape[0] != 0):
                        anyformat['PV_plus1_u'] = anyformat['PV_plus1'].map(lambda x: str(x)[:-1])
                    else:
                        anyformat['PV_plus1_u'] = anyformat['PV_plus1']
                    ptdata['AAChange1'] = ptdata[ptaacol].map(lambda x: str(x)[:-1])
                    # var2
                    anyformat2 = plusformat[plusformat['PV_plus2'].str.endswith('U', na=False)]
                    anyformat2 = anyformat2[~anyformat2['PV_plus2'].str.contains('J', na=False)]
                    if (anyformat2.shape[0] != 0):
                        anyformat2['PV_plus2_u'] = anyformat2['PV_plus2'].map(lambda x: str(x)[:-1])
                    else:
                        anyformat2['PV_plus2_u'] = anyformat2['PV_plus2']
                    anyformat = pd.concat([anyformat, anyformat2], sort=False)

                    merg_plusformat12_Uformat1 = pd.merge(ptdata, anyformat, left_on=[ptgenecol, 'AAChange1', ptaacol],
                                                          right_on=[datagenecol, 'PV_plus1_u', 'PV_plus2'], how='inner')
                    merg_plusformat12_Uformat2 = pd.merge(ptdata, anyformat,
                                                          left_on=[ptgenecol, 'AAChange1', 'AAChange1'],
                                                          right_on=[datagenecol, 'PV_plus1_u', 'PV_plus2_u'],
                                                          how='inner')
                    merg_plusformat12_Uformat3 = pd.merge(ptdata, anyformat, left_on=[ptgenecol, ptaacol, 'AAChange1'],
                                                          right_on=[datagenecol, 'PV_plus1', 'PV_plus2_u'], how='inner')

                    # SUBMethod2(CanyF+RanyH)for 12(compound mutation)
                    # var1
                    plus_anyformat1 = plusformat[plusformat['PV_plus1'].str.contains('ANY', na=False)]
                    plus_anyformat1 = plus_anyformat1[~plus_anyformat1['PV_plus1'].str.contains('J', na=False)]
                    splitany = plus_anyformat1['PV_plus1'].str.split('ANY', expand=True)
                    if (splitany.shape[0] != 0):
                        plus_anyformat1['PV_plus1_any1'] = splitany[0]
                        plus_anyformat1['PV_plus1_any2'] = splitany[1]
                    else:
                        plus_anyformat1['PV_plus1_any1'] = plus_anyformat1['PV_plus1']
                        plus_anyformat1['PV_plus1_any2'] = plus_anyformat1['PV_plus1']
                    # var2
                    plus_anyformat2 = plusformat[plusformat['PV_plus2'].str.contains('ANY', na=False)]
                    plus_anyformat2 = plus_anyformat2[~plus_anyformat2['PV_plus2'].str.contains('J', na=False)]
                    splitany2 = plus_anyformat2['PV_plus2'].str.split('ANY', expand=True)
                    if (splitany.shape[0] != 0):
                        plus_anyformat2['PV_plus2_any1'] = splitany2[0]
                        plus_anyformat2['PV_plus2_any2'] = splitany2[1]
                    else:
                        plus_anyformat2['PV_plus2_any1'] = plus_anyformat2['PV_plus2']
                        plus_anyformat2['PV_plus2_any2'] = plus_anyformat2['PV_plus2']
                    plus_anyformat = pd.concat([plus_anyformat1, plus_anyformat2], sort=False)
                    ptdata['AAChange_char1'] = [x[0] if isinstance(x, str) else np.nan for x in ptdata[ptaacol]]
                    ptdata['AAChange_char2'] = [x[-1] if isinstance(x, str) else np.nan for x in ptdata[ptaacol]]
                    merg_plusformat12_anyformat1 = pd.merge(ptdata, plus_anyformat,
                                                            left_on=[ptgenecol, 'AAChange_char1', 'AAChange_char2',
                                                                     'AAChange_char1', 'AAChange_char2'],
                                                            right_on=[datagenecol, 'PV_plus1_any1', 'PV_plus1_any2',
                                                                      'PV_plus2_any1', 'PV_plus2_any2'], how='inner')
                    merg_plusformat12_anyformat2 = pd.merge(ptdata, plus_anyformat,
                                                            left_on=[ptgenecol, ptaacol, 'AAChange_char1',
                                                                     'AAChange_char2'],
                                                            right_on=[datagenecol, 'PV_plus1', 'PV_plus2_any1',
                                                                      'PV_plus2_any2'], how='inner')
                    merg_plusformat12_anyformat3 = pd.merge(ptdata, plus_anyformat,
                                                            left_on=[ptgenecol, 'AAChange_char1', 'AAChange_char2',
                                                                     ptaacol],
                                                            right_on=[datagenecol, 'PV_plus1_any1', 'PV_plus1_any2',
                                                                      'PV_plus2'], how='inner')
                    plus_anyformat = pd.concat([plus_anyformat, anyformat], sort=False)

                    # SUBMethod3(CanyF+L1819U)for 12(compound mutation)
                    merg_plusformat12_u_anyformat1 = pd.merge(ptdata, plus_anyformat,
                                                              left_on=[ptgenecol, 'AAChange_char1', 'AAChange_char2',
                                                                       'AAChange1'],
                                                              right_on=[datagenecol, 'PV_plus1_any1', 'PV_plus1_any2',
                                                                        'PV_plus2_u'], how='inner')
                    merg_plusformat12_u_anyformat2 = pd.merge(ptdata, plus_anyformat,
                                                              left_on=[ptgenecol, 'AAChange1', 'AAChange_char1',
                                                                       'AAChange_char2'],
                                                              right_on=[datagenecol, 'PV_plus1_u', 'PV_plus2_any1',
                                                                        'PV_plus2_any2'], how='inner')
                else:
                    merg_plusformat12_Uformat1 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol],
                                                          right_on=[datagenecol, datapvcol], how='inner')
                    merg_plusformat12_Uformat2 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol],
                                                          right_on=[datagenecol, datapvcol], how='inner')
                    merg_plusformat12_Uformat3 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol],
                                                          right_on=[datagenecol, datapvcol], how='inner')
                    merg_plusformat12_anyformat1 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol],
                                                            right_on=[datagenecol, datapvcol], how='inner')
                    merg_plusformat12_anyformat2 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol],
                                                            right_on=[datagenecol, datapvcol], how='inner')
                    merg_plusformat12_anyformat3 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol],
                                                            right_on=[datagenecol, datapvcol], how='inner')
                    merg_plusformat12_u_anyformat1 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol],
                                                              right_on=[datagenecol, datapvcol], how='inner')
                    merg_plusformat12_u_anyformat2 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol],
                                                              right_on=[datagenecol, datapvcol], how='inner')

                # Method13 (WT)
                wtdata_format = data_notexon[data_notexon[datapvcol] == 'WT']
                wtdata_format_ug = wtdata_format[datagenecol].unique()
                ptdatawtgen_nottaken = ptdata[ptdata[ptgenecol].isin(wtdata_format_ug)]
                ptdatawtgen_nottaken_ug = ptdatawtgen_nottaken[ptgenecol].unique()

                def Diff(li1, li2):
                    return (list(set(li1) - set(li2)))

                reportedwtgenlst = Diff(wtdata_format_ug, ptdatawtgen_nottaken_ug)

                mrgeptdata = ptdata[ptdata[ptgenecol].isin(reportedwtgenlst)]
                mrgematchdata = data_notexon[data_notexon[datagenecol].isin(reportedwtgenlst)]
                mrgematchdatawt = mrgematchdata[mrgematchdata[datapvcol] == 'WT']
                finalwtdata13 = pd.concat([mrgematchdatawt, mrgeptdata], sort=False)

                finalGV_notexonmatch = pd.concat(
                    [merg_all, merg_uniquegens, merg_JANYU1, merg_Uformat2, merg_jnumuformat3, merg_anyformat4,
                     merg_JANYUfs5, merg_Jnumfs6,
                     merg_JnumUfs7, merg_endstarany_format8, merg_JANYUfsstarany9, merge_janyx10, merg_cds11,
                     merg_plusformat12,
                     merg_plusformat12_Uformat1, merg_plusformat12_Uformat2, merg_plusformat12_Uformat3,
                     merg_plusformat12_anyformat1,
                     merg_plusformat12_anyformat2, merg_plusformat12_anyformat3, merg_plusformat12_u_anyformat1,
                     merg_plusformat12_u_anyformat2, finalwtdata13], sort=False)

                orginallst = list(finalGV_notexonmatch)

                def diff(l1, l2):
                    return (list(set(l1) - set(l2)))

                droplst = diff(orginallst, ptdatacollist)
                droplst = diff(droplst, matchdatacollist)

                finalGV_notexonmatch = finalGV_notexonmatch.drop(droplst, axis=1)
                return finalGV_notexonmatch

        mskAct1_GV_notexonmatch = gvnotexonmacthfun(indata_dbinput, dbdata_snv, 'Gene.refGene', 'AAChange', 'GENE',
                                                    'PSEUDOVARIANT', 'EXON', list(dbdata_snv))

        # bmonc_GV_notexonmatch = gvnotexonmacthfun(indata_dbinput, bmoncoceptdata, 'Gene.refGene', 'AAChange','Gene_name', 'PSEUDOVARIANT', 'EXON',list(bmoncoceptdata))
        # dcp_GV_notexonmatch = gvnotexonmacthfun(indata_DCP, dcpdata, 'Gene.refGene', 'AAChange','Gene_Alias', 'PSEUDOVARIANT', '',list(dcpdata))

        # indata_dbinput, dbdata_snv,
        def gvexonmacthfun(ptdata, data, ptgenecol, ptaacol, ptexoncol, datagenecol, datapvcol, dataexoncol,
                           matchdatacollist):
            if (data.shape[0] != 0):
                data_exon = data[data[dataexoncol].notnull()]

                ptdata[ptgenecol] = ptdata[ptgenecol].astype(str)
                ptdata[ptaacol] = ptdata[ptaacol].astype(str)

                data_exon[datagenecol] = data_exon[datagenecol].astype(str)
                data_exon[datapvcol] = data_exon[datapvcol].astype(str)
                data_exon[dataexoncol] = data_exon[dataexoncol].astype(str)

                # Common match without checking anything
                merg_all = pd.merge(ptdata, data_exon, left_on=[ptgenecol, ptexoncol, ptaacol],
                                    right_on=[datagenecol, dataexoncol, datapvcol], how='inner')

                # genematch
                uniquegens = data_exon[datagenecol].unique()
                data_uniquegens = data_exon[data_exon[datapvcol].isin(uniquegens)]
                merg_uniquegens = pd.merge(ptdata, data_uniquegens, left_on=[ptgenecol], right_on=[datagenecol],
                                           how='inner')

                # MEHOD1(JANYU)
                data_JANYU1 = data_exon[data_exon[datapvcol].str.contains('JANYU', na=False)]
                merg_JANYU1 = pd.merge(ptdata, data_JANYU1, left_on=[ptgenecol, ptexoncol],
                                       right_on=[datagenecol, dataexoncol], how='inner')

                # METHOD2(V561U)
                uformat = data_exon[data_exon[datapvcol].str.endswith('U', na=False)]
                Uformat2 = uformat[~uformat[datapvcol].str.contains('J', na=False)]
                Uformat2['Pseudo Variant1'] = Uformat2[datapvcol].map(lambda x: str(x)[:-1])
                ptdata['AAChange1'] = ptdata[ptaacol].map(lambda x: str(x)[:-1])
                merg_Uformat2 = pd.merge(ptdata, Uformat2, left_on=[ptgenecol, ptexoncol, 'AAChange1'],
                                         right_on=[datagenecol, dataexoncol, 'Pseudo Variant1'], how='inner')

                # METHOD3(J61U)
                juformat = data_exon[data_exon[datapvcol].str.contains('J', na=False)]
                juformat = juformat[~juformat[datapvcol].str.endswith('U', na=False)]
                jnumuformat = juformat[~juformat[datapvcol].str.contains('ANY', na=False)]
                jnumuformat['pvlastremove'] = jnumuformat[datapvcol].map(lambda x: str(x)[:-1])
                jnumuformat['pvnum'] = jnumuformat['pvlastremove'].map(lambda x: str(x)[1:])
                ptdata['AAChangenum'] = ptdata['AAChange1'].map(lambda x: str(x)[1:])
                merg_jnumuformat3 = pd.merge(ptdata, jnumuformat, left_on=[ptgenecol, ptexoncol, 'AAChangenum'],
                                             right_on=[datagenecol, dataexoncol, 'pvnum'], how='inner')

                # method4(DANYV)(EanyX)
                anyformat = data_exon[data_exon[datapvcol].str.contains('ANY', na=False)]
                anyformat = anyformat[~anyformat[datapvcol].str.contains('J', na=False)]
                splitany = anyformat[datapvcol].str.split('ANY', expand=True)
                if (splitany.shape[0] != 0):
                    anyformat['PV1'] = splitany[0]
                    anyformat['PV2'] = splitany[1]
                else:
                    anyformat['PV1'] = anyformat[datapvcol]
                    anyformat['PV2'] = anyformat[datapvcol]
                ptdata['AAChange_char1'] = [x[0] if isinstance(x, str) else np.nan for x in ptdata[ptaacol]]
                ptdata['AAChange_char2'] = [x[-1] if isinstance(x, str) else np.nan for x in ptdata[ptaacol]]
                merg_anyformat4 = pd.merge(ptdata, anyformat,
                                           left_on=[ptgenecol, ptexoncol, 'AAChange_char1', 'AAChange_char2'],
                                           right_on=[datagenecol, dataexoncol, 'PV1', 'PV2'], how='inner')

                # method5(JANYUfs)
                JANYUfs_format = data_exon[data_exon[datapvcol].str.contains('JANYUfs', na=False)]
                ptdata_fs = ptdata[ptdata[ptaacol].str.endswith('fs', na=False)]
                merg_JANYUfs5 = pd.merge(ptdata_fs, JANYUfs_format, left_on=[ptgenecol, ptexoncol],
                                         right_on=[datagenecol, dataexoncol], how='inner')

                # method6(J281fs)
                Jnumfs_format = data_exon[data_exon[datapvcol].str.contains('J', na=False)]
                Jnumfs_format = Jnumfs_format[Jnumfs_format[datapvcol].str.endswith('fs', na=False)]
                filtvaljfs = ['JANYUfs', 'JANYUfs*any', 'JANYU']
                Jnumfs_format = Jnumfs_format[~Jnumfs_format[datapvcol].isin(filtvaljfs)]
                Jnumfs_format['PVNUM1'] = Jnumfs_format[datapvcol].map(lambda x: str(x)[:-2])
                Jnumfs_format['PVNUM1'] = Jnumfs_format['PVNUM1'].map(lambda x: str(x)[1:])
                ptdata_fs['AACh1'] = ptdata_fs[ptaacol].map(lambda x: str(x)[:-2])
                ptdata_fs['AACh1'] = ptdata_fs['AACh1'].map(lambda x: str(x)[1:])
                merg_Jnumfs6 = pd.merge(ptdata_fs, Jnumfs_format, left_on=[ptgenecol, ptexoncol, 'AACh1'],
                                        right_on=[datagenecol, dataexoncol, 'PVNUM1'], how='inner')

                # Method7(J58Ufs)
                JnumUfs_format = Jnumfs_format[Jnumfs_format[datapvcol].str.contains('U', na=False)]
                JnumUfs_format['PVNUM1'] = JnumUfs_format[datapvcol].map(lambda x: str(x)[:-3])
                JnumUfs_format['PVNUM1'] = JnumUfs_format['PVNUM1'].map(lambda x: str(x)[1:])
                ptdata_fs['AACh1'] = ptdata_fs[ptaacol].map(lambda x: str(x)[:-3])
                ptdata_fs['AACh1'] = ptdata_fs['AACh1'].map(lambda x: str(x)[1:])
                merg_JnumUfs7 = pd.merge(ptdata_fs, JnumUfs_format, left_on=[ptgenecol, ptexoncol, 'AACh1'],
                                         right_on=[datagenecol, dataexoncol, 'PVNUM1'], how='inner')

                # Method8(M1FS*ANY)
                endstarany_format = data_exon[data_exon[datapvcol].str.endswith('*ANY', na=False)]
                splitendstarany = endstarany_format[datapvcol].str.split('*', expand=True)
                if (splitendstarany.shape[0] != 0):
                    endstarany_format['PVdata'] = splitendstarany[0]
                else:
                    endstarany_format['PVdata'] = endstarany_format[datapvcol]
                ptdatafsstar = ptdata[ptdata[ptaacol].str.contains('fs*', na=False)]
                ptdatafsstar_splitstar = ptdatafsstar[ptaacol].str.split('*', expand=True)
                if (ptdatafsstar_splitstar.shape[0] != 0):
                    ptdatafsstar['AAChangefs'] = ptdatafsstar_splitstar[0]
                else:
                    ptdatafsstar['AAChangefs'] = ptdatafsstar[ptaacol]
                merg_endstarany_format8 = pd.merge(ptdatafsstar, endstarany_format,
                                                   left_on=[ptgenecol, ptexoncol, 'AAChangefs'],
                                                   right_on=[datagenecol, dataexoncol, 'PVdata'], how='inner')

                # Method9(JanyUfs*any)
                JANYUfsstarany_format = data_exon[data_exon[datapvcol] == 'JANYUfs*ANY']
                indataendfsstr = ptdatafsstar[ptdatafsstar[ptaacol].str.endswith('fs*', na=False)]
                uniendfsstr = indataendfsstr[ptaacol].unique()
                indatafsstarany = ptdatafsstar[~ptdatafsstar[ptaacol].isin(uniendfsstr)]
                merg_JANYUfsstarany9 = pd.merge(indatafsstarany, JANYUfsstarany_format, left_on=[ptgenecol, ptexoncol],
                                                right_on=[datagenecol, dataexoncol], how='inner')

                # METHOD10 (JANYX)
                janyx_format = data_exon[data_exon[datapvcol] == 'JANYX']
                indata_endx = ptdata[ptdata[ptaacol].str.endswith('X', na=False)]
                merge_janyx10 = pd.merge(indata_endx, janyx_format, left_on=[ptgenecol, ptexoncol],
                                         right_on=[datagenecol, dataexoncol], how='inner')

                # METHOD11(c.1934dupG)
                CDS_format = data_exon[data_exon[datapvcol].str.contains('c.', na=False)]
                CDS_format['PVcds'] = CDS_format[datapvcol].map(lambda x: str(x)[2:])
                merg_cds11 = pd.merge(ptdata, CDS_format, left_on=[ptgenecol, ptexoncol, 'AAChange_CDS'],
                                      right_on=[datagenecol, dataexoncol, 'PVcds'], how='inner')

                # METHOD12(V600E+V600M+etc upto 5 compound mutation)
                def plusFilter(string, substr):
                    return [str for str in string if any(sub in str for sub in substr)]

                substr = ['+']
                # data_exon[datapvcol]=data_exon[datapvcol].astype(str)
                plusvariants = plusFilter(data_exon[datapvcol], substr)

                plusformat = data_exon[data_exon[datapvcol].isin(plusvariants)]
                plusformat = plusformat[~plusformat[datapvcol].str.contains('>', na=False)]
                splitplus = plusformat[datapvcol].str.split('+', expand=True)
                if (splitplus.shape[0] != 0 and max(splitplus) == 1):
                    plusformat['PV_plus1'] = splitplus[0]
                    plusformat['PV_plus2'] = splitplus[1]
                    merg_plusformat12 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptexoncol, ptaacol, ptaacol],
                                                 right_on=[datagenecol, dataexoncol, 'PV_plus1', 'PV_plus2'],
                                                 how='inner')
                elif (splitplus.shape[0] != 0 and max(splitplus) == 2):
                    plusformat['PV_plus1'] = splitplus[0]
                    plusformat['PV_plus2'] = splitplus[1]
                    plusformat['PV_plus3'] = splitplus[2]
                    merg_plusformat12 = pd.merge(ptdata, plusformat,
                                                 left_on=[ptgenecol, ptexoncol, ptaacol, ptaacol, ptaacol],
                                                 right_on=[datagenecol, dataexoncol, 'PV_plus1', 'PV_plus2',
                                                           'PV_plus3'],
                                                 how='inner')
                elif (splitplus.shape[0] != 0 and max(splitplus) == 3):
                    plusformat['PV_plus1'] = splitplus[0]
                    plusformat['PV_plus2'] = splitplus[1]
                    plusformat['PV_plus3'] = splitplus[2]
                    plusformat['PV_plus4'] = splitplus[3]
                    merg_plusformat12 = pd.merge(ptdata, plusformat,
                                                 left_on=[ptgenecol, ptexoncol, ptaacol, ptaacol, ptaacol, ptaacol],
                                                 right_on=[datagenecol, dataexoncol, 'PV_plus1', 'PV_plus2', 'PV_plus3',
                                                           'PV_plus4'],
                                                 how='inner')
                elif (splitplus.shape[0] != 0 and max(splitplus) == 4):
                    plusformat['PV_plus1'] = splitplus[0]
                    plusformat['PV_plus2'] = splitplus[1]
                    plusformat['PV_plus3'] = splitplus[2]
                    plusformat['PV_plus4'] = splitplus[3]
                    plusformat['PV_plus5'] = splitplus[4]
                    merg_plusformat12 = pd.merge(ptdata, plusformat,
                                                 left_on=[ptgenecol, ptexoncol, ptaacol, ptaacol, ptaacol, ptaacol,
                                                          ptaacol],
                                                 right_on=[datagenecol, dataexoncol, 'PV_plus1', 'PV_plus2', 'PV_plus3',
                                                           'PV_plus4', 'PV_plus5'], how='inner')
                else:
                    plusformat['PV_plus1'] = plusformat[datapvcol]
                    plusformat['PV_plus2'] = plusformat[datapvcol]
                    merg_plusformat12 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptexoncol, ptaacol],
                                                 right_on=[datagenecol, dataexoncol, datapvcol], how='inner')

                # SUBMethod1(S609fs+L1819U)for 12(compound mutation)
                # var1
                if (plusformat.shape[0] != 0):
                    anyformat = plusformat[plusformat['PV_plus1'].str.endswith('U', na=False)]
                    anyformat = anyformat[~anyformat['PV_plus1'].str.contains('J', na=False)]
                    if (anyformat.shape[0] != 0):
                        anyformat['PV_plus1_u'] = anyformat['PV_plus1'].map(lambda x: str(x)[:-1])
                    else:
                        anyformat['PV_plus1_u'] = anyformat['PV_plus1']
                    ptdata['AAChange1'] = ptdata[ptaacol].map(lambda x: str(x)[:-1])
                    # var2
                    anyformat2 = plusformat[plusformat['PV_plus2'].str.endswith('U', na=False)]
                    anyformat2 = anyformat2[~anyformat2['PV_plus2'].str.contains('J', na=False)]
                    if (anyformat2.shape[0] != 0):
                        anyformat2['PV_plus2_u'] = anyformat2['PV_plus2'].map(lambda x: str(x)[:-1])
                    else:
                        anyformat2['PV_plus2_u'] = anyformat2['PV_plus2']
                    anyformat = pd.concat([anyformat, anyformat2], sort=False)
                    merg_plusformat12_Uformat1 = pd.merge(ptdata, anyformat,
                                                          left_on=[ptgenecol, ptexoncol, 'AAChange1', ptaacol],
                                                          right_on=[datagenecol, dataexoncol, 'PV_plus1_u', 'PV_plus2'],
                                                          how='inner')
                    merg_plusformat12_Uformat2 = pd.merge(ptdata, anyformat,
                                                          left_on=[ptgenecol, ptexoncol, 'AAChange1', 'AAChange1'],
                                                          right_on=[datagenecol, dataexoncol, 'PV_plus1_u',
                                                                    'PV_plus2_u'],
                                                          how='inner')
                    merg_plusformat12_Uformat3 = pd.merge(ptdata, anyformat,
                                                          left_on=[ptgenecol, ptexoncol, ptaacol, 'AAChange1'],
                                                          right_on=[datagenecol, dataexoncol, 'PV_plus1', 'PV_plus2_u'],
                                                          how='inner')

                    # SUBMethod2(CanyF+RanyH)for 12(compound mutation)
                    # var1
                    plus_anyformat1 = plusformat[plusformat['PV_plus1'].str.contains('ANY', na=False)]
                    plus_anyformat1 = plus_anyformat1[~plus_anyformat1['PV_plus1'].str.contains('J', na=False)]
                    splitany = plus_anyformat1['PV_plus1'].str.split('ANY', expand=True)
                    if (splitany.shape[0] != 0):
                        plus_anyformat1['PV_plus1_any1'] = splitany[0]
                        plus_anyformat1['PV_plus1_any2'] = splitany[1]
                    else:
                        plus_anyformat1['PV_plus1_any1'] = plus_anyformat1['PV_plus1']
                        plus_anyformat1['PV_plus1_any2'] = plus_anyformat1['PV_plus1']
                    # var2
                    plus_anyformat2 = plusformat[plusformat['PV_plus2'].str.contains('ANY', na=False)]
                    plus_anyformat2 = plus_anyformat2[~plus_anyformat2['PV_plus2'].str.contains('J', na=False)]
                    splitany2 = plus_anyformat2['PV_plus2'].str.split('ANY', expand=True)
                    if (splitany.shape[0] != 0):
                        plus_anyformat2['PV_plus2_any1'] = splitany2[0]
                        plus_anyformat2['PV_plus2_any2'] = splitany2[1]
                    else:
                        plus_anyformat2['PV_plus2_any1'] = plus_anyformat2['PV_plus2']
                        plus_anyformat2['PV_plus2_any2'] = plus_anyformat2['PV_plus2']
                    plus_anyformat = pd.concat([plus_anyformat1, plus_anyformat2], sort=False)
                    ptdata['AAChange_char1'] = [x[0] if isinstance(x, str) else np.nan for x in ptdata[ptaacol]]
                    ptdata['AAChange_char2'] = [x[-1] if isinstance(x, str) else np.nan for x in ptdata[ptaacol]]
                    merg_plusformat12_anyformat1 = pd.merge(ptdata, plus_anyformat,
                                                            left_on=[ptgenecol, ptexoncol, 'AAChange_char1',
                                                                     'AAChange_char2', 'AAChange_char1',
                                                                     'AAChange_char2'],
                                                            right_on=[datagenecol, dataexoncol, 'PV_plus1_any1',
                                                                      'PV_plus1_any2', 'PV_plus2_any1',
                                                                      'PV_plus2_any2'],
                                                            how='inner')
                    merg_plusformat12_anyformat2 = pd.merge(ptdata, plus_anyformat,
                                                            left_on=[ptgenecol, ptexoncol, ptaacol, 'AAChange_char1',
                                                                     'AAChange_char2'],
                                                            right_on=[datagenecol, dataexoncol, 'PV_plus1',
                                                                      'PV_plus2_any1',
                                                                      'PV_plus2_any2'], how='inner')
                    merg_plusformat12_anyformat3 = pd.merge(ptdata, plus_anyformat,
                                                            left_on=[ptgenecol, ptexoncol, 'AAChange_char1',
                                                                     'AAChange_char2', ptaacol],
                                                            right_on=[datagenecol, dataexoncol, 'PV_plus1_any1',
                                                                      'PV_plus1_any2', 'PV_plus2'], how='inner')
                    # SUBMethod3(CanyF+L1819U)for 12(compound mutation)
                    plus_anyformat = pd.concat([plus_anyformat, anyformat], sort=False)
                    merg_plusformat12_u_anyformat1 = pd.merge(ptdata, plus_anyformat,
                                                              left_on=[ptgenecol, ptexoncol, 'AAChange_char1',
                                                                       'AAChange_char2', 'AAChange1'],
                                                              right_on=[datagenecol, dataexoncol, 'PV_plus1_any1',
                                                                        'PV_plus1_any2', 'PV_plus2_u'], how='inner')
                    merg_plusformat12_u_anyformat2 = pd.merge(ptdata, plus_anyformat,
                                                              left_on=[ptgenecol, ptexoncol, 'AAChange1',
                                                                       'AAChange_char1',
                                                                       'AAChange_char2'],
                                                              right_on=[datagenecol, dataexoncol, 'PV_plus1_u',
                                                                        'PV_plus2_any1', 'PV_plus2_any2'], how='inner')
                else:
                    merg_plusformat12_Uformat1 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol, ptexoncol],
                                                          right_on=[datagenecol, datapvcol, dataexoncol], how='inner')
                    merg_plusformat12_Uformat2 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol, ptexoncol],
                                                          right_on=[datagenecol, datapvcol, dataexoncol], how='inner')
                    merg_plusformat12_Uformat3 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol, ptexoncol],
                                                          right_on=[datagenecol, datapvcol, dataexoncol], how='inner')
                    merg_plusformat12_anyformat1 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol, ptexoncol],
                                                            right_on=[datagenecol, datapvcol, dataexoncol], how='inner')
                    merg_plusformat12_anyformat2 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol, ptexoncol],
                                                            right_on=[datagenecol, datapvcol, dataexoncol], how='inner')
                    merg_plusformat12_anyformat3 = pd.merge(ptdata, plusformat, left_on=[ptgenecol, ptaacol, ptexoncol],
                                                            right_on=[datagenecol, datapvcol, dataexoncol], how='inner')
                    merg_plusformat12_u_anyformat1 = pd.merge(ptdata, plusformat,
                                                              left_on=[ptgenecol, ptaacol, ptexoncol],
                                                              right_on=[datagenecol, datapvcol, dataexoncol],
                                                              how='inner')
                    merg_plusformat12_u_anyformat2 = pd.merge(ptdata, plusformat,
                                                              left_on=[ptgenecol, ptaacol, ptexoncol],
                                                              right_on=[datagenecol, datapvcol, dataexoncol],
                                                              how='inner')

                # Method13 (WT)
                wtdata_format = data_exon[data_exon[datapvcol] == 'WT']
                wtdata_format_ug = wtdata_format[datagenecol].unique()
                ptdatawtgen_nottaken = ptdata[ptdata[ptgenecol].isin(wtdata_format_ug)]
                ptdatawtgen_nottaken_ug = ptdatawtgen_nottaken[ptgenecol].unique()

                def Diff(li1, li2):
                    return (list(set(li1) - set(li2)))

                reportedwtgenlst = Diff(wtdata_format_ug, ptdatawtgen_nottaken_ug)

                mrgeptdata = ptdata[ptdata[ptgenecol].isin(reportedwtgenlst)]
                mrgematchdata = data_exon[data_exon[datagenecol].isin(reportedwtgenlst)]
                mrgematchdatawt = mrgematchdata[mrgematchdata[datapvcol] == 'WT']
                finalwtdata13 = pd.concat([mrgematchdatawt, mrgeptdata], sort=False)

                finalGVexonmatch = pd.concat(
                    [merg_all, merg_uniquegens, merg_JANYU1, merg_Uformat2, merg_jnumuformat3, merg_anyformat4,
                     merg_JANYUfs5, merg_Jnumfs6,
                     merg_JnumUfs7, merg_endstarany_format8, merg_JANYUfsstarany9, merge_janyx10, merg_cds11,
                     merg_plusformat12,
                     merg_plusformat12_Uformat1, merg_plusformat12_Uformat2, merg_plusformat12_Uformat3,
                     merg_plusformat12_anyformat1,
                     merg_plusformat12_anyformat2, merg_plusformat12_anyformat3, merg_plusformat12_u_anyformat1,
                     merg_plusformat12_u_anyformat2, finalwtdata13], sort=False)

                orginallst = list(finalGVexonmatch)

                def diff(l1, l2):
                    return (list(set(l1) - set(l2)))

                droplst = diff(orginallst, ptdatacollist)
                droplst = diff(droplst, matchdatacollist)

                finalGVexonmatch = finalGVexonmatch.drop(droplst, axis=1)
                return finalGVexonmatch

        mskAct1_GV_exonmatch = gvexonmacthfun(indata_dbinput, dbdata_snv, 'Gene.refGene', 'AAChange', 'AAChange_Exon',
                                              'GENE', 'PSEUDOVARIANT', 'EXON', list(dbdata_snv))

        # bmonc_GV_exonmatch = gvexonmacthfun(indata_dbinput, bmoncoceptdata, 'Gene.refGene', 'AAChange', 'AAChange_Exon','Gene_name','PSEUDOVARIANT', 'EXON', list(bmoncoceptdata))

        # GENE VARIANT MATCH ACT
        final_db_match = pd.concat([mskAct1_GV_exonmatch, mskAct1_GV_notexonmatch], sort=False)
        final_db_match = final_db_match.drop_duplicates()

        # Gene Variant bmoncocept
        # bmonc_GENEVAR = pd.concat([bmonc_GV_exonmatch, bmonc_GV_notexonmatch], sort=False)
        # bmonc_GENEVAR=bmonc_GENEVAR.drop_duplicates(MB)

        MSK1FN = finalname_EESP1 + '_Database_MATCH'
        MSK2FN = finalname_EESP_NSFSSGL4 + '_MSK_MATCH_old'
        MSK1pathname = dirName21 + '/' + MSK1FN + '.xlsx'
        MSK2pathname = dirName21 + '/' + MSK2FN + '.xlsx'

        print('writing ', MSK1FN)
        writer = pd.ExcelWriter(MSK1pathname, engine='xlsxwriter')
        # MSKmerg1_GENE_ACT.to_excel(writer, index=False, sheet_name='MSK_Gene_Actionable')
        final_db_match.to_excel(writer, index=False)
        # msk_tumsupgene_merg.to_excel(writer, index=False, sheet_name='MSK_Gene_TUMSUPGENES')
        writer.save()

        # FDA report
        fdastatreprt = pd.read_excel(io=dbdata, sheet_name='FDA_Report_Template', skiprows=1)

        fdarptfilt = ['Not Applicable', '-']
        fdafillrept1 = fdastatreprt[fdastatreprt['STATUS'].isin(fdarptfilt)]
        fdafillrept = fdastatreprt[~fdastatreprt['STATUS'].isin(fdarptfilt)]

        fdavarchek = fdafillrept[fdafillrept['Variant'].notnull()]
        fdagenchck = fdafillrept.merge(fdavarchek, indicator=True, how='left').loc[lambda x: x['_merge'] != 'both']
        fdagenchck = fdagenchck.drop(['_merge'], axis=1)

        # genecheck

        finalmerge_fda = final_db_match[final_db_match['SOURCE'] == 'FDA']

        # finalmerge_fda['Biomarker'] = finalmerge_fda['Biomarker'].replace('BRCA1', "BRCA")
        # finalmerge_fda['Biomarker'] = finalmerge_fda['Biomarker'].replace('BRCA2', "BRCA")
        # finalmerge_fda['Biomarker'] = finalmerge_fda['Biomarker'].replace('HRAS', "RAS")
        # finalmerge_fda['Biomarker'] = finalmerge_fda['Biomarker'].replace('NRAS', "RAS")
        # finalmerge_fda['Biomarker'] = finalmerge_fda['Biomarker'].replace('KRAS', "RAS")

        unifdamatchgen = finalmerge_fda['GENE'].unique()
        print('fdamatchegenes', unifdamatchgen)
        unifdamatchvar = finalmerge_fda['VARIANT '].unique()
        fdagenchck1 = fdagenchck[fdagenchck['Gene'].isin(unifdamatchgen)]
        colrlistgen1 = fdagenchck1['Gene'].unique()
        print('mathed gene fda', colrlistgen1)
        fdagenchck2 = fdagenchck[~fdagenchck['Gene'].isin(unifdamatchgen)]
        print('notmatchgene', fdagenchck2['Gene'].unique())
        fdagenchck1['STATUS'] = 'Positive'
        fdagenchck2['STATUS'] = 'Negative'
        fdagenchck = pd.concat([fdagenchck1, fdagenchck2], sort=False)

        # genevariantcheck
        fdavarchek = \
            (fdavarchek.set_index(fdavarchek.columns.drop('Variant', 1).tolist())
                 .Variant.str.split(', ', expand=True)
                 .stack()
                 .reset_index()
                 .rename(columns={0: 'Variant'})
                 .loc[:, fdavarchek.columns]
                 )
        
        fdavarchek1 = fdavarchek[fdavarchek['Gene'].isin(unifdamatchgen)]
        colrlistgen2 = fdavarchek1['Gene'].unique()
        fdagenvarchek1 = fdavarchek1[fdavarchek1['Variant'].isin(unifdamatchvar)]
        fdagenvarchek2 = fdavarchek1[~fdavarchek1['Variant'].isin(unifdamatchvar)]
        colrlistvar1 = fdagenvarchek1['Variant'].unique()
        fdavarchek2 = fdavarchek[~fdavarchek['Gene'].isin(unifdamatchgen)]

        fdagenvarchek1['STATUS'] = 'Positive'
        fdagenvarchek2['STATUS'] = 'Negative'
        fdavarchek2['STATUS'] = 'Negative'
        fdavarchck = pd.concat([fdagenvarchek1, fdagenvarchek2, fdavarchek2], sort=False)

        # bold text
        def row_style(row):
            if row.STATUS == 'Positive':
                return pd.Series('font-weight: bold', row.index)
            else:
                return pd.Series('', row.index)

        # coluring
        def row_style2(row):
            if row.STATUS == 'Positive':
                return pd.Series('color: #006400', row.index)
            else:
                return pd.Series('', row.index)

        fdafinalrport = pd.concat([fdafillrept1, fdagenchck, fdavarchck], sort=False)
        fdafinalrport = fdafinalrport.drop(['Gene', 'Variant'], axis=1)
        fdafinalrport = fdafinalrport.sort_values(by='BIOMARKER')
        fdafinalrport = fdafinalrport.drop_duplicates()
        fdafinalrport = fdafinalrport.groupby(['DRUG', 'BIOMARKER'], sort=False)['STATUS'].apply(','.join).reset_index()
        fdafinalrport['STATUS'] = fdafinalrport['STATUS'].replace('Positive,Negative', "Positive")
        fdafinalrport = fdafinalrport.reset_index(drop=True).style.apply(row_style2, axis=1).apply(row_style, axis=1)

        fdafn2 = finalname_EESP_NSFSSGL4 + '_FDA_Report'
        fdapathname2 = dirName_fdaReport + '/' + fdafn2 + '.xlsx'

        print('writing ', fdafn2)
        writer = pd.ExcelWriter(fdapathname2, engine='xlsxwriter')
        fdafinalrport.to_excel(writer, index=False)
        writer.save()
        return pathname1_2455

