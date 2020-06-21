# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/6/4 23:25
# File   : test_invest.py
# IDE    : PyCharm

# 将已有的数据的参数，直接通过context类，进行替换。需要通过完成其他步骤获取的值，可以通过数据库查询后替换。
import unittest
from libext.ddt import ddt, data

from common import contants
from common.do_excel import DoExcel
from common.request_method import RequestMethod
import json
from common import config
from common import context
from common.mysql import MysqlUtil


@ddt
class TestInvest(unittest.TestCase):
    """
    充值接口的测试类
    """
    do_excel = DoExcel(contants.case_file)  # 利用.实现上下级，来引入其他目录下的文件
    cases = do_excel.read_data('invest')
    # req = RequestMethod()  # 实例化Reqeust类的对象，放在类里面，而不是tes_方法里面

    @classmethod
    def setUpClass(cls):
        # setUpClass(cls)是unittest里的类方法，一个类执行一次。如果是测试类前都想执行一次的操作，可以放在这个方法里，
        cls.req = RequestMethod()  # 实例化Reqeust类的对象
        cls.mysql=MysqlUtil()  #实例化MysqlUtil类对象


    def get_amount(self):
        phonenumber = getattr(context.Context, 'normal_user')
        sql= "select LeaveAmount from future.member where MobilePhone= '{0}'".format(phonenumber)
        amount = self.mysql.fetch_one(sql)[0]
        return amount

    def setUp(self):
        pass



    @data(*cases)
    def test_invest(self,case):

        conf=config.ReadConfig()
        pre_url=conf.get('API','pre_url')
        print(pre_url)
        #查找参数化的测试数据，动态替换.使用context类.
        case.data_new = context.replace_new(case.data)

        #使用封装好的request类来完成请求
        resp = self.req.request_method(case.method, pre_url+case.url, case.data_new)  # 返回请求结果
        print("case.expected:{}".format(case.expected))
        try:
            self.assertEqual(case.expected,resp.json()['code'],"invest error")
            self.do_excel.write_data('invest', case.case_id + 1, resp.text, 'PASS')

            #判断是否加标成功，如果加标成功就去查找加标的标id,然后获取loan_id
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(context.Context,'loan_member_id')
                sql="select id from future.loan where memberId= '{0}'" \
                    " order by CreateTime desc limit 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0]
                setattr(context.Context,'loan_id',str(loan_id))# 转化为str,后续正则只处理字符串

            # if resp.json()['msg'] =='竞标成功':
            #     leaveamount = self.get_amount()
            #     try:
            #         self.assertEqual(str(self.setUp().amount),str(leaveamount+100),'amount error')
            #     except AssertionError as e:
            #         raise e




        except AssertionError as e:
            self.do_excel.write_data('invest', case.case_id + 1, resp.text, 'FAIL')

            print('case.expected:',type(case.expected))
            print("resp.json()['code']",type(resp.json()['code']))
            raise e
    def  tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.req.close() # 有时候会提示资源未关闭。session建立后，用完需要关闭
        cls.mysql.close() #关闭数据库

