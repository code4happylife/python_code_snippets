# encoding: utf-8
'''
@author: developer
@software: python
@file: unittest_demo.py
@time: 2022/2/17 19:53
@desc:
'''

import unittest
import requests


class TestInterface(unittest.TestCase):
    #获取token
    def setUp(self):
        data = {'username': 'admin', 'password': '123456'}
        r = requests.post("http://127.0.0.1:8888/users/login", data)
        token = r.token
        bearToken = 'Bearer ' + token
        self.headers = {'Authorization': bearToken}

    def tearDown(self):
        pass

    # 测试登陆接口
    def test_login(self):
        data = {'username': 'admin', 'password': '123456'}
        r = requests.post("http://127.0.0.1:8888/users/login", data)
        self.assertEqual(r.status_code, 200)

    # 测试项目创建接口
    def test_create_project(self):
        data = {'name': '项目', 'desc': '该项目将提升自己的工程能力'}
        r = requests.post("http://127.0.0.1:8888/projects", data, headers=self.headers)
        self.assertEqual(201, r.status_code)
        self.assertEqual(r.desc, '该项目将提升自己的工程能力')

    # 测试环境创建接口
    def test_create_environment(self):
        data = {'name': '阿里云', 'host': 'http://test.api.com/test1', 'db_config': {}, 'project': 1}
        r = requests.post("http://127.0.0.1:8888/environments", data, headers=self.headers)
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.host, 'http://test.api.com/test1')


if __name__ == '__main__':
    unittest.main()
