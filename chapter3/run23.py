# encoding: utf-8
'''
@author: developer
@software: python
@file: run23.py
@time: 2021/8/7 7:10
@desc:
'''

'''
描述
2008年北京奥运会，A国的运动员参与了n天的决赛项目(1≤n≤17)。现在要统计一下A国所获得的金、银、铜牌数目及总奖牌数。

输入
输入n＋1行，第1行是A国参与决赛项目的天数n，其后n行，每一行是该国某一天获得的金、银、铜牌数目，以一个空格分开。
输出
输出1行，包括4个整数，为A国所获得的金、银、铜牌总数及总奖牌数，以一个空格分开。
样例输入
3
1 0 3
3 1 0
0 3 0
样例输出
4 4 3 11
'''

day_of_olympic = int(input())

medals = []

for day in range(day_of_olympic):
    medals.append(input().split())

gold_medal = []
silver_medal = []
bronze_medal = []

for day in range(day_of_olympic):
    bronze, silver, gold = int(medals[day][0]), int(medals[day][1]), int(medals[day][2])
    gold_medal.append(bronze)
    silver_medal.append(silver)
    bronze_medal.append(gold)

total_gold = sum(gold_medal)
total_silver = sum(silver_medal)
total_bronze = sum(bronze_medal)

total_medal = total_gold + total_silver + total_bronze
print("%d %d %d %d" %(total_gold, total_silver, total_bronze, total_medal))
