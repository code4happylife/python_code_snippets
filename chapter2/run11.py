# encoding: utf-8
'''
@author: developer
@software: python
@file: run11.py
@time: 2021/7/29 22:57
@desc:
'''

'''
f(x) = ax3 + bx2 + cx + d
'''
input_str = input().split()
x, a, b, c, d = float(input_str[0]), float(input_str[1]), float(input_str[2]), float(input_str[3]), float(input_str[4])

result = a * (x ** 3) + b * (x**2) + c * x + d
print("%.7f" % result)
