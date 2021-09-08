# encoding: utf-8
'''
@author: developer
@software: python
@file: run11.py
@time: 2021/9/4 16:47
@desc:
'''

'''
描述
有若干个同学参加跳水比赛，每个同学都有若干位老师给他打分。
 一共有m条打分记录，每一条记录的格式都是这样的："id score"，
 表示编号为id的同学获得了score分。（id和score都是正整数） 
 现在这m条记录依次送到了你的手上，你想在每一条记录到达的时候，
 都快速地计算出这个编号为id的同学目前得到的平均分是多少。
 平均只取整数部分即可，小数部分直接去掉，不要四舍五入。

输入
第一行，一个整数m。(m <= 100000)
接下来m行，每行两个正整数代表id和score.
输出
对每行的 id score, 输出id同学到目前为止的平均分
样例输入
4
1 100
2 90
2 95
1 70
样例输出
100
90
92
85

'''

num_of_case = int(input())
stu_info = {}
result_list = []


def mean(lst):
    sum_val = sum(lst)
    return int(sum_val // len(lst))


for i in range(num_of_case):
    stu = input().split()
    stu_id = stu[0]
    score = int(stu[1])
    if stu_id not in set(stu_info.keys()):
        stu_info[stu_id] = []
        stu_info[stu_id].append(score)
        avg = mean(stu_info[stu_id])
    elif stu_id in set(stu_info.keys()):
        stu_info[stu_id].append(score)
        avg = mean(stu_info[stu_id])
    result_list.append(avg)

for i in range(num_of_case):
    print(result_list[i])
