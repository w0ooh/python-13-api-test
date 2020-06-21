# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/3/28 22:26
# File   : test_API.py
# IDE    : PyCharm
import unittest
from common import contants
from common.do_excel import DoExcel
from common.request_method import RequestMethod
from ddt import ddt,data
from common.mysql import MysqlUtil

@ddt
class TestLogin(unittest.TestCase):
    """
    描述登录接口的类
    """
    do_excel = DoExcel(contants.case_file)  # 利用.实现上下级，来引入其他目录下的文件
    cases = do_excel.read_data('login') # 获取表单
    req = RequestMethod()  # 实例化Reqeust类的对象

    def setUp(self):
        pass

    @unittest.skip("不跑这个接口")
    @data(*cases)

    def test_login(self,case):

        resp = self.req.request_method(case.method, case.url, case.data)  # 返回请求结果
        print("case.expected:{}".format(case.expected))
        try:
            self.assertEqual(resp.text,case.expected,"Login Error")
            self.do_excel.write_data('login', case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.do_excel.write_data('login', case.case_id + 1, resp.text, 'FAIL')
            raise e

    def  tearDown(self):
        pass



@ddt
class TestRegister(unittest.TestCase):
    """
    描述登录接口的类
    """
    do_excel = DoExcel(contants.case_file)  # 利用.实现上下级，来引入其他目录下的文件
    cases = do_excel.read_data('register')
    req = RequestMethod()  # 实例化Reqeust类的对象

    mysql = MysqlUtil()  #实例化对象
    sql = "select max(mobilephone) from future.member" #sql查询语言
    max = mysql.fetch_one(sql)[0] #调用fetch_one(sql)获取查询结果，结果是元组，用索引取值
    mysql.close()

    def setUp(self):
        # Setup(self)是unittest里的方法，执行一次test_方法这个setup执行一次。
        # 如果是每条用例测试前都想执行一次的操作，可以放在这个方法里
        pass

    @data(*cases)
    def test_register(self,case):
        import json
        case_dict=json.loads(case.data) #json.loads()将传进来的data字符串转化为字典
        if case_dict['mobilephone']=='phonenumber':  #通过字典关键字取值做判断
            case_dict['mobilephone']=int(self.max)-319 #重新给这个注册的号码赋值为数据库中唯一的一个值
            print((int(self.max)-319))
        resp = self.req.request_method(case.method, case.url, case_dict)  # 返回请求结果
        print("case.expected:{}".format(case.expected))
        try:
            self.assertEqual(resp.text,case.expected,"register Error")
            self.do_excel.write_data('register', case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.do_excel.write_data('register', case.case_id + 1, resp.text, 'FAIL')
            raise e

    def  tearDown(self):
        pass

