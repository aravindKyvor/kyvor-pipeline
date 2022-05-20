import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")
import sys, getopt
import os
import time

start_time = time.time()


def cnv_svextractorTO(inputfile_sv, inputfile_cnv, path):
    head1, tail1 = os.path.split(inputfile_sv)
    tailname_sv = tail1
    filename = tailname_sv.split('SV')[0]
    tablname = path + "/" + filename + '_SV_CNV_TABLE.xlsx'
    # sv data
    indata_sv = pd.read_excel(inputfile_sv)
    svcollst = list(indata_sv)
    splitvalcol = svcollst[14]

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

    if indata_sv.shape[0] != 0:
        indata_sv = colsplit(indata_sv, 'FORMAT', ':')
        indata_sv_pass = indata_sv[indata_sv['FILTER'] == 'PASS']
        indata_sv_pass = indata_sv_pass[indata_sv_pass['Annotation_mode'] == 'split']

    # writer=pd.ExcelWriter('CRCM1_TO_SV_CNV_Table.xlsx',engine='xlsxwriter')
    # indata_sv_pass.to_excel(writer,index=False)
    # writer.save()

    # cnv data
    indata_cnv = pd.read_excel(inputfile_cnv)
    cnvcollst = list(indata_cnv)
    splitvalcol = cnvcollst[14]

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

    indata_cnv = colsplit(indata_cnv, 'FORMAT', ':')
    indata_cnv_pass = indata_cnv[indata_cnv['FILTER'] == 'PASS']
    indata_cnv_pass = indata_cnv_pass[indata_cnv_pass['Annotation_mode'] == 'split']

    indata_cnv_pass["Gene name"] = indata_cnv_pass["Gene_name"]

    keeplist_cnv = ['SV chrom', 'SV start', 'SV end', 'SV length', 'SV type', 'AnnotSV type', 'Gene name', 'NM',
                    'CDS length', 'tx length', 'location', 'AnnotSV ranking', 'GT', 'CN', 'PE']
    keeplist_sv = ['SV chrom', 'SV start', 'SV end', 'SV length', 'SV type', 'AnnotSV type', 'Gene name', 'NM',
                   'CDS length', 'tx length', 'location', 'AnnotSV ranking', 'PR', 'SR']

    cnvcollst = list(indata_cnv_pass)
    if indata_sv.shape[0] != 0:
        svcollst = list(indata_sv_pass)

    def finalcvcdiff1(l1, l2):
        return (list(set(l1) - set(l2)))

    cnvdroplst1 = finalcvcdiff1(cnvcollst, keeplist_cnv)

    if indata_sv.shape[0] != 0:
        svdroplst1 = finalcvcdiff1(svcollst, keeplist_sv)

    indata_cnv_pass = indata_cnv_pass.drop(cnvdroplst1, axis=1)

    if indata_sv.shape[0] != 0:
        indata_sv_pass = indata_sv_pass.drop(svdroplst1, axis=1)

    indata_cnv_pass['PR'] = '-'
    indata_cnv_pass['SR'] = '-'
    indata_cnv_pass['Total_Exons'] = ''
    indata_cnv_pass['Matches'] = ''
    indata_cnv_pass['CNV/SV'] = 'CNV'
    if indata_sv.shape[0] != 0:
        indata_sv_pass['GT'] = '-'
        indata_sv_pass['CN'] = '-'
        indata_sv_pass['PE'] = '-'
        indata_sv_pass['Total_Exons'] = ''
        indata_sv_pass['Matches'] = ''
        indata_sv_pass['CNV/SV'] = 'SV'

    if indata_sv.shape[0] != 0:
        svcnvtable = pd.concat([indata_sv_pass, indata_cnv_pass], sort=False)
    else:
        svcnvtable = indata_cnv_pass
    cols = list(svcnvtable)
    cols.insert(8, cols.pop(cols.index('CNV/SV')))
    cols.insert(9, cols.pop(cols.index('Total_Exons')))
    svcnvtable = svcnvtable.loc[:, cols]

    svcnvtable = svcnvtable.sort_values(by='Gene name')

    writer = pd.ExcelWriter(tablname, engine='xlsxwriter')
    svcnvtable.to_excel(writer, index=False)
    writer.save()
    return tablname
