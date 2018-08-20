#coding=utf-8
import readConfig
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import threading,os
import glob,zipfile
from log import MyLog
recf=readConfig.ReadConfig()

class Email:
    def __init__(self):
        self.sender =recf.get_email('sender')
        self.receiver = recf.get_email('receiver')
        self.subject = '[AutomationTest]接口自动化测试报告通知'
        self.smtpserver = recf.get_email('smtpserver')
        self.username = recf.get_email('username')
        self. password =recf.get_email('password')
        self.emailflg=recf.get_email('emailflg')
        self.log=MyLog.get_log()
        self.logger=self.log.get_logger()
        self.message=MIMEMultipart()
    def config_header(self):
        self.message['subject'] = self.subject
        self.message['From'] = self.sender
        self.message['To'] = self.receiver

    def set_content(self):
        try:
            with open(os.path.join(readConfig.proDir,'testfile','mail.txt')) as f:
               content= f.read()
        except Exception as ex:
            self.logger.error(ex)
        finally:
            f.close()
        try:
            content_plain = MIMEText(content, 'html', 'utf-8')
            self.message.attach(content_plain)
        except Exception as ex:
            self.logger.error(ex)

    def set_file(self):
        try:
            file_path=self.log.get_result_path()
            reuslt_path=os.path.join(readConfig.proDir,'testfile','test.zip')
            files=glob.glob(file_path+'\*')
            f=zipfile.ZipFile(reuslt_path,'w',zipfile.ZIP_DEFLATED)
            for file in files:
                    # 修改压缩文件的目录结构
                f.write(file, '/report/' + os.path.basename(file))
            f.close()
            reportfile = open(reuslt_path, 'rb').read()
            filehtml = MIMEText(reportfile, 'base64', 'utf-8')
            filehtml['Content-Type'] = 'application/octet-stream'
            filehtml['Content-Disposition'] = 'attachment; filename="test.zip"'
            self.message.attach(filehtml)
        except Exception as ex:
            self.logger.error(ex)

    def send_Email(self):

         self.config_header()
         self.set_content()
         self.set_file()
         # smtp=smtplib.SMTP_SSL(smtpserver,465)
         try:
             smtp = smtplib.SMTP_SSL(self.smtpserver, 465)
             smtp.set_debuglevel(1)
             smtp.login(self.username, self.password)
             smtp.sendmail(self.sender, self.receiver, self.message.as_string())
             smtp.quit()
             self.logger.info("邮件已发送")
         except Exception as ex:
             self.logger.error(ex)

class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():

        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email

if __name__ == "__main__":
    email = MyEmail.get_email()
    #email.send_Email()
