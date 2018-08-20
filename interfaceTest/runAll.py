#coding=utf-8
#from interfaceTest import HTMLTestRunner
from TestReport import HTMLTestReportCN
from log import MyLog
import readConfig
from config.configEmail import MyEmail
import os,sys
import unittest

class AllTest:

    def __init__(self):
        self.log=MyLog.get_log()
        self.logger=self.log.get_logger()
        self.resultpath=self.log.get_report_path()
        self.caseFile = os.path.join(readConfig.proDir, "testCase")
        self.email=MyEmail.get_email()


    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        test_suite = unittest.TestSuite()

        suite_module = []
        discover = unittest.defaultTestLoader.discover(self.caseFile, pattern='test*.py', top_level_dir=None)
        suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    #print (test_name)
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            #print (suit)
            if suit is not None:
                self.logger.info("********TEST START********")
                fp = open(self.resultpath, 'wb')
                runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description',tester='xiongt')
                runner.run(suit)
            else:
                self.logger.info("Have no case to test.")
        except Exception as ex:
            self.logger.error(str(ex))
        finally:
            self.logger.info("*********TEST END*********")
            fp.close()
            if self.email.emailflg=='on':
                self.email.send_Email()
            else:
                self.logger.info('邮件功能关闭')

if __name__ == '__main__':
    obj = AllTest()
    obj.run()