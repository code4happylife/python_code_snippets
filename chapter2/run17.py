# encoding: utf-8
'''
@author: developer
@software: python
@file: run17.py
@time: 2021/7/30 23:03
@desc:
'''

'''
描述
一个最简单的计算器，支持+, -, *, / 四种运算。仅需考虑输入输出为整数的情况(除法结果就是商，忽略余数）
输入
输入只有一行，共有三个参数，其中第1、2个参数为整数，第3个参数为操作符（+,-,*,/）。
输出
输出只有一行，一个整数，为运算结果。然而：
1. 如果出现除数为0的情况，则输出：Divided by zero!
2. 如果出现无效的操作符(即不为 +, -, *, / 之一），则输出：Invalid operator!
样例输入
1 2 +
样例输出
3
'''

input_str = input().split()
num1, num2, oper = int(input_str[0]), int(input_str[1]), input_str[2]
if oper == '+':
    result = num1 + num2
    print(result)
elif oper == '-':
    result = num1 - num2
    print(result)
elif oper == '*':
    result = num1 * num2
    print(result)
elif oper == '/':
    if num2 == 0:
        print("Divided by zero!")
    else:
        result = num1 // num2
        print(result)
else:
    print("Invalid operator!")

