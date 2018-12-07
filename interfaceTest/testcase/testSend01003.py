import unittest
import common
import paramunittest
from config import configHttp
from log import MyLog
import time


xlxs=common.get_xls('case.xlsx','Sheet1')

@paramunittest.parametrized(*xlxs)
class send01003(unittest.TestCase):
     def setParameters(self,urlpath,request,reParms,code,result):
         self.urlpath=urlpath
         print(self.urlpath)
         self.request=request
         self.data=reParms
         self.code=code
         self.result=result

     def setUp(self):
         self.log = MyLog.get_log()
         self.logger = self.log.get_logger()
         self.conf = configHttp.configHttp()
         self.logger.info('-------------------')

     def testSend01003_1(self):
            if self.request=='post':
                    self.logger.info('设置URL为:%s',self.urlpath)
                    self.conf.set_url(self.urlpath)
                    self.logger.info('设置header参数')
                    self.conf.set_headers()
                    self.logger.info('设置请求参数为:%s', self.data)
                    self.conf.set_data(self.data)
                    repose=self.conf.post()
                    self.logger.info('接口请求结果:%s',repose.text)
                    time.sleep(0.5)
                    #验证接口响应结果
                    self.assertEqual(repose.text ,"百度一下，你就知道")

     def testSend01003_2(self):
            if self.request=='post':
                    self.logger.info('设置URL为:%s', self.urlpath)
                    self.conf.set_url(self.urlpath)
                    self.conf.set_headers()
                    self.logger.info('设置请求参数为:%s', self.data)
                    self.conf.set_data(self.data)
                    repose=self.conf.post()
                    time.sleep(0.5)
                    self.logger.info('接口请求结果码:%s', repose.status_code)
                    #验证接口响应结果码
                    self.assertEqual(repose.status_code, self.code)

     def tearDown(self):
        self.logger.info('-------------------')
