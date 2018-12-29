#!/usr/bin/python
# coding=utf-8
import os
import time
import psutil
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

# os.system('/usr/local/nbpt/mobilets/ts-control-center/start.sh')
smtpserver='smtp.qq.com'
username='1213867918'
password='pskepuqwvgqebaga'

def jiank():
    monitor_name = set(['dataprovider','gsmts','tsreport','pasm','ts-control-center','ts-result-receiving','processing'])
    proc_dict = {}
    proc_name = set()

    monitor_map = {
        'dataprovider': '/usr/local/nbpt/mobilets/DataProvider/bin/startup.sh',
        'gsmts':'/usr/local/nbpt/mobilets/gsmts/bin/startup.sh',
        'tsreport':'/usr/local/nbpt/mobilets/tsreport/bin/startup.sh',
        'pasm': '/usr/local/nbpt/mobilets/pasm/bin/startup.sh',
        'ts-control-center': '/usr/local/nbpt/mobilets/ts-control-center/start.sh',
        'processing': '/usr/local/nbpt/mobilets/ts-result-processing/bin/start.sh',
        'ts-result-receiving': '/usr/local/nbpt/mobilets/ts-result-receiving/start.sh',
    }
    while True:
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            proc_dict[proc.info['pid']] = proc.info['name']
            proc_name.add(proc.info['name'])

        proc_stop = monitor_name - proc_name
        print(proc_stop)
        if proc_stop:
            for p in proc_stop:

                p_name = p
                data = {
                    "程序退出告警通知": {
                        "程序退出时间": "### %s" % time.strftime("%Y-%m-%d %X") +
                                "#### %s程序退出,正在尝试自动重启!!!" % p_name
                    },
                }
                send_data = json.dumps(data,ensure_ascii=False)
                Send_Email(send_data)
                os.system(monitor_map[p_name])
                proc_set = set()
                for proc_again in psutil.process_iter(attrs=['pid', 'name']):
                    proc_set.add(proc_again.info['name'])

        time.sleep(5)
        proc_name = set()

def Send_Email(content):
    message = MIMEMultipart()
    message['subject'] ='程序监控告警通知'
    message['From'] ='1213867918@qq.com'
    message['To'] ='xiongt@nbpt.cn'
    content_plain = MIMEText(content, 'html', 'utf-8')
    message.attach(content_plain)
    stmp = smtplib.SMTP_SSL(smtpserver, 465)
    stmp.login(username, password)
    stmp.sendmail('1213867918@qq.com', 'xiongt@nbpt.cn', message.as_string())

jiank()
