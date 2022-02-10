#!/usr/bin/env python
# encoding: utf-8
'''
@file: test4.py
@time: 2022/2/9 9:19 下午
@desc:
'''
import copy

total_line_count = len(open("demo.txt", 'r').readlines())

temp_dict = {}
final_list = []

with open("demo.txt", 'r') as f:
    keys = f.readline().strip().split(',')
    for i in range(total_line_count - 1):
        values = f.readline().strip().split(',')
        for k in keys:
            temp_dict[k] = values[keys.index(k)]
        test_dict = copy.deepcopy(temp_dict)
        final_list.append(test_dict)

print(final_list)

'''
[{'id': '1', 'url': 'www.baidu.com', 'mobilephone': '137777777', 'pwd': '123456'}, {'id': '2', 'url': 'www.taobao.com', 'mobilephone': '13666666', 'pwd': '654321'}]

'''
