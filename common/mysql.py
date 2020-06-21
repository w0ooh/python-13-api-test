# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/4/5 23:04
# File   : mysql.py
# IDE    : PyCharm

#1. 建一次连接，每次查询后，关闭查询，关闭数据库

#2. 也可以建一次连接，建立一次查询，在这一个查询里完成所有的操作，然后关闭查询关闭数据库，
#  这样就需要将cursor写在初始化函数内，关闭查询的cursor.close（）可以写在 def close() 函数中，统一全部关闭

import pymysql
from common import contants
import configparser
from common import config

class MysqlUtil:

    '''
    数据库查询的类
    '''

    def __init__(self): #千万要注意init容易写成int，会报错，找不到定义的实例变量
        # host = "test.lemonban.com"
        # user = "test"
        # password = "test" #这样写死了 万一有两个或多个数据库环境，就需要改代码。
        # self.mysql=pymysql.connect(host,user,password,port=3306)
        conf=config.ReadConfig()   #读取响应配置中的数据库设置，可以自由更换数据库环境。
        host =conf.get('DB','host')
        user = conf.get('DB', 'user')
        password = conf.get('DB', 'password')
        port =conf.getint('DB','port')
        self.mysql = pymysql.connect(host=host,user=user,password=password, port=port) #建立连接

    def fetch_one(self,sql):
        cursor=self.mysql.cursor() #实例化一个查询
        cursor.execute(sql) #执行查询
        result=cursor.fetchone() #获取结果
        cursor.close() #关闭查询
        return result  #返回查询结果

    def close(self):
        self.mysql.close()  #关闭数据库


if __name__== '__main__':
    mysql=MysqlUtil()
    sql="select max(mobilephone) from future.member"
    result=mysql.fetch_one(sql)
    print(type(result[0]),result[0])
    mysql.close()


