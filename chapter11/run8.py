# encoding: utf-8
'''
@author: developer
@software: python
@file: run8.py
@time: 2021/9/4 10:33
@desc:
'''

'''
一家医院中，同时住院的患者人数称为医院的负荷。

卫生部门获取到了大量的病人住院/出院记录，并希望能据此统计出，在所有时刻单个医院的最大负荷是多少。

住院记录的格式是一行两个正整数p和h，分别表示患者编号和医院编号。

出院记录的格式是一行一个正整数p和一个-1，其中p表示患者编号。

为简便起见，假设每家医院一开始都没有住院患者。

题目保证，每个患者只会住院一次并至多出院一次，且任何患者在出院之前一定会在某家医院住院。（不保证记录结束时，所有患者都已出院）

例如，对于下面的8条记录：

1 1
4 3
3 1
5 1
8 3
3 -1
1 -1
2 1

病人住院/出院过程如下：

①1号患者在1号医院住院，此时1号医院负荷变为1；

②4号患者在3号医院住院，此时3号医院负荷变为1；

③3号患者在1号医院住院，此时1号医院负荷变为2；

④5号患者在1号医院住院，此时1号医院负荷变为3；

⑤8号患者在3号医院住院，此时3号医院负荷变为2；

⑥3号患者出院，由于3号患者之前在1号医院住院，因此1号医院负荷变为2；

⑦1号患者出院，由于1号患者之前在1号医院住院，因此1号医院负荷变为1；

⑧2号患者在1号医院住院，此时1号医院负荷变为2。

在整个过程中，单个医院最大负荷量是3（1号医院在第4条记录时达到该负荷峰值）。

请编写程序来计算医院的最大负荷。

输入
本题目有多组输入数据。
第一行一个整数n，表示输入数据的组数；
接下来共n组数据，每组数据中：
第一行为一个整数m，表示该组数据中住院/出院记录的条数；
接下来m行，每行为一条住院/出院记录，格式如上所述。
输出
对每组输入数据，输出一个整数，表示单个医院曾经达到的最大负荷
样例输入
2
8
1 1
4 3
3 1
5 1
8 3
3 -1
1 -1
2 1
1
1 2
样例输出
3
1
'''

case_num = int(input())
for case in range(case_num):
    temp = []
    data_num = int(input())
    patient_dict = {}
    hospital_dict = {}
    for data in range(data_num):
        patient_no, hospital_no = map(int, input().split())
        if hospital_no > 0:
            if patient_no not in patient_dict.keys():
                patient_dict[patient_no] = hospital_no
            if hospital_no not in hospital_dict.keys():
                hospital_dict[hospital_no] = 1
            else:
                hospital_dict[hospital_no] += 1
        elif hospital_no == -1:
            patient_hospital_no = patient_dict[patient_no]
            hospital_dict[patient_hospital_no] -= 1
        temp.append(max(hospital_dict.values()))

    print(max(temp))





