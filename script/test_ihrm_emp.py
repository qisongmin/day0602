import unittest
import logging

import pymysql

import app
from api.emp_api import EmpAPI
from utils import assert_common, DBUtils


class TestEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.empapi=EmpAPI()
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass
    #添加员工用例
    def test01_Add_Emp(self):
        response=self.empapi.add_emp("葫芦娃水0220","18898989988")
        assert_common(self,response,200,True,10000,"操作成功")

        #设置新添员工的id为全局变量 供员工查询接口使用

        app.EMPID=response.json().get("data").get("id")
        logging.info("新添加的员工的id为：{}".format(app.EMPID))
    #查询员工用例
    def test02_query_emp(self):
        response=self.empapi.query_emp()
        logging.info('查询员工接口返回的数据：{}'.format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")
    def test03_modify_emp(self):
        response=self.empapi.modify_emp("变形金刚")
        logging.info('员工修改返回的数据：{}'.format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")
        '''
        #建立连接
        conn=pymysql.connect("182.92.81.159","readuser",'iHRM_user_2019',"ihrm")
        #获取游标
        cursor=conn.cursor()
        #查询数据库
        modify_sql="select username from bs_user where id={} limit 1".format(app.EMPID)
        cursor.execute(modify_sql)
        result=cursor.fetchone()
        logging.info("查询的数据库中员工id为{}的username是：{}".format(app.EMPID,result[0]))
        self.assertEqual("变形金刚",result[0])
        cursor.close()
        conn.close()
        '''
        with DBUtils("182.92.81.159","readuser",'iHRM_user_2019',"ihrm") as db:
            modify_sql = "select username from bs_user where id={} limit 1".format(app.EMPID)
            db.execute(modify_sql)
            result = db.fetchone()
        logging.info("---------查询的数据库中员工id为{}的username是：{}".format(app.EMPID, result[0]))
        self.assertEqual("变形金刚", result[0])

    def test04_delete_emp(self):
        response=self.empapi.delete_emp()
        logging.info('员工删除接口返回的数据：{}'.format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")


