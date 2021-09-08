# encoding: utf-8
'''
@author: developer
@software: python
@file: run19.py
@time: 2021/7/30 23:19
@desc:
'''
'''
你买了一箱n个苹果，很不幸的是买完时箱子里混进了一条虫子。虫子每x小时能吃掉一个苹果，
假设虫子在吃完一个苹果之前不会吃另一个，那么经过y小时你还有多少个完整的苹果？

输入
输入仅一行，包括n，x和y（均为整数）。
输出
输出也仅一行，剩下的苹果个数
样例输入
10 4 9
样例输出
7
'''

import math

input_str = input().split()
apple_num, time_to_eat, time_pass = int(input_str[0]), int(input_str[1]), int(input_str[2])

bad_apple = math.ceil(time_pass / time_to_eat)

good_apple = apple_num - bad_apple
if good_apple >= 0:
    print(good_apple)
else:
    print(0)
