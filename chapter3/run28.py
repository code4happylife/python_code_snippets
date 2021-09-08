# encoding: utf-8
'''
@author: developer
@software: python
@file: run28.py
@time: 2021/8/7 18:55
@desc:
'''

'''
描述
一个十进制自然数,它的七进制与九进制表示都是三位数，
且七进制与九进制的三位数码表示顺序正好相反。
编程求此自然数,并输出显示。

输入
无。
输出
三行：
第一行是此自然数的十进制表示；
第二行是此自然数的七进制表示；
第三行是此自然数的九进制表示。
样例输入
（无）
样例输出
（不提供）
'''

for origin_val in range(100, 1000):
    num_7_base = origin_val
    num_9_base = origin_val
    result_7_base = ""
    result_9_base = ""

    while num_7_base:
        res = num_7_base % 7
        num_7_base = num_7_base // 7
        result_7_base += str(res)

    while num_9_base:
        res = num_9_base % 9
        num_9_base = num_9_base // 9
        result_9_base += str(res)

    if result_9_base == result_7_base[::-1]:
        print(origin_val)
        print(result_9_base)
        print(result_7_base)


