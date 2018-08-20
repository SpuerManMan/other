#coding =utf-8
import os
import configparser

class Config:

    pDir=os.path.split(os.path.realpath(__file__))[0]
    confPath=os.path.join(pDir,'config.ini')
    conf=configparser.ConfigParser()
    conf.read(confPath)

    def __init__(self):
        pass

    def get_Data(self,name):
        value=self.conf.get('DATA',name)
        return value

if __name__=="__main__":
    conf=Config()
    username=conf.get_Data('uesrname')
    print(username)
