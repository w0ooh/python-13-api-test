# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/3/25 22:24
# File   : requestmethod.py
# IDE    : PyCharm

import requests


class RequestMethod:

    def __init__(self):
        self.session = requests.sessions.session()  # 实例化一个session

    def request_method(self, method, url, data=None):
        method = method.upper()  # 将字符转成全部大写

        if data is not None and type(data) == str:
            data = eval(data)  # 转变为字典格式，excel读取出来都是字符串格式。

        if method == 'GET':
            resp = self.session.request(method, url=url, params=data)  # 调用get方法，使用params传参
            print('response:{0}'.format(resp.text))
            return resp

        elif method == 'POST':
            resp = self.session.request(method, url=url, data=data)
            print('response:{}'.format(resp.text))
            return resp
        else:
            print('un-supported request method !!!')

    def close(self):
        self.session.close()  # 关闭对话
