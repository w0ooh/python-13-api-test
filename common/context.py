# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/4/24 21:55
# File   : context.py  #正则
# IDE    : PyCharm

d= {"admin_user":'13522450475',"admin_pwd":'123456'}
s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'

#s:需要替换的目标字符串
#d:用来替换的内容
# 用正则去匹配需要替换的目标字符串，提取字符串
# 用re.search提取的字符串作为key,在字典d内进行取值，去到了用来替换的值
# 用re.sub进行匹配并替换

import re  #导入正则模块
from common import config

#
# def replace(s, d): #传两个参数 方法一只用正则来替换参数的值
#     p = '\$\{(.*?)}' #定义正则表达式
#     while re.search(p, s) is not None: #一旦找不到匹配的，循环停止
#         m = re.search(p, s) #按照p去字符串s中匹配，找到第一个，返回对象m
#         g = m.group(1)  #提取字符串
#         value = d[g]    # 通过提取的字符串去字典d中查找key
#         s = re.sub(p, value, s, count=1) #替换
#     return s
#
#
# d = {"admin_user": '13522450475', "admin_pwd": '123456'}

# s = replace(s, d)
# print(s)

# 方法二 使用反射来进行替换参数的值
conf = config.ReadConfig()
class Context:

    admin_user = conf.get('DATA','admin_user')
    admin_pwd = conf.get('DATA','admin_pwd')
    loan_member_id=conf.get('DATA','loan_member_id')
    normal_user=conf.get('DATA','normal_user')
    normal_pwd=conf.get('DATA','normal_pwd')
    normal_member_id=conf.get('DATA', 'normal_member_id')



def replace_new(s):

    p = '\$\{(.*?)}'  # 定义正则表达式
    while re.search(p, s) is not None:  # 一旦找不到匹配的，循环停止
        m = re.search(p, s)  # 按照p去字符串s中匹配，找到第一个，返回对象m
        g = m.group(1)  # 提取字符串
        if hasattr(Context,g):
            value = getattr(Context,g)  # 利用反射动态获取了Context属性值
            s = re.sub(p, value, s, count=1)  # 替换
        else:
            return None
    return s

s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'

s= replace_new(s)
print(s)

