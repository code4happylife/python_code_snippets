# encoding: utf-8
'''
@author: developer
@software: python
@file: run46.py
@time: 2021/8/29 11:59
@desc:
'''

'''
描述
给定一个字符串，输出所有长度至少为2的回文子串。

回文子串即从左往右输出和从右往左输出结果是一样的字符串，比如：abba，cccdeedccc都是回文字符串。

输入
一个字符串，由字母或数字组成。长度500以内。
输出
输出所有的回文子串，每个子串一行。
子串长度小的优先输出，若长度相等，则出现位置靠左的优先输出。
样例输入
123321125775165561
样例输出
33
11
77
55
2332
2112
5775
6556
123321
165561
'''


def huiwen(str_test):
    if str_test == str_test[::-1]:
        return True
    else:
        return False


input_str = input()
result_str = []

str_len = len(input_str)

for sub_len in range(2, str_len):
    for start_index in range(0, str_len - sub_len + 1):
        if huiwen(input_str[start_index: start_index + sub_len]):
            result_str.append((input_str[start_index: start_index + sub_len], sub_len, start_index))

if huiwen(input_str):
    result_str.append((input_str, str_len, 0))

result_str.sort(key=lambda x: (x[1], x[2]))

for i in range(len(result_str)):
    print(result_str[i][0])

