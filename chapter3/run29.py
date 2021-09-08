# encoding: utf-8
'''
@author: developer
@software: python
@file: run29.py
@time: 2021/8/7 18:58
@desc:
'''

'''
描述
请统计某个给定范围[L, R]的所有整数中，数字2出现的次数。

比如给定范围[2, 22]，数字2在数2中出现了1次，在数12中出现1次，
在数20中出现1次，在数21中出现1次，在数22中出现2次，所以数字2在该范围内一共出现了6次。

输入
输入共 1 行，为两个正整数 L 和 R，之间用一个空格隔开。
输出
输出共 1 行，表示数字 2 出现的次数。
样例输入
样例 #1：
2 22

样例 #2：
2 100
样例输出
样例 #1：
6

样例 #2：
20
'''

input_str_val = input().split()

low_num  = int(input_str_val[0])
high_num = int(input_str_val[1])

num_str=''
for i in range(low_num, high_num + 1):
    num_str+=str(i)

num_of_ch = 0
for ch in num_str:
    if ch == '2':
        num_of_ch += 1

print(num_of_ch)

