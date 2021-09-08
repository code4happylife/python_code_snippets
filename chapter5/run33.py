# encoding: utf-8
'''
@author: developer
@software: python
@file: run33.py
@time: 2021/8/18 22:51
@desc:
'''

'''
描述
输入一行字符，统计出其中数字字符的个数。

输入
一行字符串，总长度不超过255。
输出
输出为1行，输出字符串里面数字字符的个数。
样例输入
Peking University is set up at 1898.
样例输出
4
'''
input_str = input()
num_of_number = 0

for ch in input_str:
    if 48 <= ord(ch) <= 57:
        num_of_number += 1

print(num_of_number)
