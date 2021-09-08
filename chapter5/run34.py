# encoding: utf-8
'''
@author: developer
@software: python
@file: run34.py
@time: 2021/8/18 23:00
@desc:
'''

'''
描述
把一个字符串中所有出现的大写字母都替换成小写字母，同时把小写字母替换成大写字母。

输入
输入一行：待互换的字符串。
输出
输出一行：完成互换的字符串（字符串长度小于80）。
样例输入
If so, you already have a Google Account. You can sign in on the right. 
样例输出
iF SO, YOU ALREADY HAVE A gOOGLE aCCOUNT. yOU CAN SIGN IN ON THE RIGHT. 
来源
'''

input_str = input()

for ch in input_str:
    if 97 <= ord(ch) <= 122:
        print(chr(ord(ch)-32), end="")
    elif 65 <= ord(ch) <= 90:
        print(chr(ord(ch) + 32), end="")
    else:
        print(ch, end="")

