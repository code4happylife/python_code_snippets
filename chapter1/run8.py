# encoding: utf-8
'''
@author: developer
@software: python
@file: run8.py
@time: 2021/7/28 22:35
@desc:
'''

str1 = input()
str2 = input()

output_str1 = str2[0:2] + str1[2:]
output_str2 = str1[0:2] + str2[2:]
print(output_str1)
print(output_str2)
