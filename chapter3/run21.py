# encoding: utf-8
'''
@author: developer
@software: python
@file: run21.py
@time: 2021/8/7 6:34
@desc:
'''

'''
描述
读入n（1 <= n <= 10000）个整数，求它们的和与均值。

输入
输入第一行是一个整数n，表示有n个整数。
第2~n+1行每行包含1个整数。每个整数的绝对值均不超过10000。
输出
输出一行，先输出和，再输出平均值（保留到小数点后5位），两个数间用单个空格分隔。
样例输入
4
344
222
343
222
样例输出
1131 282.75000
'''

number_count = int(input())
num_list = []

for i in range(number_count):
    num_list.append(int(input()))

sum_of_num = 0

for num in num_list:
    sum_of_num += num

avg_num = sum_of_num / number_count

print("%d %.5f" % (sum_of_num, avg_num))
