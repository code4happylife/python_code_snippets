# encoding: utf-8
'''
@author: developer
@software: python
@file: run3.py
@time: 2021/9/4 8:21
@desc:
'''

'''
描述
一个句子中有多个单词，单词之间可能有一个或多个空格。
给定一个字符，请计算该字符在每个单词中的出现次数。 
本题目不区分大小写字母。例如，字符A与字符a在单词Abandon中的出现次数都认为是2。 本题目有多组输入数据。

输入
第一行一个整数n，表示数据组数；
接下来共2n行，每两行为一组：
每组中第一行为给定的字符，保证为小写或大写字母；
每组中第二行为输入的句子，保证只由大小写字母或空格组成，且第一个单词前与最后一个单词后都没有空格。
输出
n行，每行若干个整数，表示句子的每个单词中，给定字符的出现次数。
每行的相邻整数之间用一个空格分隔。

行末多输出了空格没有关系
样例输入
3
a
Abandon that
B
Bob  is   the  BIG BOSS
z
Zelda   ZZZ
样例输出
2 1
2 0 0 1 1
1 3
'''

test_case = int(input())


def calc_char_freqence(ch, word):
    freq = 0
    freq_result = []
    for i in word:
        if i != "":
            for c in i:
                if ch.upper() == c.upper():
                    freq += 1
            freq_result.append(freq)
            freq = 0
    return freq_result


for test in range(test_case):
    input_ch = input()
    input_word = input().split(" ")

    for word in input_word:
        temp = calc_char_freqence(input_ch, input_word)

    for num in temp:
        print(num, end=" ")
    print()
