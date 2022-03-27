#!/usr/bin/env python
# encoding: utf-8


"""
1、用一个队列来存储数据
2、创建一个专门生产数据的任务函数，循环生产5次数据，每轮循环，往队列中添加20条数据，每循环一轮暂停1秒
3、创建一个专门处理数据的任务函数 循环获取队列中的数据处理，每秒处理4条数据。
4、创建一个线程(或进程)生产数据 ，3个线程(或进程)处理数据
5、统计数据生产并获取完  程序运行的总时长
"""

from multiprocessing import Process, Queue
import time


def produce(q):
    for i in range(5):
        for j in range(20):
            url = 'http://www.baidu.com/test{}_{}.html'.format(str(i), str(j))
            print("生产数据", url)
            q.put(url)
        time.sleep(1)


def deal_with_data(q):
    while True:
        for k in range(4):
            url = q.get()
            if url is None:
                exit()
            print("处理数据：", url)
        time.sleep(1)


if __name__ == '__main__':
    q = Queue()
    # 记录开始时间
    st = time.time()
    p0 = Process(target=produce, args=(q,))

    p1 = Process(target=deal_with_data, args=(q,))
    p2 = Process(target=deal_with_data, args=(q,))
    p3 = Process(target=deal_with_data, args=(q,))

    p0.start()
    p1.start()
    p2.start()
    p3.start()

    p0.join()
    q.put(None)
    q.put(None)
    q.put(None)

    p1.join()
    p2.join()
    p3.join()
    # 记录结束时间
    et = time.time()
    print("消耗的时间:{}秒".format(et - st))

