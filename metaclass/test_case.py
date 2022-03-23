#!/usr/bin/env python
# encoding: utf-8

import HttpTestBase, MetaTestCase


class TestLogin(HttpTestBase, metaclass=MetaTestCase):
    datas = [
        {'title': '用例1', 'url': 'http://www.baidu.com'},
        {'title': '用例2', 'url': 'http://www.baidu.com'},
        {'title': '用例3', 'url': 'http://www.baidu.com'},
        {'title': '用例4', 'url': 'http://www.baidu.com'}

    ]
