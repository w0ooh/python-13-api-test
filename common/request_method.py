# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2019/12/18 22:40
# File   : request_method.py
# IDE    : PyCharm

import requests
from common.mylog import get_log
logger=get_log('request')

#封装方法一:实例化session来传递cookies
class RequestMethod:

    def __init__(self):
        self.session=requests.sessions.session() # 创建一个session对象

    def request_method(self,method,url,data=None):
        method=method.upper()  # 将method全部转化为大写字母，含括所有情况：get/GET/post/POST

        if data is not None and type(data) == str:
            data=eval(data)  # excel读取的数据都是字符串，需要转换成字典的格式传入
        logger.info('method:{},url:{}'.format(method,url))
        logger.info('data:{}'.format(data))

        if method=='GET':
            resp= self.session.request(method,url=url,params=data)
            logger.info('response:{}'.format(resp.text))
            return resp

        elif method=='POST':
            resp= self.session.request(method,url=url,data=data)
            logger.info('response:{}'.format(resp.text))
            return resp
        else:
            logger.info('Un-supported request method!!!')

    def close(self):
        self.session.close()


if __name__=='__main__':

    r=RequestMethod()
    resp=r.request_method(method='get',url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                          data={'mobilephone':'13522450475','pwd':'123456'})
    print(resp.text)


#封装方法二,手动传递cookies
# class RequestMethod:
#
#     def __init__(self,method,url,data=None,cookies=None):
#         self.method=method
#         self.url=url
#         self.data=data
#         self.cookies=cookies
#
#     def request_method(self):
#         self.method=self.method.upper()
#
#         if self.data is not None and type(self.data)==str:
#             self.data=eval(self.data)  # 看视频实战三 获取和解析 json和dict
#
#         if self.method=='GET':
#             return requests.get(url=self.url,params=self.data,cookies=self.cookies)
#         elif self.method=='POST':
#             return requests.post(url=self.url, data=self.data, cookies=self.cookies)
#         else:
#             print('Un-supported method!!!')
#
# if __name__=='__main__':
#     r=RequestMethod(method='get',url='http://test.lemonban.com/futureloan/mvc/api/member/login',data={'mobilephone':'13522450475','pwd':'1234567a'})
#     resp=r.request_method()
#     print(resp)

