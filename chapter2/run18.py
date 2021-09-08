# encoding: utf-8
'''
@author: developer
@software: python
@file: run18.py
@time: 2021/7/30 23:11
@desc:
'''

'''
描述
一只大象口渴了，要喝20升水才能解渴，但现在只有一个深h厘米，底面半径为r厘米的小圆桶(h和r都是整数)。问大象至少要喝多少桶水才会解渴。
输入
输入有一行：包含两个整数，以一个空格分开，分别表示小圆桶的深h和底面半径r，单位都是厘米。
输出
输出一行，包含一个整数，表示大象至少要喝水的桶数。
样例输入
23 11
样例输出
3
提示
如果一个圆桶的深为h厘米，底面半径为r厘米，那么它最多能装Pi * r * r * h立方厘米的水。(设Pi=3.14159)
1升 = 1000毫升
1毫升 = 1 立方厘米
'''

input_str = input().split()
height, radius = float(input_str[0]), float(input_str[1])

volume_unit = 3.14150 * (radius ** 2 ) * height / 1000

num_of_container = int(20 // volume_unit + 1)

print(num_of_container)
