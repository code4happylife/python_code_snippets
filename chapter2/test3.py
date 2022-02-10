#!/usr/bin/env python
# encoding: utf-8
'''

@file: test3.py
@time: 2022/2/9 9:10 下午
@desc: 计算买书的方式一共有多少种
'''

book_num = 100
book_price_total = 100

a_price = 4
b_price = 3
c_price = 0.5

method = 0
for a_num in range(100):
    for b_num in range(100):
        for c_num in range(100):
            if (a_num * a_price + b_num * b_price + c_num*c_price == 100) and a_num + b_num + c_num == 100:
                print(a_num, b_num, c_num)
                method += 1

print("total ways of buying books is :", method)

'''
0 20 80
5 13 82
10 6 84
total ways of buying books is : 3
'''

