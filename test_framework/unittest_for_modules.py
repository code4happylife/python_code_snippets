#!/usr/bin/env python
# encoding: utf-8


import unittest

from concurrent.futures.thread import ThreadPoolExecutor


class TestRunner:
    """
        以模块为单位拆分
    """

    def parser_suite(self, suites):
        """

        :param suites: 测试套件
        :return:
        """
        return list(suites)

    def my_run(self, suite, thread=1):
        cases = self.parser_suite(suite)
        # 测试结果记录器
        result = unittest.TestResult()
        # 遍历测试用例
        with ThreadPoolExecutor(max_workers=thread) as tp:
            for testcase in cases:
                tp.submit(testcase.run, result)
        return result


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('.', 'test*.py')
    # suite 就是模块
    runner = TestRunner()
    result = runner.my_run(suite=suite, thread=4)
    print("测试结果：", result)
