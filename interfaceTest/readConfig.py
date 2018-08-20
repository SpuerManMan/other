#coding=utf-8
import configparser
import os
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath=os.path.join(proDir, "conf.ini")

conf = configparser.ConfigParser()
conf.read(configPath)

class ReadConfig:
    def __init__(self):
        self.conf=configparser.ConfigParser()
        self.conf.read(configPath)

     #读取配置文件EMAIL下的key：value
    def get_email(self,name):
         value=self.conf.get("EMAIL",name)
         return value

    # 读取配置文件HTTP下的key：value
    def get_http(self,name):
        value=self.conf.get("HTTP",name)
        return value


if __name__ == "__main__":
    email = ReadConfig()
    s=email.get_http('header')
    print (s)
