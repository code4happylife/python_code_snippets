#!/usr/bin/env python
# encoding: utf-8


"""
自定义一个类
    1、通过上课的相关知识点对这个类创建的对象，进行属性限制，对象只能设置这个三个属性：  title    money   data
    2、通过相关机制对设置的属性类型进行限制，title只能设置字符串类型数据
    money设置为int类型数据  data可以设置为任意类型
    3、通过相关机制实现，data 属性不能进行删除
    4、当money属性不存在时，查询出来的结果显示为0，
"""


class TestDemo(object):
    __slots__ = ['title', 'money', 'data']

    def __setattr__(self, key, value):
        if key == 'title':
            if isinstance(value, str):
                super().__setattr__(key, value)
            else:
                raise TypeError("title属性只能设置为字符串类型")
        elif key == 'money':
            if isinstance(value, int):
                super().__setattr__(key, value)
            else:
                raise TypeError("money属性只能设置为int类型")
        else:
            super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'data':
            raise AttributeError("data属性不支持删除")

    def __getattr__(self, item):
        if item == 'money':
            return 0


t = TestDemo()
t.title = 'developer'
# t.money = 1000
t.data = 'nice'

# t.title = 1000  # TypeError: title属性只能设置为字符串类型

# t.money = 'developer' #TypeError: money属性只能设置为int类型

# del t.data #AttributeError: data属性不支持删除
print(t.money)  # 0
