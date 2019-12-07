import logging

import requests


class LoginApi:
    def __init__(self):
        self.login_url = "http://182.92.81.159" + "/api/sys/login"
        self.headers = {"Content-Type": "application/json"}
        pass

    def login(self, mobile, password):
        logging.info("登录手机号码：{}".format(mobile))
        login_data = {
            "mobile": mobile,
            "password": password
        }
        return requests.post(self.login_url, json=login_data, headers=self.headers)

    def no_Params(self):
        return requests.post(self.login_url, headers=self.headers)

    def extra_Params(self):
        return requests.post(self.login_url, json={"mobile": "13800000002", "password": "123456", "extra": "ninhao"
                                                   }, headers=self.headers)

    def less_Params(self):
        return requests.post(self.login_url, json={"mobile": "13800000002"}, headers=self.headers)
