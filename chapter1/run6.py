# encoding: utf-8
'''
@author: developer
@software: python
@file: run6.py
@time: 2021/7/28 22:29
@desc:
'''

num_str = input().split()
num_list = []
for num in num_str:
    num_list.append(int(num))

a = num_list[0]
b = num_list[1]
c = num_list[2]
result = (a + b) * c
print(result)
