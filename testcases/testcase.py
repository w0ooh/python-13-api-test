# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2019/12/28 22:44
# File   : testcase.py
# IDE    : PyCharm


#不用unittest方法
from common import contants
from common.request_method import RequestMethod
from common.do_excel import DoExcel

class TestCases:

    def test_case(self,sheet_name):

        do_excel=DoExcel(contants.case_file)  #利用.实现上下级，来引入其他目录下的文件
        cases=do_excel.read_data(sheet_name)

        req=RequestMethod()#实例化Reqeust类的对象
        for case in cases:
            resp= req.request_method(case.method,case.url,case.data) #返回请求结果
            print("case.expected:{}".format(case.expected))
            if resp.text==case.expected:
                do_excel.write_data('login',case.case_id+1,resp.text,'PASS')
            else:
                do_excel.write_data('login',case.case_id+1, resp.text, 'FAIL')

if __name__=='__main__':
    case=TestCases()
    case.test_case(sheet_name='register')
