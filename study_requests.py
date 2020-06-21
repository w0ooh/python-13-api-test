# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2019/11/15 22:34
# File   : study_requests.py
# IDE    : PyCharm

# import requests
#构造请求
# resp= requests.get('http://cn.python-requests.org/zh_CN/latest/')
# resp.encoding='utf-8'#解决乱码问题
# print('响应码',resp.status_code)
# print("响应信息",resp.text)
# with open('index.html','w+',encoding='utf-8') as file: #输出到文件
#     file.write(resp.text)

# 登录接口--GET--url传参--params
# data={'mobilephone':'13522450475',"pwd":'123456'} #要用字典的格式来传参
# resp= requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=data)
#
# print('响应码',resp.status_code)#获取状态码
# print("响应信息",resp.text) #获取响应信息
# print("url",resp.request.url) #响应信息URL，参数传到URL末尾

#登录接口--POST--表单传参--data
# data={'mobilephone':'13522450475',"pwd":'123456'} #要用字典的格式来传参
# resp= requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',data=data)
###查看所有请求的信息
# print("请求url",resp.request.url) #查看响应信息URL
# print("请求参数",resp.request.body) #参数会传到请求信息的body里
# print("请求cookies",resp.request._cookies) #查看响应信息URL
# #_cookies 前加上'_'是因为cookies是被保护的，不加会报错。可以通过debug查看哪些参数是被保护的。
# print("请求headers",resp.request.headers) #参数会传到请求信息的body里
# ###查看所有响应信息
# print('响应码',resp.status_code)#获取状态码
# print("响应信息",resp.text) #获取响应信息
# print('响应cookies',resp.cookies)
# print('响应header',resp.headers)

# print("响应信息",resp.text) #获取响应信息
# print(type(resp.text))
# print("响应信息",resp.json())#获取响应信息字典格式
# print(type(resp.json()))



#########homework############
#使用requests完成其中注册，登录，充值接口的调用 （温馨提示，充值需要传登录之后返回的cookies）
import requests

# #注册接口
# data={'mobilephone':'13522450475','pwd':'123456','regname':'nicole'}
# resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/register',data=data)
# print("响应状态",resp.status_code)
# print("响应信息",resp.json())
# print("响应cookies",resp.cookies)
# print("响应cookies",resp.headers)
#
#登录接口
# data_1={'mobilephone':'13522450475','pwd':'123456'}
# resp_1=requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=data_1)
# print("响应状态",resp.status_code)
# print("响应信息",resp.json())
# print("响应cookies",resp.cookies)
# print("响应cookies",resp.headers)

# cok=resp_1.cookies
# #充值接口方法一 传入登录会话的cookies
# data={'mobilephone':'13522450475','amount':'20000'}
# resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge',data=data,cookies=cok)
# print("响应状态",resp.status_code)
# print("响应信息",resp.json())   # ----- resp.text是字符串格式，但是内容其实是一个json格式，用resp.json()直接变为字典格式，可以进行取值
# print("响应cookies",resp.cookies)
# print("响应cookies",resp.headers)
# print("响应body",resp.request.body)

#充值接口方法二  用session创建一个对象，然后进行调用request
session=requests.sessions.Session()
# data={'mobilephone':'13522450475','pwd':'123456'}
# resp=session.request('post','http://test.lemonban.com/futureloan/mvc/api/member/login',data=data)
# print(resp.text)
#
# data= {'mobilephone':'13522450475','amount':'100'}
# resp=session.request('post','http://test.lemonban.com/futureloan/mvc/api/member/recharge',data=data)
# print(resp.text)






