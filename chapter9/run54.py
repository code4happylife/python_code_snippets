# encoding: utf-8
'''
@author: developer
@software: python
@file: run54.py
@time: 2021/9/2 20:59
@desc:
'''

'''
输入
有多组数据，每组一行
输出
对每组数据， 抽取出其中的tag及其包含的电话号码中的区号输出。每个tag输出为一行。tag外的电话号码不用理会。
如果找不到tag及其包含的电话号码， 则输出NONE
数据保证不会出现两个tag重叠的情况。
样例输入
2
<bb>(01)-123<a>bbb(02)-2784KK</a><xy>stk(1)-123(03)-345b</xy>(04)-123</xy><z>(05)-123</zz>zz<yy>(06)-123</yy>
<bb>(01)-123<a><k>1223</k><a>(01)-12</a>
样例输出
<xy>1,03</xy>
<yy>06</yy>
NONE 
提示
1） tag中间可以有任何文字，比如 <ab>xddd</cd></ab>也是一个合法tag
2） 在分组的右边可以通过分组的编号引用该分组所匹配的子串
m = r'(((ab*)c)d)e\3' #要求 ab*cde后面跟着第三分组的内容
r = re.match(m,"abbbcdeabbbkfg") # 后面的bbb少一个b则不能匹配，因为第三分组是abbb
print(r.group(3)) # abbb
print(r.group()) # abbbcdeabbb
3) 如果一个正则表达式搞不定，可以先用一个正则表达式抽取某个中间结果，再在中间结果里面手工或者用另外的正则表达式进一步分析

'''