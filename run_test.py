# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/6/17 22:43
# File   : run_test.py
# IDE    : PyCharm

import unittest
from common import contants
import HTMLTestRunnerNew
from testcases import test_login
from testcases.test_invest import TestInvest
from testcases.test_recharge import TestRecharge

# *****之前的写法****
# suite=unittest.TestSuite() #创建测试用例集合
#
# loader= unittest.TestLoader() #加载用例
#
#
# suite.addTest(loader.loadTestsFromModule(test_login))  #以模块加载到用例集合suite中
# suite.addTest(loader.loadTestsFromTestCase(TestRecharge)) #以类加载到用例集合suite中
#
# runner=unittest.TextTestRunner()
# runner.run(suite)
#**********************

#testcases目录下，查找以test开头的.py文件里的所有测试类
discover=unittest.defaultTestLoader.discover(contants.testcases_dir,pattern='test_*.py',top_level_dir=None)

with open(contants.reports_html,'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='API',
                                              description='API测试报告',
                                              tester='hua')
    runner.run(discover)  # 执行测试集里面的用例
