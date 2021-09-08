# encoding: utf-8
'''
@author: developer
@software: python
@file: run53.py
@time: 2021/9/2 20:12
@desc:
'''

'''
输入一串字符，将输入中的，在<>里面的，没有前导0的少于4位的整数依次输出。单独的0也要输出。

输入
第一行是整数n，表示后面一共有n个字符串
接下来有n行字符串
输出
对每个字符串，输出题目要求的结果
样例输入
3
abc<123>cd<0456>,78,123<3554>1a<38>ab<08>,1<0>111cd<3>
<12>cd<77347>
<>
样例输出
123 38 0 3 
12 
NONE

'''
import re

reg_test = r"<\b([^0][0-9]{1,2}|[0]|[0-9])\b>"

case_num = int(input())


def get_substr(str_test):
    if re.findall(reg_test, str_test):
        for i in re.findall(reg_test, str_test):
            print(i, end=" ")
        print()
    else:
        print("NONE")


for i in range(case_num):
    test_input = input()
    get_substr(test_input)

