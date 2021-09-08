# encoding: utf-8
'''
@author: developer
@software: python
@file: count.py
@time: 2021/8/31 19:56
@desc:
'''

'''

要求根据id.txt和finalscore.txt生成学生成绩。文件都是utf-8格式的

1) id.txt 里面放着学号和姓名，没有排序。姓名很怪，不要在乎
2) finalscore.txt里面放着学生的做题信息。其中第三栏或第四栏是做题数量
   有的学生昵称是学号，有的是姓名，有的是姓名学号都有。只要有学号或姓名，就有效
3) 分数计算办法: 1题50,2题60,此后每做一题加4分
4) 生成id.txt里面有的所有学生的成绩，按学号排序输出到指定的结果文件。
如果在 finalscore里面找不到学生的做题记录，该生题数和成绩都记0

结果文件格式如：

学号	姓名	题数	分数
1700943357	玘尜寋	0	0
1700943359	杛旺煃	0	0
1700943383	玘签翢	2	60
1700943405	陕榄伳	0	0
1700943465	匒乡奡	5	72
1700943469	巸俗杽	3	64
1700943472	钬内佦	0	0
1700943481	別珜辽	0	0
1700943523	趂盨淦	7	80


这样的结果可以导入excel表格(拷贝粘贴即可)

id.txt里面没有的学生，不用处理。

注意：源文件和目标文件里面的分隔符，都不是空格，都是制表符 \t (Tab)
注意看finalscore.txt里面，有连着两个 Tab 的情况，比如下面学号和做题数之间是2个tab：


4	1700943836		9


也许你需要关注这一点，也许并不需要

5)程序文件名必须叫count.py。运行时，将count.py和id.txt, finalscore.txt放在相同文件夹下面,
然后在命令行窗口进入该文件夹，以命令行方式运行程序，命令行中可以指定结果文件名:

python count.py XXX.txt 

程序在同一个文件夹下生成结果文件XXX.txt。这个文件名可以随便指定

6)正确的结果已经给出，即ans.txt。最终生成的结果应该和ans.txt文件一致

0) 把finalscore用readlines读到一个字符串列表score里面，列表的每个元素都是一行
1) 把 id.txt全部读到一个列表里面，每个元素一行，就是一个学生的信息
   然后把这个列表排序，就得到了按学号排序的学生列表 students

2) 对 students 里的每个元素，split出学号部分和姓名部分，然后到整个 score里面去找，
学号部分或姓名部分如果能够在score里面找到，
split找到的那个score元素，得到分数，再算成绩，输出。
由于数据量不大，所以可以不用字典，集合等。
'''
import re

# 读取2个测试文件
# 读取finalscore.txt 文件的内容， 获取学号，和答题数
finalscore_list = []
with open('finalscore.txt', encoding='utf-8') as f:
    finalscore_list = f.readlines()

# print(finalscore_list)

# 读取id.txt 文件的内容， 获取学号和姓名信息
student_info = []
with open('id.txt', encoding='utf-8') as f:
    student_info = f.readlines()

stu_id_name_list = []
for item in student_info:
    stu_id_name = re.split('\t|\n', item)
    stu_id_name_list.append((stu_id_name[0], stu_id_name[1]))

# 转换成字典，获取学号和姓名对应关系的字典
dict_stu_id = dict(stu_id_name_list)
print("学号 姓名")
print(dict_stu_id)

# 进一步处理finalscore_list, 得到学号与答题数的对应关系
id_answer_list = []
for item_answer in finalscore_list:
    id_answer = re.split(r'\t|\n|\t\t|\(|\)| ', item_answer)
    try:
        id_answer_list.append(re.findall(r'\d{10}$', id_answer[1]), int(id_answer[3]))
    except:
        id_answer_list.append((id_answer[1], 0))


# 根据答题数目计算得分
def calc_score(num_of_answer):
    score = 0
    if num_of_answer == 1:
        score = 60
        return score
    elif num_of_answer == 2:
        return score
    elif num_of_answer == 0:
        score = 0
        return score
    else:
        score = 60
        for i in range(num_of_answer - 2):
            score += 4
        return score


print(id_answer_list)


# 获取学号与分数的对应关系，存储在id_score_list
id_score_list = []
for item_score in id_answer_list:
    try:
        id_score_list.append((re.findall(r'\d{10}$', item_score[0]), calc_score(int(item_score[1]))))
    except:
        id_score_list.append((item_score[0]), calc_score(int(item_score[1])))


print("学号，分数")
print(id_score_list)

result_list = []

dict_id_answer = dict(id_answer_list)

'''
dict_id_score = {}
for i in id_score_list:
    try:
        dict_id_score[int((i[0])[0])] = i[1]
    except:
        dict_id_score[i[0]] = i[1]
'''


print("学号 分数")
#print(dict_id_score)

result = 'ans1.txt'

with open(result, 'w', encoding='utf-8') as f:
    f.write('学号 姓名 题数 分数\n')

    for item in dict_stu_id:
        study_id = item[0]
        name = stu_id_name_list[int(study_id)]
        answer = dict_id_answer[int(study_id)]
        score = calc_score(answer)
        f.write("%s %s %s %s\n" % (study_id, name, answer, score))
