# encoding: utf-8
'''
@author: developer
@software: python
@file: run32.py
@time: 2021/8/17 22:26
@desc:
'''

'''
描述
石头剪刀布是常见的猜拳游戏。石头胜剪刀，剪刀胜布，布胜石头。如果两个人出拳一样，则不分胜负。

一天，小A和小B正好在玩石头剪刀布。已知他们的出拳都是有周期性规律的，比如：“石头-布-石头-剪刀-石头-布-石头-剪刀……”，就是以“石头-布-石头-剪刀”为周期不断循环的。请问，小A和小B比了N轮之后，谁赢的轮数多？

输入
输入包含三行。
第一行包含三个整数：N，NA，NB，分别表示比了N轮，小A出拳的周期长度，小B出拳的周期长度。0 < N,NA,NB < 100。
第二行包含NA个整数，表示小A出拳的规律。
第三行包含NB个整数，表示小B出拳的规律。
其中，0表示“石头”，2表示“剪刀”，5表示“布”。相邻两个整数之间用单个空格隔开。
输出
输出一行，如果小A赢的轮数多，输出A；如果小B赢的轮数多，输出B；如果两人打平，输出draw。
样例输入
10 3 4
0 2 5
0 5 0 2
样例输出
A
提示
对于测试数据，猜拳过程为：
A：0 2 5 0 2 5 0 2 5 0
B：0 5 0 2 0 5 0 2 0 5
A赢了4轮，B赢了2轮，双方打平4轮，所以A赢的轮数多。

'''

input_pattern = input().split()
loop_time = int(input_pattern[0])

period_a = int(input_pattern[1])
period_b = int(input_pattern[2])

pattern_a_str = input().split()
pattern_b_str = input().split()

a_repeat_times = loop_time // period_a
a_reserve_times = abs(loop_time - a_repeat_times * period_a)
compete_a = pattern_a_str * a_repeat_times + pattern_a_str[:a_reserve_times]

b_repeat_times = loop_time // period_b
b_reserve_times = abs(loop_time - b_repeat_times * period_b)
compete_b = pattern_b_str * b_repeat_times + pattern_b_str[:b_reserve_times]


def compete(a, b):
    if a == b:
        return 0
    elif a == 0 and b == 2:
        return 1
    elif a == 2 and b == 5:
        return 1
    elif a == 5 and b == 0:
        return 1
    else:
        return -1


# print(compete_a)
# print(compete_b)
result = 0
for index in range(loop_time):
    result += compete(int(compete_a[index]), int(compete_b[index]))

if result > 0:
    print("A")
elif result < 0:
    print("B")
else:
    print("draw")

