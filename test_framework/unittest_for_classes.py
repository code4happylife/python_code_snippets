#!/usr/bin/env python
# encoding: utf-8



import unittest

from concurrent.futures.thread import ThreadPoolExecutor


class TestRunner:

    def parser_suite(self, suites):
        """

        :param suites: 测试套件
        :return:
        """
        cases_list = []

        def handle_suite(suites):
            for item in suites:
                # 判断是否为测试用例类， 将用例类append到cases_list然后进行遍历执行
                if isinstance(item, unittest.TestCase):
                    # item 为用例
                    return cases_list.append(suites)
                else:
                    handle_suite(item)

        
        handle_suite(suites)
        # print(len(cases_list))
        return cases_list
        # print(cases_list)



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
    runner = TestRunner()
    result = runner.my_run(suite=suite, thread=4)
    print("测试结果：", result)
