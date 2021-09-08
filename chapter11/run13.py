# encoding: utf-8
'''
@author: developer
@software: python
@file: run13.py
@time: 2021/9/5 9:20
@desc:
'''
'''
描述
给定公元year年month月，打印该月月历

输入
第一行一个输入整数n，表示有n组数据。
后面n行，每行一组数据，是两个整数，分别代表year( 0 < year <= 100000）和month（数据合法，1<=month<=12），用空格隔开
输出
对于每组数据：
第一行输出月份（英文表示，首字母大写）和年份，用逗号隔开；
第二行输出星期几， Sun Mon Tue Wed Thu Fri Sat，用\t隔开；
接下来输出当月日期，日期用\t隔开，第一周缺天直接输出\t。
（行与行之间无空行，每组数据之间无空行）
行末多出来\t没有关系
12个月份的单词是：
"January","February", "March", "April", "May", "June", "July", "August", "September", "October","November", "December"
样例输入
3
2019 12
403 5
23456 7
样例输出
December,2019
Sun	Mon	Tue	Wed	Thu	Fri	Sat
1 	2 	3 	4 	5 	6 	7 	
8 	9 	10 	11 	12 	13 	14 	
15 	16 	17 	18 	19 	20 	21 	
22 	23 	24 	25 	26 	27 	28 	
29 	30 	31 	
May,403
Sun	Mon	Tue	Wed	Thu	Fri	Sat
				1 	2 	3 	
4 	5 	6 	7 	8 	9 	10 	
11 	12 	13 	14 	15 	16 	17 	
18 	19 	20 	21 	22 	23 	24 	
25 	26 	27 	28 	29 	30 	31 	
July,23456
Sun	Mon	Tue	Wed	Thu	Fri	Sat
		1 	2 	3 	4 	5 	
6 	7 	8 	9 	10 	11 	12 	
13 	14 	15 	16 	17 	18 	19 	
20 	21 	22 	23 	24 	25 	26 	
27 	28 	29 	30 	31
'''

case_num = int(input())


def whether_leap_year(year_time):
    if (year_time % 4 == 0 and year_time % 100 != 0) or (year_time % 400 == 0):
        return True
    else:
        return False


def calc_weekday(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > 31:
        print("Illegal")
        return
    elif month == 2 and not (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and day > 28:
        print("Illegal")
        return

    monthdays = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    days = 0

    if year >= 2021:
        for y in range(2021, year):
            if whether_leap_year(y):
                days += 366
            else:
                days += 365

        if whether_leap_year(year):
            monthdays[2] = 29

        for i in range(1, month):
            days += monthdays[i]
        days += day
        days -= 3
        # print(weekdays[(days) % 7])
        return weekdays[(days) % 7]
    elif year < 2021:
        for y in range(year, 2021):
            if whether_leap_year(abs(y)):
                days += 366
            else:
                days += 365

        if whether_leap_year(abs(year)):
            monthdays[2] = 29

        for i in range(1, month):
            days -= monthdays[i]

        days = days - day
        days = days + 1 + 3
        index_of_week = abs(days % 7)
        # print(weekdays[(7 - index_of_week + 1)%7])
        return weekdays[(7 - index_of_week + 1) % 7]


for i in range(case_num):
    # input year and month
    time_input = input().split()
    year = int(time_input[0])
    month = int(time_input[1])
    day = 0
    total = 0
    space = 0
    # 判断输入的年份是否是闰年
    isRun = whether_leap_year(year)
    monthdays = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 计算输入月份第一天的空格数，及获取是星期几
    week_day = calc_weekday(year, month, 1)
    # weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    week_day_format = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_index = week_day_format.index(week_day)
    space = day_index % 7
    month_word = ["-1", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                  "October", "November", "December"]
    print(" ")
    print(month_word[month], end="")
    print("," + str(year))

    # 打印日历表头
    print('Sun\tMon\tTue\tWed\tThu\tFri\tSat')

    for m in range(1, month + 1):
        # week_day获取不同月份有多少天
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            dates = 31
        elif m == 2:
            if isRun == True:
                dates = 29
            else:
                dates = 28
        else:
            dates = 30

    for s in range(0, space):
        print('\t', end='')

    for d in range(1, dates + 1):
        print(d, end='\t')
        # 判断是否为周六并换行
        if (day_index + d) % 7 == 0 and d != dates:
            print("\n")
