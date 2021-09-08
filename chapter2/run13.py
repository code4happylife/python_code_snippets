# encoding: utf-8
'''
@author: developer
@software: python
@file: run13.py
@time: 2021/7/29 23:10
@desc:
'''

'''
有一个正方形，四个角的坐标（x,y)分别是（1，-1），（1，1），（-1，-1），（-1，1），x是横轴，y是纵轴。
写一个程序，判断一个给定的点是否在这个正方形内（包括正方形边界）。

输入
输入一行，包括两个整数x、y，以一个空格分开，表示坐标(x,y)。
输出
输出一行，如果点在正方形内，则输出yes，否则输出no。
'''
input_list = input().split()
location_x, location_y = int(input_list[0]), int(input_list[1])

if -1 <= location_x <= 1 and -1 <= location_y <= 1:
    print("yes")
else:
    print("no")

