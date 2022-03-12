#!/usr/bin/env python
# encoding: utf-8


"""
1、现有有如下功能函数：
def work(a,b):
    res = a+b
    print('a+b的结果为:',res)
# 调用函数当参数类型不能进行相加时，work执行会报错！如：work(10,‘a’)
# 需求：在不更改函数代码的前提现，实现调用work函数传入不同类型的参数是函数不报错，输出结果：您传入的参数类型不一样，无法正常执行

2、实现一个函数执行报错，自动重新执行的装饰器，
要被装饰的函数执行出现AssertionError，则重新再执行一次该函数，如果还是执行出现AssertionError，则抛出异常
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        if type(args[0]) != type(args[1]):
            print("您传入的参数类型不一样，无法正常执行")
        else:
            func(*args, **kwargs)

    return wrapper


@decorator
def work(a, b):
    res = a + b
    print('a+b的结果为:', res)


work(10, 'a')
work(10, 10)
work('ss', 'ss')
work([1, 2, 3], [4, 5, 6])

"""
运行结果：
您传入的参数类型不一样，无法正常执行
a+b的结果为: 20
a+b的结果为: ssss
a+b的结果为: [1, 2, 3, 4, 5, 6]
"""

'''
2、实现一个函数执行报错，自动重新执行的装饰器，
要被装饰的函数执行出现AssertionError，则重新再执行一次该函数，如果还是执行出现AssertionError，则抛出异常
'''


def deco(func):
    def wrapper(*args, **kwargs):
        for i in range(2):
            try:
                res = func(*args, **kwargs)
            except AssertionError as e:
                if i == 1:
                    raise e
            else:
                return res

    return wrapper


@deco
def test(a, b):
    print("判断a和b是否相等")
    assert a == b


# test(1, 1)
test(1, 1)
test(1, 100)

"""
运行结果：
判断a和b是否相等
判断a和b是否相等
判断a和b是否相等
    assert a == b
AssertionError
"""
