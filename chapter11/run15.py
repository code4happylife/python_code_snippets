"""
1、通过列表推导式完成下面数据类型转换
现在有以下数据， li1 = ["{'a':11,'b':2}","[11,22,33,44]"] 
需要转换为以下格式： li1 = [{'a':11,'b':2},[11,22,33,44]] 
2、 Names=['python','java','php','c','c++','django','unittest','pytest','pymysql'],请通过列表推导式，获取names中字符串长度大于4的元素
3、通过字典推导式，颠倒字典的键名和值:将{'py': "python09", 'java': "java09"} 转换为： {'python09': "py", 'java09': "java"}
4、将字典{'x': 'A', 'y': 'B', 'z': 'C' } 通过推导式转换为：['x=A','y=B','z=C']
"""

li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]

li1 = [eval(i) for i in li1]

print(li1)

Names = ['python', 'java', 'php', 'c', 'c++', 'django', 'unittest', 'pytest', 'pymysql']
new_names = [item for item in Names if len(item) > 4]
print(new_names)

dict1 = {'py': "python09", 'java': "java09"}
dict2 = {v: k for k, v in dict1.items()}
print(dict2)

dict3 = {'x': 'A', 'y': 'B', 'z': 'C'}
list_tmp = [k + '=' + v for k, v in dict3.items()]
print(list_tmp)


'''
[{'a': 11, 'b': 2}, [11, 22, 33, 44]]
['python', 'django', 'unittest', 'pytest', 'pymysql']
{'python09': 'py', 'java09': 'java'}
['x=A', 'y=B', 'z=C']
'''
