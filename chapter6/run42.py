# encoding: utf-8
'''
@author: developer
@software: python
@file: run42.py
@time: 2021/8/29 10:36
@desc:
'''

'''
描述
给定n行m列的图像各像素点的灰度值，要求用如下方法对其进行模糊化处理：

1. 四周最外侧的像素点灰度值不变；

2. 中间各像素点新灰度值为该像素点及其上下左右相邻四个像素点原灰度值的平均（舍入到最接近的整数）。

输入
第一行包含两个整数n和m，表示图像包含像素点的行数和列数。1 <= n <= 100，1 <= m <= 100。
接下来n行，每行m个整数，表示图像的每个像素点灰度。相邻两个整数之间用单个空格隔开，每个元素均在0~255之间。
输出
n行，每行m个整数，为模糊处理后的图像。相邻两个整数之间用单个空格隔开。
样例输入
4 5
100 0 100 0 50
50 100 200 0 0
50 50 100 100 200
100 100 50 50 100
样例输出
100 0 100 0 50
50 80 100 60 0
50 80 100 90 200
100 100 50 50 100
'''
import copy
n, m = map(int, input().split())
matrix_test = []
result_matrix = []
for i in range(n):
    matrix_test.append(list(map(int, input().split())))

result_matrix = copy.deepcopy(matrix_test)

for line in range(1, n-1):
    for col in range(1, m-1):
        result_matrix[line][col] = round((matrix_test[line][col] + matrix_test[line-1][col] + matrix_test[line+1][col] + matrix_test[line][col-1] + matrix_test[line][col+1])/5)

for line in range(0, n):
    for col in range(0, m):
        print(result_matrix[line][col], end=" ")
    print()

print()

