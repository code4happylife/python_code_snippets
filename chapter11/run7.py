# encoding: utf-8
'''
@author: developer
@software: python
@file: run7.py
@time: 2021/9/4 10:22
@desc:
'''

'''
描述
新冠肺炎肆虐全球，中国提供物资支援世界各国。现需统计世界各国总共收到的物资件数。

输入
第一行输入一个数n，代表中国援外航班数。
后面是n行，每行代表一个航班。
每个航班的信息包含一个整数，表示物资数量,以及一个国名。国名不含空格。
输出
各国的所接收到的物资总件数，按各国名称的字典序输出。
样例输入
7
10 USA
20 Germany
30 Japan
40 Korea
70 Japan
20 USA
40 Germany
样例输出
Germany 60
Japan 100
Korea 40
USA 30
'''

num_of_data = int(input())
resource_dict = {}

for i in range(num_of_data):
    input_info = input().split()
    res = int(input_info[0])
    country = input_info[1]
    if country in resource_dict.keys():
        resource_dict[country] += res
    else:
        resource_dict[country] = res

for i in sorted(resource_dict.keys()):
    print(i, resource_dict[i], end=" ")
    print()


