# encoding: utf-8
'''
@author: developer
@software: python
@file: run16.py
@time: 2021/7/30 22:56
@desc:
'''

'''
描述
编写程序，计算下列分段函数y=f(x)的值。
y=-x+2.5; 0 <= x < 5
y=2-1.5(x-3)(x-3); 5 <= x < 10
y=x/2-1.5; 10 <= x < 20
输入
一个浮点数N,0 <= N < 20
输出
输出N对应的分段函数值：f(N)。结果保留到小数点后三位。
样例输入
1.0
样例输出
1.500
'''


def func_test(num):
    if 0 <= num < 5:
        return (-1) * num + 2.5
    elif 5 <= num < 10:
        return 2 - 1.5 * (num - 3) * (num - 3)
    elif 10 <= num < 20:
        return num / 2 - 1.5


input_number = float(input())
result = func_test(input_number)
print("%.3f" % result)
