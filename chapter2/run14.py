# encoding: utf-8
'''
@author: developer
@software: python
@file: run14.py
@time: 2021/7/30 22:40
@desc:
'''

'''
给定三个正整数，分别表示三条线段的长度，判断这三条线段能否构成一个三角形。
输入
输入共一行，包含三个正整数，分别表示三条线段的长度，数与数之间以一个空格分开。
输出
如果能构成三角形，则输出“yes” ，否则输出“no”。
'''

input_str = input().split()
line_a, line_b, line_c = int(input_str[0]), int(input_str[1]), int(input_str[2])

if (line_a + line_b > line_c) and (line_a + line_c > line_b) and (line_b + line_c > line_a):
    print("yes")
else:
    print("no")

