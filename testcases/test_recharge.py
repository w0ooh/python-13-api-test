# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/3/28 21:58
# File   : test_login.py
# IDE    : PyCharm


#1.excel 设计用例第一条是正常登陆
#2.使用session保持对话的方式来进行请求，那就需要把request的实例化对象放到类里面，
# 只实例化一次对象，一个session然后进行所有的接口测试
#3.执行用例
import unittest
from common import contants
from common.do_excel import DoExcel
from common.request_method import RequestMethod
from libext.ddt import ddt,data
from common import config
from common.mylog import get_log

logger=get_log('case')


@ddt
class TestRecharge(unittest.TestCase):
    """
    充值接口的测试类
    """
    do_excel = DoExcel(contants.case_file)  # 利用.实现上下级，来引入其他目录下的文件
    cases = do_excel.read_data('recharge2')
    # req = RequestMethod()  # 实例化Reqeust类的对象，放在类里面，而不是tes_方法里面

    @classmethod
    def setUpClass(cls):
        # setUpClass(cls)是unittest里的类方法，一个类执行一次。如果是测试类前都想执行一次的操作，可以放在这个方法里，
        cls.req = RequestMethod()  # 实例化Reqeust类的对象

    def setUp(self):
        pass

    @data(*cases)
    def test_recharge(self,case):
        conf=config.ReadConfig()
        pre_url=conf.get('API','pre_url')
        #print(pre_url)
        resp = self.req.request_method(case.method, pre_url+case.url, case.data)  # 返回请求结果
        logger.info("case.expected:{}".format(case.expected))
        try:
            self.assertEqual(case.expected,resp.json()['code'],"recharge error")
            self.do_excel.write_data('recharge', case.case_id + 1, resp.text, 'PASS')
            logger.info("这是第{}条用例测试结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_data('recharge', case.case_id + 1, resp.text, 'FAIL')
            logger.error("这是第{}条用例测试结果：FAIL".format(case.case_id))
            # print('case.expected:',type(case.expected))
            # print("resp.json()['code']",type(resp.json()['code']))
            raise e
    def  tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.req.close() # 有时候会提示资源未关闭。session建立后，用完需要关闭





