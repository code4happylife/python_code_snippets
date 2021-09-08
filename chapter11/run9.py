# encoding: utf-8
'''
@author: developer
@software: python
@file: run9.py
@time: 2021/9/4 11:20
@desc:
'''

'''
描述
输入一个整数矩阵，交换其中的两行，然后计算位于矩阵边缘的元素之和。所谓矩阵边缘的元素，就是第一行和最后一行的元素以及第一列和最后一列的元素。

输入
第一行分别为矩阵的行数m和列数n（m < 100，n < 100），两者之间以一个空格分开。
接下来输入的m行数据中，每行包含n个整数，整数之间以一个空格分开。
在接下来是两个整数x,y，表示需要将矩阵的第x行和第y行交换一下。
输出
输出交换行之后的矩阵的边缘元素和
样例输入
3 3
3 4 1
3 7 1
2 0 1
1 2
样例输出
18
'''

matrix_line, matrix_col = map(int, input().split())
matrix_test = [[0 for i in range(matrix_col)] for j in range(matrix_line)]


for line in range(matrix_line):
    temp = input().split()
    matrix_test[line] = temp

swap_line1, swap_line2 = map(int, input().split())

swap_line1 -= 1
swap_line2 -= 1

for j in range(matrix_col):
    t = matrix_test[swap_line1][j]
    s = matrix_test[swap_line2][j]
    matrix_test[swap_line2][j] = t
    matrix_test[swap_line1][j] = s


result = 0

for i in range(matrix_line):
    for j in range(matrix_col):
        if i == 0:
            result += int(matrix_test[i][j])
        elif i == matrix_line - 1:
            result += int(matrix_test[i][j])
        elif j == 0:
            result += int(matrix_test[i][j])
        elif j == matrix_col - 1:
            result += int(matrix_test[i][j])

print(result)
