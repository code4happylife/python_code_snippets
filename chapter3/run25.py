# encoding: utf-8
'''
@author: developer
@software: python
@file: run25.py
@time: 2021/8/7 7:48
@desc:
'''

'''
描述
所谓角谷猜想，是指对于任意一个正整数，如果是奇数，则乘3加1，如果是偶数，则除以2，
得到的结果再按照上述规则重复处理，最终总能够得到1。
如，假定初始整数为5，计算过程分别为16、8、4、2、1。
程序要求输入一个整数，将经过处理得到1的过程输出来。

输入
一个正整数N(N <= 2,000,000)
输出
从输入整数到1的步骤，每一步为一行，每一部中描述计算过程。
最后一行输出"End"。如果输入为1，直接输出"End"。
样例输入
5
样例输出
5*3+1=16
16/2=8
8/2=4
4/2=2
2/2=1
End
'''
input_num = int(input())

if input_num == 1:
    print("End")


while input_num != 1:
    if input_num % 2 == 1:
        print("%d*3+1=%d" % (input_num, input_num*3+1))
        input_num = input_num * 3 + 1
    elif input_num % 2 == 0:
        print("%d/2=%d" % (input_num, input_num/2))
        input_num /= 2
    if input_num == 1:
        print("End")

