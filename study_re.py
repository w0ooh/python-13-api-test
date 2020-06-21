# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/4/21 14:52
# File   : study_re.py
# IDE    : PyCharm

import json
import re

# print(re.match('com','www.runoob.com'))  #re.match()是尝试从起始位置进行匹配，如果不是起始位置匹配成功就返回none
# print(re.search('com','www.runoob.com')) #扫描整个字符串并返回第一个成功的匹配

admin_user = '13522450475'
admin_pwd = '123456'
s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'

# 方法一
# dict1=json.loads(s) #将字符串转换成字典
# if dict1['mobilephone'] == '${admin_user}':
#     dict1['mobilephone'] = admin_user
# if dict1['pwd']=="${admin_pwd}":
#     dict1['pwd'] = admin_pwd
# print(dict1)

#方法二
# if s.find("${admin_user}")> -1 :
#     s=s.replace("${admin_user}",admin_user) #使用replace函数一定要将替换后的字符串重新赋值一遍，否则打印的还是原来没有替换的
#
#     print(s)



#方法三 ：用正则: 用于在某大段字符串里查找特定的字符串： 重点掌握：'.','*','\d',
data= {"admin_user":'13522450475',"admin_pwd":'123456'}
# m=re.search("\$\{admin_user}",s) #最前端是$,需要转义，让正则知$是一个符号
# print(m)
#method 1.原本字符查找
# p = '\$\{admin_user}'
#method 2.元字符和限定符查找
# p1="\$\{(.*?)}" #用括号表示至少找出一组，*任意字符，但是以${为开头，}为结束的组
# m=re.search(p1,s)  #找到一个匹配项，就返回。只会输出一个或者none
# print(m)  #返回的m是一个对象
# g1=m.group(1)
# g2=m.group(0)
# 返回的是匹配的字符串 1.group(0)返回匹配的整个字符串，group(1)返回第一个括号里匹配的字符串
# print(g1)
# print(type(g1))
# print(g2)
# value=data[g1] # 通过key来取值
# print(value)
# s=re.sub(p1,value,s,count=1) #sub默认是先使用findall的规则来全部匹配一次，找出所有的匹配字符串，用count参数来控制使用value替换几个
# print('使用正则表达式，进行查找并替换',s)
#
# l= re.findall(p1,s) #查找所有匹配的字符串，返回一个列表，没有找到返回空列表
# print('使用findall查找匹配的字符串',l)