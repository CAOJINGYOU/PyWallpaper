import os
import logging
import sys
import time
import logging.handlers
 
def singleton(cls):
  instances = {}
  def _singleton(*args,**kwargs):
    if cls not in instances:
      instances[cls] = cls(*args,**kwargs)
    return instances[cls]
  return _singleton
 
@singleton
class Logger():
    def __init__(self,logfile=None):
        self.logger = logging.getLogger()
        formater = logging.Formatter("%(asctime)s %(name)s  %(levelname)s %(filename)s  %(lineno)d  %(message)s")
        if logfile == None:
            stime = time.strftime("%Y-%m-%d",time.localtime())
            logfile = os.getcwd() + os.sep + "log_" + stime + ".log"
        else:
            logfile = os.path.join(os.getcwd(),logfile)+ ".log"
        self.sh = logging.StreamHandler(sys.stdout)
        self.sh.setFormatter(formater)
        #self.fh = logging.FileHandler(logfile)
        self.fh = logging.handlers.RotatingFileHandler(logfile, maxBytes = 1024*1024, backupCount = 5)
        self.fh.setFormatter(formater)
        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.fh)
        self.logger.setLevel(logging.DEBUG)
 
if __name__ == "__main__":

    lg = Logger("test")
    lg.logger.warning("test")
