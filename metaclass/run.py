#!/usr/bin/env python
# encoding: utf-8

import unittest
from unittestreport import TestRunner, Load

suite = unittest.defaultTestLoader.discover('.', 'test*.py')

TestRunner(suite, templates=2).run()


"""
用例执行的--wrapper--
处理用例数据
发送请求
响应数据提取
断言
{'title': '用例1', 'url': 'http://www.baidu.com'}
test_demo_1 (test_case.TestLogin)执行——>【通过】
用例执行的--wrapper--
处理用例数据
发送请求
响应数据提取
断言
{'title': '用例2', 'url': 'http://www.baidu.com'}
test_demo_2 (test_case.TestLogin)执行——>【通过】
用例执行的--wrapper--
处理用例数据
发送请求
响应数据提取
断言
{'title': '用例3', 'url': 'http://www.baidu.com'}
test_demo_3 (test_case.TestLogin)执行——>【通过】
用例执行的--wrapper--
处理用例数据
发送请求
响应数据提取
断言
{'title': '用例4', 'url': 'http://www.baidu.com'}
test_demo_4 (test_case.TestLogin)执行——>【通过】
所有用例执行完毕，正在生成测试报告中......
测试报告已经生成，报告路径为:./reports/report.html

"""
