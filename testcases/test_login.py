# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/3/28 21:58
# File   : test_login.py
# IDE    : PyCharm

import unittest
from libext.ddt import ddt,data

from common import contants
from common.do_excel import DoExcel
from common.request_method import RequestMethod
from common.mylog import get_log

logger=get_log('LoginTest')


@ddt
class TestLogin(unittest.TestCase):
    """
    描述登录接口的类
    """
    do_excel = DoExcel(contants.case_file)  # 利用.实现上下级，来引入其他目录下的文件
    cases = do_excel.read_data('login')
    req = RequestMethod()  # 实例化Reqeust类的对象

    def setUp(self):
        pass

    @data(*cases)

    def test_login(self,case):

        resp = self.req.request_method(case.method, case.url, case.data)  # 返回请求结果
        logger.info("case.expected:{}".format(case.expected))
        try:
            self.assertEqual(resp.text,case.expected,"Login Error")
            self.do_excel.write_data('login', case.case_id + 1, resp.text, 'PASS')
            logger.info("第{0}条用例测试结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_data('login', case.case_id + 1, resp.text, 'FAIL')
            logger.error("第{0}条用例测试结果：FAIL".format(case.case_id))
            raise e

    def  tearDown(self):
        pass


