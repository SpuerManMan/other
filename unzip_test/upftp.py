#coding=utf-8
from ftplib import FTP

def ftpconnect(host,username,password):
    ftp=FTP() #设置变量
    #ftp.set_debuglevel(2)#打开调试级别2，显示详细信息
    ftp.connect(host,21)
    ftp.login(username,password)
    return ftp

def downloadfile(ftp,remotepath,localpath):
     print(ftp.size(remotepath),'KB')
     bufsize=1024
     tp=open(localpath,'wb')
     ftp.retrbinary('RETR '+remotepath,tp.write,bufsize)
     ftp.set_debuglevel(0)
     tp.close()

def uploadfile(ftp,remotepath,localpath):
    bufsize=1024
    fp=open(localpath,'rb')
    ftp.storbinary('STOR '+remotepath,fp,bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__=="__main__":
    ftp =ftpconnect('192.168.200.18','nbpt','g6s8m3t7s')
    downloadfile(ftp,'quick-1.0.1-setup.zip','quick-1.0.1-setup.zip')
    ftp.quit()