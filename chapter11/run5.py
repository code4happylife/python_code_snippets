# encoding: utf-8
'''
@author: developer
@software: python
@file: run5.py
@time: 2021/9/4 8:54
@desc:
'''

'''
描述
用一张面值为x元的纸币换面值为y角、z角的硬币，
每种硬币至少一枚，问有几种换法？请注意，纸币的单位是元，硬币的单位是角，一元等于10角。

输入
输入三个正整数x、y和z
输出
输出一个正整数，为换法的种数
样例输入
样例#1
1 2 5
样例#2
2 2 4
样例#3
3 4 6
样例输出
样例#1
0
样例#2
4
样例#3
2
提示
枚举y、z可能枚数的全部组合
'''

x, y, z = map(int, input().split())
methods = 0

result = []
y_coin = 0
z_coin = 0
max_coin = x * 10
total = x * 10
for i in range(1, max_coin):
    for j in range(1, max_coin):
        if y * i + z * j == total:
          result.append((i, j))

print(len(result))



