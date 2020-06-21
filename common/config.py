# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/4/11 22:18
# File   : config.py
# IDE    : PyCharm
from common import contants
import configparser  #解析配置文件的模块
# #1,实例化对象，是通过对象来完成配置文件的解析
# config = configparser.ConfigParser()
# #2.加载文件
# config.read(contants.test_conf)
# #3.获取配置文件里的值
# value= config.get('API','pre_url')
# print(type(value),value)  # 返回的value是字符串类型

class ReadConfig:
    """
    读取配置文件
    """

    def __init__(self):

        self.config=configparser.ConfigParser() #实例化对象
        self.config.read(contants.global_conf)  #读取开关配置
        conf=self.config.getboolean('switch','open') #获取开关的值
        #print(type(conf),conf)
        if conf:
            self.config.read(contants.test_conf)  #如果为真，则加载test_conf
        else:
            self.config.read(contants.test_conf2) #如果为假，则加载test_conf2

    # def read_url(self):
    #     res = self.config.get("API", 'pre_url')  # 获取响应配置的option值 ，返回
    #     return res
    #
    # def read_db(self):
    #     host=self.config.get('DB','host')   #从配置文件中读取内容
    #     user = self.config.get('DB', 'user')
    #     pwd = self.config.get('DB', 'password')
    #     port = self.config.getint('DB', 'port')
    #     return host,user,pwd,port

    #按照老师的思路，将以上读取的两个函数整体封装为一个函数,更为简洁，高效
    def get(self,section,option):
        value=self.config.get(section,option)
        return value

    def getboolean(self, section, option):
        value = self.config.getboolean(section, option)
        return value

    def getint(self, section, option):
        value = self.config.getint(section, option)
        return value


if __name__=="__main__":
    conf=ReadConfig()
    res=conf.get('DB','host')
    es = conf.get('DB', 'host')
    print(type(res),res)
