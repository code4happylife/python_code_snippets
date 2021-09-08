# encoding: utf-8
'''
@author: developer
@software: python
@file: run2.py
@time: 2021/9/4 8:15
@desc:
'''
'''
描述
小明到了手办店非常开心，要大买特买。但他不是大富豪，所以只能买不超过60元手办。

现在知道若干手办的价钱，请计算小明一共要花掉多少钱。

输入
一行，若干个正整数，每个正整数表示一个手办的价钱
输出
小明会买下所有不超过60元的手办。输出他将要花掉多少钱
样例输入
120 60 60 30 50 10 100
样例输出
210
'''

shouban = input()
shouban_list = shouban.split()


total = 0

for price in shouban_list:
    if int(price) <= 60:
        total += int(price)

print(total)


