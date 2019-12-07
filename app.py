# 导包
import logging
from logging import handlers
import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
HEADERS={}
EMPID=""
def init_logger():
    # 日志器初始化
    logger=logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 初始化处理器

    # 初始化控制台处理器
    sh=logging.StreamHandler()
    # 初始化文件处理器
    log_path=BASE_DIR+"/log/ihrm.log"
    fh=logging.handlers.TimedRotatingFileHandler(log_path,when="H",interval=1,backupCount=3,encoding="utf-8")
    # 初始化格式化处理器
    fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d] - %(message)s"
    formatter=logging.Formatter(fmt)
    # 处理器添加格式化处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 日志器中添加处理器
    logger.addHandler(sh)
    logger.addHandler(fh)
