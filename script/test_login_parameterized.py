import logging
import unittest
# 定义测试类
from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import assert_common, read_login_data


class TestLogin_parameterized(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loginapi = LoginApi()

        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(read_login_data)
    def test01_login(self, mobile, password, http_code, success, code, message):
        response = self.loginapi.login(mobile, password)
        logging.info("登录接口返回的数据为：{}".format(response.json()))
        assert_common(self, response, http_code, success, code, message)

        # jsonData = response.json()
        #
        # # 将令牌设置为全局变量 供员工的增删改查接口使用
        #
        # token = "Bearer " + jsonData.get("data")
        # app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # logging.info("保存登陆的token和content-type：{}".format(app.HEADERS))
    # #
    def test02_No_params(self):
        response = self.loginapi.no_Params()
        logging.info("登录接口返回的数据为：{}".format(response.json()))
        assert_common(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    def test03_extra_params(self):
        response = self.loginapi.extra_Params()
        logging.info("登录接口返回的数据为：{}".format(response.json()))
        assert_common(self, response, 200, True, 10000, "操作成功")

    def test04_less_params(self):
        response = self.loginapi.less_Params()
        logging.info("登录接口返回的数据为：{}".format(response.json()))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")
