#!/usr/bin/env python
# encoding: utf-8
'''
@file: myClass.py
@time: 2022/1/30 11:31 上午
@desc:
'''


class MyClass(object):
    __slots__ = ['title', 'money', 'data']

    def __init__(self, title=None, money=None, data=None):
        self.title = title
        self.money = money
        self.data = data

    # 通过__setattr__方法限制对象的各个属性的数据类型
    def __setattr__(self, key, value):
        if key == 'title':
            if isinstance(value, str):
                object.__setattr__(self, key, value)
            else:
                raise TypeError("title 只能设置为字符串类型~")
        elif key == 'money':
            if isinstance(value, int):
                object.__setattr__(self, key, value)
            else:
                raise TypeError("money 只能设置为int类型~")
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'data':
            raise AttributeError("data属性不能删除")
        else:
            object.__delattr__(self, item)

    # 通过__getattr__方法获取对象的各个属性值
    def __getattr__(self, item):
        if item == 'money':
            value = object.__getattribute__(self, item)
            if value < 0:
                value = 0
            return value
        elif item == 'data':
            value = object.__getattribute__(self, item)
            if value != 'IEEE' or value != 'SCI':
                value = 'IEEE and SCI'
                return value
            else:
                return 'Keep write essays'
        else:
            return object.__getattribute__(self, item)


if __name__ == '__main__':
    m = MyClass('testString', -100, 'Some short papers')
    print(m.__getattr__('title'))
    print(m.__getattr__('money'))
    print(m.__getattr__('data'))

'''
testString
0
IEEE and SCI
'''
