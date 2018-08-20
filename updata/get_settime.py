#coding=utf-8

import zipfile
import os,time
from datetime import datetime
import xml.dom.minidom
import shutil
from log import log

def get_zip(dir_path,zip_path):
    format = '%Y-%m-%d %H:%M:%S.%f'
    zfile=zipfile.ZipFile(dir_path,'r')
    for filename in zfile.namelist():
        zfile.extract(filename, zip_path)
    zfile.close()
    pt=os.listdir(zip_path)
    for p in pt:
       sp= os.path.join(zip_path,p)
       #print (sp)
    if os.path.exists(os.path.join(zip_path,'ItemResult.xml')):
        log.LOG_INFO('ItemResult.xml文件已解压')
        dom=xml.dom.minidom.parse(os.path.join(zip_path,'ItemResult.xml'))
        re=dom.getElementsByTagName('Blocked')
        if re[0].firstChild==None:
            log.LOG_INFO('Blocked解析为NUll')
            return
        else:
            Blocked=re[0].firstChild.data
            log.LOG_INFO('Blocked:%s'%Blocked)
        re1=dom.getElementsByTagName('Screen90PEndTime')
        if re1[0].firstChild==None:
            log.LOG_INFO('Screen90PEndTime解析为NUll')
            return
        else:
            Screen90PEndTime=re1[0].firstChild.data
            log.LOG_INFO('Screen90PEndTime:%s' % Screen90PEndTime)
    else:
        log.LOG_INFO('ItemResult.xml文件不存在')
    if os.path.exists(os.path.join(zip_path,'Resources.xml')):
        log.LOG_INFO('Resources.xml文件已解压')
        dom = xml.dom.minidom.parse(os.path.join(zip_path, 'Resources.xml'))
        itemlist = dom.getElementsByTagName('Page')
        StartedDateTime = itemlist[0].getAttribute("StartedDateTime")
        if StartedDateTime=='':
            log.LOG_INFO('StartedDateTime解析为空！')
        else:
            log.LOG_INFO('StartedDateTime:%s'%StartedDateTime)

    else:
        log.LOG_INFO('Resources.xml文件不存在')

    a = datetime.strptime(Screen90PEndTime, format)
    b = datetime.strptime(StartedDateTime, format)
    t1 = time.mktime(a.timetuple()) * 1000 + a.microsecond / 1000
    t2 = time.mktime(b.timetuple()) * 1000 + b.microsecond / 1000
    t3= t2+int(Blocked)
    screen90PsOffsetTime=(t1 - t3)/1000
    #print(stime)
    return screen90PsOffsetTime