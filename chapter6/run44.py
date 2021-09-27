# encoding: utf-8
'''
@author: developer
@software: python
@file: run44.py
@time: 2021/8/29 10:56
@desc:
'''

'''
描述
病人登记看病，编写一个程序，将登记的病人按照以下原则排出看病的先后顺序：
1. 老年人（年龄 >= 60岁）比非老年人优先看病。
2. 老年人按年龄从大到小的顺序看病，年龄相同的按登记的先后顺序排序。
3. 非老年人按登记的先后顺序看病。
输入
第1行，输入一个小于100的正整数，表示病人的个数；
后面按照病人登记的先后顺序，每行输入一个病人的信息，包括：一个长度小于10的字符串表示病人的ID（每个病人的ID各不相同且只含数字和字母），一个整数表示病人的年龄，中间用单个空格隔开。
输出
按排好的看病顺序输出病人的ID，每行一个。
样例输入
5
021075 40
004003 15
010158 67
021033 75
102012 30
样例输出
021033
010158
021075
004003
102012

'''

patient_num = int(input())
patient_list = []

for i in range(patient_num):
    info = input().split()
    index = 1
    patient_list.append(((info[0]), int(info[1]), int(index)))
    index += 1


def priority(patient_information):
    if patient_information[1] >= 60:
        return -patient_information[1]
    else:
        return int(patient_information[2])


patient_list.sort(key=priority)

for i in range(patient_num):
    print(patient_list[i][0])