"""
运行结果：
生产数据 http://www.baidu.com/test0_0.html
生产数据 http://www.baidu.com/test0_1.html
生产数据 http://www.baidu.com/test0_2.html
处理数据： http://www.baidu.com/test0_0.html
生产数据 处理数据： http://www.baidu.com/test0_1.html
http://www.baidu.com/test0_3.html
生产数据 http://www.baidu.com/test0_4.html
生产数据 http://www.baidu.com/test0_5.html
生产数据 http://www.baidu.com/test0_6.html
生产数据 http://www.baidu.com/test0_7.html
生产数据 http://www.baidu.com/test0_8.html
处理数据： http://www.baidu.com/test0_2.html
处理数据：生产数据  http://www.baidu.com/test0_3.htmlhttp://www.baidu.com/test0_9.html

生产数据 http://www.baidu.com/test0_10.html
生产数据 http://www.baidu.com/test0_11.html
生产数据 http://www.baidu.com/test0_12.html
生产数据 http://www.baidu.com/test0_13.html
生产数据 http://www.baidu.com/test0_14.html
生产数据 http://www.baidu.com/test0_15.html
生产数据 http://www.baidu.com/test0_16.html
生产数据 http://www.baidu.com/test0_17.html
生产数据 http://www.baidu.com/test0_18.html
生产数据 http://www.baidu.com/test0_19.html
处理数据： http://www.baidu.com/test0_4.html
处理数据： http://www.baidu.com/test0_5.html
处理数据： http://www.baidu.com/test0_6.html
处理数据： http://www.baidu.com/test0_7.html
处理数据： http://www.baidu.com/test0_8.html
处理数据： http://www.baidu.com/test0_9.html
处理数据： http://www.baidu.com/test0_10.html
处理数据： http://www.baidu.com/test0_11.html
生产数据 http://www.baidu.com/test1_0.html
处理数据： http://www.baidu.com/test0_12.html
生产数据 http://www.baidu.com/test1_1.html
处理数据： http://www.baidu.com/test0_13.html
生产数据 http://www.baidu.com/test1_2.html
生产数据 http://www.baidu.com/test1_3.html
处理数据： http://www.baidu.com/test0_14.html生产数据
 http://www.baidu.com/test1_4.html
生产数据处理数据： http://www.baidu.com/test0_15.html
处理数据： http://www.baidu.com/test0_16.html
处理数据： http://www.baidu.com/test0_17.html
处理数据： http://www.baidu.com/test0_18.html 
http://www.baidu.com/test1_5.html
生产数据 http://www.baidu.com/test1_6.html
生产数据 http://www.baidu.com/test1_7.html
生产数据 http://www.baidu.com/test1_8.html
处理数据：生产数据 http://www.baidu.com/test0_19.html
 处理数据： http://www.baidu.com/test1_0.html
处理数据： http://www.baidu.com/test1_1.html
处理数据： http://www.baidu.com/test1_2.html
处理数据： http://www.baidu.com/test1_3.html
http://www.baidu.com/test1_9.html
生产数据 http://www.baidu.com/test1_10.html
生产数据 http://www.baidu.com/test1_11.html
生产数据 http://www.baidu.com/test1_12.html
生产数据 http://www.baidu.com/test1_13.html
生产数据 http://www.baidu.com/test1_14.html
生产数据 http://www.baidu.com/test1_15.html
生产数据 http://www.baidu.com/test1_16.html
生产数据 http://www.baidu.com/test1_17.html
生产数据 http://www.baidu.com/test1_18.html
生产数据 http://www.baidu.com/test1_19.html
处理数据： http://www.baidu.com/test1_4.html
处理数据： http://www.baidu.com/test1_5.html
处理数据： http://www.baidu.com/test1_6.html
处理数据： http://www.baidu.com/test1_7.html
处理数据： http://www.baidu.com/test1_8.html
处理数据： http://www.baidu.com/test1_9.html
生产数据 http://www.baidu.com/test2_0.html
处理数据： http://www.baidu.com/test1_10.html
生产数据 http://www.baidu.com/test2_1.html处理数据： http://www.baidu.com/test1_11.html

处理数据： http://www.baidu.com/test1_12.html
生产数据 http://www.baidu.com/test2_2.html
生产数据 http://www.baidu.com/test2_3.html
生产数据 http://www.baidu.com/test2_4.html
生产数据 http://www.baidu.com/test2_5.html处理数据：
 http://www.baidu.com/test1_13.html
处理数据： http://www.baidu.com/test1_14.html
处理数据： http://www.baidu.com/test1_15.html
生产数据 http://www.baidu.com/test2_6.html
生产数据 http://www.baidu.com/test2_7.html
生产数据 http://www.baidu.com/test2_8.html
生产数据 http://www.baidu.com/test2_9.html
生产数据 http://www.baidu.com/test2_10.html
生产数据 http://www.baidu.com/test2_11.html
生产数据 http://www.baidu.com/test2_12.html
生产数据 http://www.baidu.com/test2_13.html
生产数据 http://www.baidu.com/test2_14.html
生产数据 http://www.baidu.com/test2_15.html
生产数据 http://www.baidu.com/test2_16.html
生产数据 http://www.baidu.com/test2_17.html
生产数据 http://www.baidu.com/test2_18.html
生产数据 http://www.baidu.com/test2_19.html
处理数据： http://www.baidu.com/test1_16.html
处理数据： http://www.baidu.com/test1_17.html
处理数据： http://www.baidu.com/test1_18.html
处理数据： http://www.baidu.com/test1_19.html
处理数据： http://www.baidu.com/test2_0.html
处理数据： http://www.baidu.com/test2_1.html
处理数据： http://www.baidu.com/test2_2.html
处理数据： http://www.baidu.com/test2_3.html
处理数据： http://www.baidu.com/test2_4.html
处理数据： http://www.baidu.com/test2_5.html
处理数据： http://www.baidu.com/test2_6.html
处理数据： http://www.baidu.com/test2_7.html
生产数据 http://www.baidu.com/test3_0.html
生产数据 http://www.baidu.com/test3_1.html
生产数据 http://www.baidu.com/test3_2.html
生产数据 http://www.baidu.com/test3_3.html
生产数据 http://www.baidu.com/test3_4.html
生产数据 http://www.baidu.com/test3_5.html
生产数据 http://www.baidu.com/test3_6.html
生产数据 http://www.baidu.com/test3_7.html
生产数据 http://www.baidu.com/test3_8.html
生产数据 http://www.baidu.com/test3_9.html
生产数据 http://www.baidu.com/test3_10.html
生产数据 http://www.baidu.com/test3_11.html
生产数据 http://www.baidu.com/test3_12.html
生产数据 http://www.baidu.com/test3_13.html
生产数据 http://www.baidu.com/test3_14.html
生产数据 http://www.baidu.com/test3_15.html
生产数据 http://www.baidu.com/test3_16.html
生产数据 http://www.baidu.com/test3_17.html
生产数据 http://www.baidu.com/test3_18.html
生产数据 http://www.baidu.com/test3_19.html
处理数据： http://www.baidu.com/test2_8.html
处理数据： http://www.baidu.com/test2_9.html
处理数据： http://www.baidu.com/test2_10.html
处理数据： http://www.baidu.com/test2_11.html
处理数据： http://www.baidu.com/test2_12.html
处理数据： http://www.baidu.com/test2_13.html
处理数据： http://www.baidu.com/test2_14.html
处理数据： http://www.baidu.com/test2_15.html
处理数据： http://www.baidu.com/test2_16.html
处理数据： http://www.baidu.com/test2_17.html
处理数据： http://www.baidu.com/test2_18.html
处理数据： http://www.baidu.com/test2_19.html
生产数据 http://www.baidu.com/test4_0.html
生产数据 http://www.baidu.com/test4_1.html
生产数据 http://www.baidu.com/test4_2.html
生产数据 http://www.baidu.com/test4_3.html
生产数据 http://www.baidu.com/test4_4.html
生产数据 http://www.baidu.com/test4_5.html
生产数据 http://www.baidu.com/test4_6.html
生产数据 http://www.baidu.com/test4_7.html
生产数据 http://www.baidu.com/test4_8.html
生产数据 http://www.baidu.com/test4_9.html
生产数据 http://www.baidu.com/test4_10.html
生产数据 http://www.baidu.com/test4_11.html
生产数据 http://www.baidu.com/test4_12.html
生产数据 http://www.baidu.com/test4_13.html
生产数据 http://www.baidu.com/test4_14.html
生产数据 http://www.baidu.com/test4_15.html
生产数据 http://www.baidu.com/test4_16.html
生产数据 http://www.baidu.com/test4_17.html
生产数据 http://www.baidu.com/test4_18.html
生产数据 http://www.baidu.com/test4_19.html
处理数据： http://www.baidu.com/test3_0.html
处理数据： http://www.baidu.com/test3_1.html
处理数据： http://www.baidu.com/test3_2.html
处理数据： http://www.baidu.com/test3_3.html
处理数据： http://www.baidu.com/test3_4.html
处理数据： http://www.baidu.com/test3_5.html
处理数据： http://www.baidu.com/test3_6.html
处理数据： http://www.baidu.com/test3_7.html
处理数据： http://www.baidu.com/test3_8.html
处理数据： http://www.baidu.com/test3_9.html
处理数据： http://www.baidu.com/test3_10.html
处理数据： http://www.baidu.com/test3_11.html
处理数据： http://www.baidu.com/test3_12.html
处理数据： http://www.baidu.com/test3_13.html
处理数据： http://www.baidu.com/test3_14.html
处理数据： http://www.baidu.com/test3_15.html
处理数据： http://www.baidu.com/test3_16.html
处理数据： http://www.baidu.com/test3_17.html
处理数据： http://www.baidu.com/test3_18.html
处理数据： http://www.baidu.com/test3_19.html
处理数据： http://www.baidu.com/test4_0.html
处理数据： http://www.baidu.com/test4_1.html
处理数据： http://www.baidu.com/test4_2.html
处理数据： http://www.baidu.com/test4_3.html
处理数据： http://www.baidu.com/test4_4.html
处理数据： http://www.baidu.com/test4_5.html
处理数据： http://www.baidu.com/test4_6.html
处理数据： http://www.baidu.com/test4_7.html
处理数据： http://www.baidu.com/test4_8.html
处理数据： http://www.baidu.com/test4_9.html
处理数据： http://www.baidu.com/test4_10.html
处理数据： http://www.baidu.com/test4_11.html
处理数据： http://www.baidu.com/test4_12.html
处理数据： http://www.baidu.com/test4_13.html
处理数据： http://www.baidu.com/test4_14.html
处理数据： http://www.baidu.com/test4_15.html
处理数据： http://www.baidu.com/test4_16.html
处理数据： http://www.baidu.com/test4_17.html
处理数据： http://www.baidu.com/test4_18.html
处理数据： http://www.baidu.com/test4_19.html
消耗的时间:8.018893957138062秒

"""
