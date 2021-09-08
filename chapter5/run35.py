# encoding: utf-8
'''
@author: developer
@software: python
@file: run35.py
@time: 2021/8/22 10:27
@desc:
'''

'''
描述
一个句子中也许有多个连续空格，过滤掉多余的空格，只留下一个空格。

输入
一行，一个字符串（长度不超过200），句子的头和尾都没有空格。
输出
过滤之后的句子。
样例输入
Hello      world.This is    c language.
样例输出
Hello world.This is c language.
'''

import re

str_test = input()

result = re.sub(r'\s+', ' ', str_test)
print(result)
