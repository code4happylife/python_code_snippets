# encoding: utf-8
'''
@author: developer
@software: python
@file: run4.py
@time: 2021/9/4 8:45
@desc:
'''
'''
描述
程序填空

对于给定的一行字符串，输出其中每一对小括号里的信息。如果找不到配对的小括号，就输出NONE。

“配对”指的是一个左括号与其右侧最近的右括号的匹配，例如"(a)(b)"里，第一个左括号与第一个右括号配对，第二个左括号与第二个右括号配对。

本题目保证配对的小括号里一定有内容，也就是不会出现"a()b"这样的字符串。

本题目保证配对的小括号不嵌套，也就是不会出现"xy(a(bc)def)z"这样的字符串。

注意，尽管类似"123(ab)cd(ef)gh(ij)k"这样的字符串中也存在"(...(...)...)"的模式，但此时“配对”的小括号没有嵌套，因此是满足题目限制的。

import re
exit = 10   #此句没用
n = int(input())
#填空内容应为 pt = "XXXX"，即写一个正则表达式pt
// 在此处补充你的代码
for i in range(n):
    s = input()
    k = re.findall(pt,s)
    if k:
        for x in k:
            print(x, end = " ")
        print("")
    else:
        print("NONE")
输入
第一行一个整数n，表示输入字符串行数。
接下来n行里每行一个不包含空格的字符串s。
输出
输出共n行，每行若干个字符串，相邻字符串间用一个空格分隔，表示每行输入字符串中各个小括号里的内容。
样例输入
3
1;!(#234)5@6(78)9(0)*
0(a))(()(bcd)12
)Nothing(
样例输出
#234 78 0
a ( bcd
NONE
提示
在正则表达式中没有分组时，re.findall返回所有匹配子串构成的列表。

有且只有一个分组时，re.findall返回的是一个子串的列表，每个元素是一个匹配子串中分组对应的内容。

在正则表达式中有超过一个分组时，re.findall返回的是一个元组的列表，每个元组对应于一个匹配的子串，元组里的元素，依次是1号分组、2号分组、3号分组......匹配的内容
'''

import re
n = int(input())
#填空内容应为 pt = "XXXX"，即写一个正则表达式pt
pt = r"[(](.*?)[)]"
for i in range(n):
    s = input()
    k = re.findall(pt, s)
    if k:
        for x in k:
            print(x, end=" ")
        print("")
    else:
        print("NONE")
