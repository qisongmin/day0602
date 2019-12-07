from HTMLTestRunner import HTMLTestRunner
import unittest
import time
# from script.test_ihrm_emp import TestEmp
from script.test_ihrm_emp_parameterized import TestEmp_parameterized
from script.test_login import TestLogin
#
# from script.test_login_parameterized import TestLogin_parameterized
# 实例化测试套件
suite=unittest.TestSuite()
# 组织用例套件
suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestEmp))

# suite.addTest(unittest.makeSuite(TestLogin_parameterized))
suite.addTest(unittest.makeSuite(TestEmp_parameterized))

# 报告保存路径
aaa= "./report/ihtm{}.html".format(time.strftime("%Y%m%d %H%M%S"))
with open(aaa,mode="wb") as f:
    runner=HTMLTestRunner(f,verbosity=1,title="IHRM测试报告",description="登录接口")
    runner.run(suite)