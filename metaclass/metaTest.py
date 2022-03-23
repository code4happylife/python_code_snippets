#!/usr/bin/env python
# encoding: utf-8


import unittest


def create_new_case_method(case_method, item):
    def wrapper(self):
        print("用例执行的--wrapper--")
        case_method(self, item)

    return wrapper


class MetaTestCase(type):

    def __new__(cls, name, bases, attrs, *args, **kwargs):
        """"""
        # 创建类
        new_cls = super().__new__(cls, name, bases, attrs, *args, **kwargs)
        for index, item in enumerate(getattr(new_cls, 'datas')):
            case_name = 'test_demo_{}'.format(index + 1)
            case_method = getattr(new_cls, 'execute_case')
            wrapper = create_new_case_method(case_method, index)

            # 遍历数据动态生成测试用例
            setattr(new_cls, case_name, wrapper)
        return new_cls


class HttpTestBase(unittest.TestCase):
    def execute_case(self, item):
        """
        1,处理用例数据
        2，发送请求
        3，提取响应中的依赖数据保存
        4，断言
        :return:
        """
        self.__handle_data()
        self.__send_request()
        self.__response_data_handle()
        self.__assertion()
        print(item)

    def __handle_data(self):
        print("处理用例数据")

    def __send_request(self):
        print("发送请求")

    def __response_data_handle(self):
        print("响应数据提取")

    def __assertion(self):
        print("断言")
        self.assertTrue(True)
