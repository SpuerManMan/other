#coding=utf-8
"""
文件解压

Usage:
    unzip  <file> <num>


"""
from xml.etree import ElementTree
import zipfile
import os
from docopt import docopt
import  xml.dom.minidom
def netfly(file,num):
    panpath='D:\\netfly'
    for nm in range(2,num+1):
        zip=zipfile.ZipFile(file, 'r')
        zip.extractall(os.path.join(panpath,'ts'+str(nm)))
        zip.close()
        pafile = os.path.join(panpath, 'ts' + str(nm),'config', 'config.xml')
        print(pafile)
        # 修改config配置
        updateTree = ElementTree.parse(pafile)
        root = updateTree.getroot()
        for TsName in root.findall('Terminal'):
            TsName.find('TsName').text = 'Home' + str(nm)
        for TsDeviceId in root.findall('Terminal'):
            TsDeviceId.find('TsDeviceId').text = '60-45-CB-81-86-' + str(nm)
        updateTree.write(pafile,encoding="utf-8",xml_declaration=True)

def unzip():
    arguments = docopt(__doc__, version='unzip v1.0')
    file=arguments.get('<file>')
    data=arguments.get('<num>')
    num=int(data)
    netfly(file, num)

if __name__ == '__main__':
    #netfly('ts-tester-win-1.0.0.11-setup.zip', 2)
    unzip()