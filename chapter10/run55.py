# encoding: utf-8
'''
@author: developer
@software: python
@file: run55.py
@time: 2021/9/3 23:17
@desc:
'''

'''
055:时间处理
查看提交统计提问
总时间限制: 1000ms 内存限制: 65536kB
描述
求从给定时刻开始过了给定时间后的时刻。

输入
有若干组数据。
每组数据有2行，第一行是给定时刻，可能有两种格式
格式1) 年 月 日 时 分(时是24小时制)
格式2) 月-日-年 时:分 上下午 （时是12小时制,注意没有秒)
第二行是时间增量，也可能有两种格式
格式1) 一个整数，代表多少秒
格式2) 日 时 分
输出
对每组数据，输出给定时刻加上时间增量后的新时刻,24小时制
格式如： 1982-12-10 12:12:28
样例输入
1982 12 1 23 0
737848
1982 12 1 23 15
180 2 18
12-01-1982 1:23 AM
737848
样例输出
1982-12-10 11:57:28
1983-05-31 01:33:00
1982-12-09 14:20:28

'''

import datetime

def calc_time_new(input_time, input_interval):
    if "-" in input_time:
        # time_list = input_time.split(" ")
        # year, month, day, hour, minute = time_list[0], time_list[1], time_list[2], time_list[3], time_list[4]
        time_info = datetime.datetdatetime.strptime(input_time, '%m-%d-%Y %h:%M %p')
        # print(time_info)
    else:
        time_info = datetime.datetime.strptime(input_time, "%Y %m %d %H %M")
        print(time_info)

    #time_interval = 0

    if len(input_interval.split(" ")) > 1:
        d, h, m = map(int, input_interval.split())
        seconds_add = d * 86400 + h * 3600 + m * 60
    else:
        seconds_add = int(input_interval)

    out_date = (time_info + datetime.timedelta(seconds=seconds_add)).strftime("%Y-%m-%d %H:%M:%S")
    print(out_date)


while True:
    try:
        input_time = input()
        input_interval = input()
        calc_time_new(input_time, input_interval)
    except:
        break

