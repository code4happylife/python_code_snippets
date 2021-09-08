# encoding: utf-8
'''
@author: developer
@software: python
@file: run1.py
@time: 2021/9/4 8:12
@desc:
'''

'''
描述
输入一个正整数，如果是5和7的公倍数，就输出 best，如果不是7的倍数，但是是5的倍数就输出good，其它情况就输出bad。注意这些词都是小写

输入
一个正整数n
输出
根据要求输出best,good或bad
样例输入
样例#1
35
样例#2
14
样例#3
10
样例输出
样例#1
best
样例#2
bad
样例#3
good
'''

input_num = int(input())

if input_num % 5 == 0 and input_num % 7 == 0:
    print("best")
elif input_num % 7 !=0 and input_num % 5 == 0:
    print("good")
else:
    print("bad")
