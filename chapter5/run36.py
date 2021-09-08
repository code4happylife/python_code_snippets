# encoding: utf-8
'''
@author: developer
@software: python
@file: run36.py
@time: 2021/8/22 10:45
@desc:
'''

'''
描述
给定一个只包含小写字母的字符串，请你找到第一个仅出现一次的字符。如果没有，输出no。

输入
一个字符串，长度小于100000。
输出
输出第一个仅出现一次的字符，若没有则输出no。
样例输入
abcabd
样例输出
c
'''


str_seq = input()
flag = False
dict_test = {}

for element in str_seq:
    if element not in dict_test:
        dict_test[element] = 1
    else:
        dict_test[element] += 1


for i in range(len(str_seq)):
    if dict_test[str_seq[i]] == 1:
        flag = True
        print(str_seq[i])
        break

if not flag:
    print("no")
