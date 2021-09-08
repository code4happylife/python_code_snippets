# encoding: utf-8
'''
@author: developer
@software: python
@file: run22.py
@time: 2021/8/7 6:46
@desc:
'''

'''
描述
给定一个长度为n的非负整数序列，请计算序列的最大跨度值（最大跨度值 = 最大值减去最小值）。

输入
一共2行，第一行为序列的个数n（1 <= n <= 1000)，第二行为序列的n个不超过1000的非负整数，整数之间以一个空格分隔。
输出
输出一行，表示序列的最大跨度值。
样例输入
6
3 0 8 7 5 9
样例输出
9
'''
num_count = int(input())

temp = input().split()

num_list_int = [int(x) for x in temp]

min_Value = num_list_int[0]
max_Value = num_list_int[0]

for val in num_list_int:
    if val < min_Value:
        min_Value = val
    elif val >= max_Value:
        max_Value = val

gap_between_min_max = max_Value - min_Value
print(gap_between_min_max)
