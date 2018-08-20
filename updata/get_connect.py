#coding=utf-8
import mysql.connector
import get_settime
from log import log
import os

import readConf
cf=readConf.Config()

class Data:

    def __init__(self):
        self.uesr=cf.get_Data('uesrname')
        self.pwd=cf.get_Data('password')
        self.database=cf.get_Data('database')
        self.host=cf.get_Data('host')
        self.starttime=cf.get_Data('starttime')
        self.endtime=cf.get_Data('endtime')

    def get_mysql(self):
        sql="SELECT Screen90PSOffsetTime,id,DATAFILE FROM testrecord4000005  WHERE BrowserType=2 AND teststarttime BETWEEN {0} AND {1}".format("'"+self.starttime+"'","'"+self.endtime+"'")
        try:
            con=mysql.connector.connect(user=self.uesr,password=self.pwd,database=self.database,host=self.host)
            cursor=con.cursor()
            cursor.execute(sql)
            values=cursor.fetchall()
            return values
        except Exception as ex:
            log.LOG_ERROR(ex)
        finally:
            cursor.close()
            con.close()

    def get_count(self):
        sql = "SELECT count(*) FROM testrecord4000005  WHERE BrowserType=2 AND teststarttime BETWEEN {0} AND {1}".format("'" + self.starttime + "'","'"+self.endtime+"'")
        try:
            con = mysql.connector.connect(user=self.uesr, password=self.pwd, database=self.database, host=self.host)
            cursor = con.cursor()
            cursor.execute(sql)
            values = cursor.fetchall()
            for v in values:
                count=v[0]
            return count
        except Exception as ex:
            log.LOG_ERROR(ex)
        finally:
            cursor.close()
            con.close()

    def updatp_time(self,settime,id):
        sql='update testrecord4000005 set Screen90PSOffsetTime={0} WHERE id={1}'.format("'"+str(settime)+"'","'"+str(id)+"'")
        try:
            conn=mysql.connector.connect(user=self.uesr, password=self.pwd, database=self.database, host=self.host)
            cusor=conn.cursor()
            cusor.execute(sql)
            conn.commit()
        except Exception as ex:
            log.LOG_ERROR(ex)
        finally:
            cusor.close()
            conn.close



    def runAll(self):
        proDir = os.path.split(os.path.realpath(__file__))[0]
        zip_path =os.path.join(proDir,'abc')
        #dir_path = 'D:\\test\\574_25_2338828_7_40000_20180502151848.423.zip'
        dir_path='D:\\test\\574_25_2338828_2_40000_20180502151421.819.zip'
        data=Data()
        count=data.get_count()
        c=int(count)
        log.LOG_INFO('查找到 %d 条结果需要更新！'%c)
        log.LOG_INFO('--------任务启动----------')
        vaules=data.get_mysql()
        i=1
        for va in vaules:
            sPTime=va[0]
            id=va[1]
            datefile=va[2]
            log.LOG_INFO('数据库原始screen90PsOffsetTime值：%s'% sPTime)
            log.LOG_INFO('数据库查询id：%s' % id)
            log.LOG_INFO('数据库文件路径：%s'% str(datefile))
        #for i in range(c):
            screen90PsOffsetTime=get_settime.get_zip(dir_path,zip_path)
            if screen90PsOffsetTime!=None:
                log.LOG_INFO('更新数据ID为:%s'% id)
                data.updatp_time(screen90PsOffsetTime,id)
                log.LOG_INFO('screen90PsOffsetTime:%s -->%s'%(sPTime,screen90PsOffsetTime))
                #log.LOG_INFO("第%d条数据更新完成！"%(c-1))
                log.LOG_INFO('-------第 %d 条数据执行完成！----------'%i)
            else:
                log.LOG_INFO('screen90PsOffsetTime值为空更新跳过！')
                log.LOG_INFO('--------第 %d 条数据执行完成！---------'%i)
            i=i+1