import json

import pymysql
from requests import Response  # 用于设置下列变量response自动提示

import app

'''
@type response:Response     #用于设置下列变量response自动提示
'''


def assert_common(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


class DBUtils:
    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(host, user, password, database)

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            # __enter__和__exit__这两个魔法函数是python内置函数，是在使用with语法打开对象时要执行的函数
            # 执行顺序：with打开时，执行__enter__函数。退出with时，执行__exit__函数
            # with open(filename,mode="r") as f :pass
            # 引用：with DBUtils() as db:db.excute()


def read_login_data():
    login_data_path = app.BASE_DIR + "/data/login_data.json"
    with open(login_data_path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        result_list = []
        for login_data in jsonData:
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            http_code = login_data.get("http_code")
            success = login_data.get("success")
            code = login_data.get("code")
            message = login_data.get("message")
            result_list.append((mobile, password, http_code, success, code, message))
    return result_list


def read_add_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        result_list = []
        add_emp_data = jsonData.get("add_emp")
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        result_list.append((username, mobile, http_code, success, code, message))
    return result_list


def read_query_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        result_list = []
        query_emp_data = jsonData.get("query_emp")
        http_code = query_emp_data.get("http_code")
        successs = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        result_list.append((http_code, successs, code, message))
    return result_list


def read_modify_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        result_list = []
        modify_emp_data = jsonData.get("modify_emp")
        username = modify_emp_data.get("usename")
        http_code = modify_emp_data.get("http_code")
        successs = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        result_list.append((username, http_code, successs, code, message))
    return result_list


def read_delete_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        result_list = []
        delete_emp_data = jsonData.get("delete_emp")
        http_code = delete_emp_data.get("http_code")
        successs = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        result_list.append((http_code, successs, code, message))
    return result_list

if __name__ == '__main__':
    print(read_add_emp_data())