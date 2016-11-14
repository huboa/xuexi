import logging
##创建日志

logger = logging.getLogger("tset-log")
logger.setLevel(logging.DEBUG)

##创建 屏幕 输出debug
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

##创建文件 handler 设置 警告级别
fh = logging.FileHandler("access.log",encoding="utf-8")
fh.setLevel(logging.ERROR)

fh_formatter = logging.Formatter('%(asctime)s %(process)d %(filename)s:%(lineno)d - %(levelname)s: %(message)s')
ch_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s)')
fh.setFormatter(fh_formatter)
ch.setFormatter(ch_formatter)

logging._addHandlerRef(fh)
logging._addHandlerRef(ch)

logging.warning("warning commit....")
logger.error("error happend..")
