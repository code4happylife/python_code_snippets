# encoding: utf-8
'''
@author: developer
@software: python
@file: run4.py
@time: 2021/7/28 21:31
@desc:
'''

num_str = input().split()
num_list = []
for num in num_str:
    num_list.append(float(num))

print(sum(num_list))
