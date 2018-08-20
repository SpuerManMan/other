#coding=utf-8
import readConfig
import requests
from log import MyLog
log=MyLog.get_log()
logger=log.get_logger()
cf=readConfig.ReadConfig()
import gzip

class configHttp:
    def __init__(self):
        self.testip=cf.get_http('testip')
        self.port=cf.get_http('port')

    # 设置URL参数
    def set_url(self,urlpath):
        self.url='http://'+self.testip+':'+self.port+urlpath
        #print(self.url)

     #设置header参数
    def set_headers(self):
        self.headers={
        'Content-Encoding': 'gzip',
        'Content-Type': 'x-application/x-gzip'}

    def set_params(self,params):

        self.params=params
    #设置post参数
    def set_data(self,data):
        # dat = bytes(json.dumps(data), 'utf-8')
        # str 转bytes
        dat = str.encode(data)
        ct = gzip.compress(dat)
        self.data=ct

     # post 请求
    def post(self):
       try:
           # response=requests.post(self.url,headers=self.headers,data=self.data)
           response = requests.post(self.url, headers=self.headers, data=self.data)
           return response
       except Exception as e:
           logger.error(e)

     #get 请求
    def get(self):
        try:
          request=requests.get(self.url,headers=self.headers,params=self.params)
          return request
        except Exception as e:
            logger.error(e)
    def getprint(self):
        return self.port

'''
if __name__=="__main__":
    conf=configHttp()
    conf.set_url(urlpath)
    conf.set_data(postData)
    conf.set_headers(requestHeaders)
    rep=conf.post()
    print(rep.text)
'''