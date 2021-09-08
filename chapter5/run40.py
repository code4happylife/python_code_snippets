# encoding: utf-8
'''
@author: developer
@software: python
@file: run40.py
@time: 2021/8/25 20:24
@desc:
'''
'''
描述
给定年月日，求星期几。已知2020年11月18日是星期三。另外，本题有公元0年，这个和真实的纪年不一样
11 月 17日 星期二
11月 16日 星期一
11月 15日 星期天

2021 年 1 月 1 号 星期五
2021 年 1 月 3 号 星期天
输入
第一行是n(n <=30)，表示有n组数据
接下来n行，每行是一组数据。
每行三个整数y,m,d，分别代表年，月，日。(-1000000<=y<=1000000)

若今年是2017年，则往前就是2016年，2015年....一直数到2年，1年，再往前就是0年，-1年，-2年.....
输出
对每组数据，输出星期几，星期几分别用

"Sunday","Monday","Tuesday","Wednesday","Thursday", "Friday","Saturday" 表示

如果月份和日期不合法，输出"Illegal"
样例输入
6
2017 2 29
2017 13 2
0 1 1
-2 3 4
2017 10 18
2015 12 31
样例输出
Illegal
Illegal
Saturday
Wednesday
Wednesday
Thursday
'''

# judge illegal

test_case_num = int(input())

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
        print(weekdays[(days) % 7])
        return
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
        print(weekdays[(7 - index_of_week + 1)%7])
        return


if __name__ == '__main__':
    for tests in range(test_case_num):
        input_date = input().split()
        year_input, month_input, day_input = int(input_date[0]), int(input_date[1]), int(input_date[2])
        calc_weekday(year_input, month_input, day_input)
