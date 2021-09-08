# encoding: utf-8
'''
@author: developer
@software: python
@file: run31.py
@time: 2021/8/8 9:50
@desc:
'''

'''
描述
给定三个正整数m,n,s问从1到m这m个数里面取n个不同的数，
使它们和是s,有多少种取法

输入
多组数据
输入的第一行是整数t，表示有t组数据
此后有t行，每行是一组数据
每组数据就是三个正整数，m,n, s ( n <= 10,s <= 20)
输出
对每组数据，输出答案
样例输入
5
13 4 20
12 5 18
1 1 1
1 2 1
119 3 20
样例输出
22
3
1
0
24
提示
用函数ways(m,n,s)表示 从1到m这m个数里面取n个不同的数，使它们和是s的取法总数
显然，必须取m个数，不能不取(除非m == 0)


1) 考虑如果 m > s, 问题可以等价于什么？
2) 对于m<= s的情况，把所有的取法分成两类:
第一类： 取m。则取m后，剩下的问题变成什么？
第二类： 不取m，那么剩下的问题变成什么？
3) 注意边界条件（即递归终止条件，即不需要递归的条件）
边界条件一般是 n,m,s = 0, = 1 之类的情况。

例如：从 1-m这m个数里面，取0个数，使得它们的和是0，有几种取法? 答案是1。
从 1到m这m个数里面，取0个数，使得它们的和是s(s>0)，有几种取法? 答案是0。无解对应的答案就是0.
当 m < n时，答案是0，因为没法取n个数
当 m = 0时，只要m和s有一个不是0，ways(m,n,s)就应该返回0。


递归的时候，函数的参数会减少，如果会出现某个参数一直没完没了减少下去，那就不对了。
因此,边界条件一定要考虑周全，确保递归可以终止。

边界条件可以有多种写法。
'''
num_of_tests = int(input())


def ways(m, n, s):
    if m == 1 and n == 1 and s == 1:
        way = 1
        return way
    elif m == 1 and n > m:
        way = 0
        return way
    elif n == 0 and s == 0:
        way = 1
        return way
    elif m == 0 and (n != 0 or s != 0):
        way = 0
        return way
    elif m <= s:
        way = ways(m - 1, n - 1, s - m) + ways(m - 1, n, s)
        return way
    elif m > s:
        way = ways(s, n, s)
        return way


for test in range(num_of_tests):
    input_nums_strs = input().split()
    m, n, s = int(input_nums_strs[0]), int(input_nums_strs[1]), int(input_nums_strs[2])
    print(ways(m, n, s))
