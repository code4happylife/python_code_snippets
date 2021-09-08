# encoding: utf-8
'''
@author: developer
@software: python
@file: run39.py
@time: 2021/8/22 22:37
@desc:
'''

'''
描述
输入两个串s1,s2，找出s2在s1中所有出现的位置

两个子串的出现不能重叠。例如'aa'在 aaaa 里出现的位置只有0,2

输入
第一行是整数n
接下来有n行，每行两个不带空格的字符串s1,s2
输出
对每行，从小到大输出s2在s1中所有的出现位置。位置从0开始算
如果s2没出现过，输出 "no"
行末多输出空格没关系
样例输入
4
ababcdefgabdefab ab
aaaaaaaaa a
aaaaaaaaa aaa 
112123323 a
样例输出
0 2 9 14 
0 1 2 3 4 5 6 7 8 
0 3 6 
no
'''

test_case_num = int(input())


def count_chr(str_test, ch_test):
    if str_test.count(ch_test) == 0:
        print("no")
    else:
        i = 0
        while str_test.find(ch_test, i) != -1:
            index_temp = str_test.find(ch_test, i)
            print(index_temp, end=" ")
            i = index_temp + len(ch_test)
        print()


if __name__ == '__main__':
    for case in range(test_case_num):
        input_test = input().split()
        str1, str2 = input_test[0], input_test[1]
        count_chr(str1, str2)
