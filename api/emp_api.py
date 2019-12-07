import requests

import app


class EmpAPI:
    def __init__(self):
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"
    #添加员工接口
    def add_emp(self, username, mobile):
        data = {"username": username,
                "mobile": mobile,
                "timeOfEntry": "2019-07-01",
                "formOfEmployment": 1,
                "workNumber": "1322131",
                "departmentName": "开发部",
                "departmentId": "1066240656856453120",
                "correctionTime": "2019-11-30"}
        return requests.post(self.emp_url,json=data,headers=app.HEADERS)
    #查询员工接口
    def query_emp(self):
        query_emp_url=self.emp_url +"/"+app.EMPID
        return requests.get(query_emp_url,headers=app.HEADERS)
    #修改员工接口
    def modify_emp(self,username):
        modify_emp_url=self.emp_url +"/"+app.EMPID
        return requests.put(modify_emp_url,json={"username":username},headers=app.HEADERS)
    def delete_emp(self):
        modify_emp_url=self.emp_url +"/"+app.EMPID
        return requests.delete(modify_emp_url,headers=app.HEADERS)