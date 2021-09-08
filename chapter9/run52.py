# encoding: utf-8
'''
@author: developer
@software: python
@file: run52.py
@time: 2021/9/2 20:01
@desc:
'''

'''
描述
程序填空，输出指定结果

import re
m = \
// 在此处补充你的代码
for x in  re.findall(m,"cdef<h3>abd</h3><h3>bcK</h3><h3>123</h3>KJM"):
    print(x)
输入
无
输出
abd
bcK
123
样例输入
无
样例输出
abd
bcK
123
提示
请注意，同一行的代码要在中间换行，在python 里的写法是加 “\"

如

x = \
3

即为

x = 3
'''

import re
m = r"<h3>(.*?)</h3>"
for x in re.findall(m,"cdef<h3>abd</h3><h3>bcK</h3><h3>123</h3>KJM"):
    print(x)


