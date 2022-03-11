#!/usr/bin/env python
# encoding: utf-8


'''
1、现在有一个列表   li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22], 
请将 大于5的数据过滤出来，然后除以2取余数，结果放到一个生成器中(通过生成器表达式实现)


2、定义一个可以使用send传入域名，自动生成一个在前面加上http://，在后面加上路径/user/login的url地址，
生成器最多可以生成5个url,生成5条数据之后再去生成，则报错StopIteration
使用案例：
# 例如:
res = g.send('www.baidu.com')
# 生成数据res为：http://www.baidu.com/user/logim'


3、通过相关操将下面的列表cases 转换为字典格式
 cases = [
     ['case_id', 'case_title', 'url', 'data', 'excepted'],
     [1, '用例1', 'www.baudi.com', '001', 'ok'],
     [4, '用例4', 'www.baudi.com', '002', 'ok'],
     [2, '用例2', 'www.baudi.com', '002', 'ok'],
     [3, '用例3', 'www.baudi.com', '002', 'ok'],
     [5, '用例5', 'www.baudi.com', '002', 'ok'],
 ]

转换之后的结果格式如下：
 res1 = [
     {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
     {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
     {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
     {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
     {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
 ]
'''

"""
1、现在有一个列表   li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22], 
请将 大于5的数据过滤出来，然后除以2取余数，结果放到一个生成器中(通过生成器表达式实现)
"""
li = [11, 21, 4, 55, 6, 67, 123, 54, 66, 9, 90, 56, 34, 22]
gen = (i % 2 for i in li if i > 5)
print(next(gen))
print(next(gen))
print(next(gen))

"""
2、定义一个可以使用send传入域名，自动生成一个在前面加上http://，在后面加上路径/user/login的url地址，
生成器最多可以生成5个url,生成5条数据之后再去生成，则报错StopIteration
使用案例：
# 例如:
res = g.send('www.baidu.com')
# 生成数据res为：http://www.baidu.com/user/logim'
"""


def gen_url():
    i = 0
    while i <= 5:
        address = yield
        prefix = 'http://'
        suffix = '/user/login'
        print(prefix + address + suffix)
        i += 1


g = gen_url()
next(g)
r1 = g.send('www.baidu.com')
r2 = g.send('www.google.com')
r3 = g.send('www.sina.com')
r4 = g.send('www.sohu.com')
r5 = g.send('www.163.com')



"""
3、通过相关操将下面的列表cases 转换为字典格式
 cases = [
     ['case_id', 'case_title', 'url', 'data', 'excepted'],
     [1, '用例1', 'www.baudi.com', '001', 'ok'],
     [4, '用例4', 'www.baudi.com', '002', 'ok'],
     [2, '用例2', 'www.baudi.com', '002', 'ok'],
     [3, '用例3', 'www.baudi.com', '002', 'ok'],
     [5, '用例5', 'www.baudi.com', '002', 'ok'],
 ]

转换之后的结果格式如下：
 res1 = [
     {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
     {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
     {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
     {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
     {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
 ]
"""

cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

title = cases[0]
res1 = []
for i in range(1, len(cases)):
    res1.append(dict(zip(title, cases[i])))

print(res1)


'''
1
1
1
http://www.baidu.com/user/login
http://www.google.com/user/login
http://www.sina.com/user/login
http://www.sohu.com/user/login
http://www.163.com/user/login
[{'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'}, {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}, {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}, {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}, {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}]

'''
