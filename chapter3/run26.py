# encoding: utf-8
'''
@author: developer
@software: python
@file: run26.py
@time: 2021/8/7 8:01
@desc:
'''

'''
描述
监护室每小时测量一次病人的血压，若收缩压在90 - 140之间并且舒张压在60 - 90之间（包含端点值）则称之为正常，
现给出某病人若干次测量的血压值，计算病人保持正常血压的最长小时数。

输入
第一行为一个正整数n，n < 100
其后有n行，每行2个正整数，分别为一次测量的收缩压和舒张压，中间以一个空格分隔。
输出
输出仅一行，血压连续正常的最长小时数。
样例输入
4
100 80
90 50
120 60
140 90
样例输出
2
'''

hour_len = int(input())
pressure_val = []

for i in range(hour_len):
    pressure_val.append(input().split())

normal_list = []
for i in range(hour_len):
    if 90 <= int(pressure_val[i][0]) <= 140 and 60 <= int(pressure_val[i][1]) <= 90:
        normal_list.append(1)
    else:
        normal_list.append(0)

total_normal_hour = 0
result = []

for i in normal_list:
    if i == 1:
        total_normal_hour += 1
    else:
        total_normal_hour = 0
    result.append(total_normal_hour)


print(max(result))

