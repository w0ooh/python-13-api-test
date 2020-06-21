# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/6/14 23:07
# File   : mylog.py
# IDE    : PyCharm

#1. 日志文件名参数化
#2.级别配置化
#3.输出路径参数化

import logging
import logging.handlers
import os

from common.config import ReadConfig
from common import contants


conf = ReadConfig()


def get_log(log_name):


    my_logger=logging.getLogger(log_name) #定义一个日志收集器
    my_logger.setLevel('DEBUG')  #定义收集器的级别

    fmt=logging.Formatter('%(asctime)s-%(levelname)s-%(name)s-日志信息：%(message)s-(%(filename)s:%(lineno)d)') #设置格式

    ch=logging.StreamHandler() #创建一个输出到控制台的渠道
    level=conf.get('LogLevel','console')#从配置文件获取级别
    ch.setLevel(level)
    ch.setFormatter(fmt) #设置输出格式

    file_name = os.path.join(contants.log_path, 'case.log')
    file_handler= logging.handlers.RotatingFileHandler(file_name,maxBytes=20*1024*1024,backupCount=10) #创建一个输出到指定文件的渠道
    #RotatingFileHandler相对于FileHandler,可以对日志进行清理的操作，更优化
    level=conf.get('LogLevel','file')#从配置文件获取级别
    file_handler.setLevel(level)
    file_handler.setFormatter(fmt) #设置输出格式

    my_logger.addHandler(file_handler) #匹配上日志与日志输出渠道
    my_logger.addHandler(ch)

    return my_logger

my_logger= get_log('invest')

my_logger.info('this is a invest log info')



