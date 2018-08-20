#condig=utf-8
import  logging,os
import  threading
from datetime import datetime
proDir = os.path.split(os.path.realpath(__file__))[0]
class log():
    def __init__(self):
        # 创建日志文件路径
        self.logfilePtah=os.path.join(proDir,'log')
        if not os.path.exists(self.logfilePtah):
            os.mkdir(self.logfilePtah)
        self.logptah=os.path.join(self.logfilePtah,datetime.now().strftime("%Y%m%d%H%M%S"))
        if not os.path.exists(self.logptah):
            os.mkdir(self.logptah)
        #定义result.log
        log_file=os.path.join(self.logptah,'result.log')
        '''
        %(levelno)s：打印日志级别的数值
        %(levelname)s：打印日志级别的名称
        %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s：打印当前执行程序名
        %(funcName)s：打印日志的当前函数
        %(lineno)d：打印日志的当前行号
        %(asctime)s：打印日志的时间
        %(thread)d：打印线程ID
        %(threadName)s：打印线程名称
        %(process)d：打印进程ID
        %(message)s：打印日志信息
        '''
        # 设置logger输出格式
        log_farmat='[%(asctime)s][%(levelname)s][%(filename)s]->%(lineno)d %(message)s'
        logging.basicConfig(format=log_farmat,filename=log_file,level=logging.DEBUG)
        # 输出到屏幕
        console=logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        # 输出到屏幕的格式
        fomater=logging.Formatter(log_farmat) # 实例化formatter
        console.setFormatter(fomater)  #为handler添加formatter

        self.logger=logging.getLogger() #获取logger对象
        self.logger.addHandler(console) #为logger添加handler

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def get_report_path(self):
        reportpath=os.path.join(self.logptah,'report.html')
        return reportpath

    def get_result_path(self):

        return self.logptah

class MyLog:
    log = None
    mutex = threading.RLock() # 创建一个线程锁

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            #获取锁
            MyLog.mutex.acquire()
            try:
                MyLog.log = log()
            finally:
                #释放锁
                MyLog.mutex.release()
        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger=log.get_logger()
    logger.debug("test debug")
    logger.info("test info")
