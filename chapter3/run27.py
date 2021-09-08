# encoding: utf-8
'''
@author: developer
@software: python
@file: run27.py
@time: 2021/8/7 12:01
@desc:
'''

'''
描述
给定一个整数，请将该数各个位上数字反转得到一个新数。
新数也应满足整数的常见形式，即除非给定的原数为零，
否则反转后得到的新数的最高位数字不应为零（参见样例2）。

输入
输入共 1 行，一个整数N。

-1,000,000,000 ≤ N≤ 1,000,000,000。
输出
输出共 1 行，一个整数，表示反转后的新数。
样例输入
样例 #1：
123
样例 #2：
-380
样例输出
样例 #1：
321
样例 #2：
-83
'''
input_val = int(input())
result = 0
flag = 1
if input_val == 0:
    print(0)
elif input_val > 0:
    while input_val != 0:
        result = result * 10 + input_val % 10
        input_val = input_val // 10
    print(flag * result)
else:
    flag = -1
    while input_val != 0:
        input_val = abs(input_val)
        result = result * 10 + input_val % 10
        input_val = input_val // 10
    print(flag * result)



