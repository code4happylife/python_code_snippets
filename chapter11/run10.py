# encoding: utf-8
'''
@author: developer
@software: python
@file: run10.py
@time: 2021/9/4 16:16
@desc:
'''

'''
tag是形如
"<X>A</X>"的字符串，X是一个长度不为0且不超过5的字符串，由大小写字母构成。

"<X>" 和 "</X>"里面的X必须相同。
例如：
<abc>xyd</abc> 是一个tag
但是  <abc>xyd</bc> 不是一个tag。


双重tag形式如下：
"<X>A<Y>B</Y>C</X>"

X,Y都是一个长度不为0且不超过5的字符串，由大小写字母构成。
"<X>" 和 "</X>"里面的X必须相同，
"<Y>"和"</Y>"里面的Y必须相同。

"<Y>B</Y>"称为内重tag。"<Y>"只和离他最近的"</Y>"构成内重tag。
A,B,C是任意长度不为0的字符串。

请找出B中的全部不超过4位的整数。00003 算超过4位。

输入
若干行。数据保证一个tag内部最多只有一个tag
输出
对每行，依次输出双重tag中的所有不超过4位且没有前导0的整数。单个的0算没有前导0。如果找不到，就输出NONE
样例输入
bac<x><a>bb123<c>aaa 292 bbb 384 j 67477 0 dd 04 05hd</c>c12c</a></y>def
k<a>1<c>12 35</c>78</c></a></a><x>d<y>3 4</x></y>k</x>def
k<a>1<c>12 35</c>78</c></a></a><x>d<y>3 4</y>k</x>def
k<a>1<c>12 35</c>78</c></a></a><x>d<y>3 4</y></x>def
k<a>1<c>12 35</c>78</c></a></a><abcdefg>d<y>3 4</y></abcdefg>def
k<a>1<c>12 35</a>78</a></c></B><x>d<y>3 4</y></x>def
样例输出
292 384 0 
12 35 3 4 
12 35 3 4 
12 35 
12 35 
NONE
提示
读入若干行，需要用 try...except 来判断结束
'''
import re

#m = r'<([a-zA-Z]{1,5})>(.*)<([a-zA-Z]{1,5})>.+([0-9]{1,4}).+</\3>(.*?)</\1>'
m=r'(\D|\b)(0|[1-9]\d{0,3})(\D|\b)'
while True:
    try:
        test_str = input()
        result = re.findall(m, test_str)
        for i in result:
            print(i, end=" ")
    except:
        break