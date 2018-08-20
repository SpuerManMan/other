#coding=utf-8
import os
from xlrd import open_workbook
#获取当前的绝对路径
proDir=os.path.split(os.path.relpath(__file__))[0]

def get_xls(xls_name,sheet_name):
    cls=[]
    path= os.path.join(proDir,"testfile",xls_name)
    file=open_workbook(path)
    sheet=file.sheet_by_name(sheet_name)
    rows=sheet.nrows
    for i in range(rows):
        if sheet.row_values(i)[0]!='urlpath':
            cls.append(sheet.row_values(i))
    return  cls

#if __name__=="__main":
#print(get_xls('case.xlsx','Sheet1'))