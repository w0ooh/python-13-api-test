# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2019/12/20 22:39
# File   : contants.py
# IDE    : 常量

#常量：不变的变量，可以封装起来，方便调用

import os

print(os.path.abspath(__file__)) #当前文件所在目录
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #工程的根目录路径存放在变量base_dir
#print(base_dir) #/Users/wanghua/PycharmProjects/python13-api-test
data_dir=os.path.join(base_dir,"datas")
case_file=os.path.join(data_dir,"cases.xlsx")
#print(case_file) #/Users/wanghua/PycharmProjects/python13-api-test/datas/case.xlsx
#这样每次要使用我们的excel数据表格时，可以直接调用这个变量

conf_dir=os.path.join(base_dir,"conf")
test_conf=os.path.join(conf_dir,"test.conf")  #测试配置文件路径
test_conf2=os.path.join(conf_dir,"test2.conf")
global_conf=os.path.join(conf_dir,"global.conf")

log_path=os.path.join(base_dir,'log')
print(log_path)

testcases_dir=os.path.join(base_dir,'testcases') #测试类的目录

reports_dir=os.path.join(base_dir,'reports') #报告文件夹的目录
reports_html=os.path.join(reports_dir,'reports.html') #报告的目录
