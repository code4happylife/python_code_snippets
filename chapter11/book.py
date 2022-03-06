#!/usr/bin/env python
# encoding: utf-8

import pymysql


class DB:
    def __init__(self):
        self.con = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='1234',
            database='dbtest',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cur = self.con.cursor()

    def query_sql(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def execute_sql(self, sql):
        self.cur.execute(sql)
        return self.con.commit()

    def close(self):
        self.cur.close()
        self.con.close()


class Books:
    def __init__(self):
        self.db = DB()

    def add_book(self):
        """添加图书"""
        print("*****************添加图书******************")
        name = input("请输入书名:")
        position = input("请输入位置:")
        sql = "insert into books2(name,position) value('{}','{}')".format(name, position)
        self.db.execute_sql(sql)
        print('图书添加成功!')
        n = input("任意键回车退回主菜单， 继续添加输入1")
        if n == '1':
            self.add_book()

    def update_book(self):
        """修改图书"""
        print("******************修改图书***************")
        id = input("请输入要修改的书籍编号:")
        res = self.db.query_sql('select * from books2 where id={}'.format(id))
        if res:
            print("您要修改的书籍信息为:", res[0])
            name = input("新书名：")
            position = input("新位置")
            if name and position:
                sql = f'update books2 set name="{name}", position="{position}" where id="{id}"'
                print(sql)
                self.db.execute_sql(sql)
            elif name:
                sql = f'update books2 set name="{name}" where id="{id}"'
                print(sql)
                self.db.execute_sql(sql)
            elif position:
                sql = f'update books2 set position="{position}" where id="{id}"'
                print(sql)
                self.db.execute_sql(sql)
        else:
            print("书籍id不存在")
        n = input("任意键回车退回主菜单， 继续修改输入1")
        if n == '1':
            self.update_book()

    def delete_book(self):
        """删除图书"""
        print("*******************删除图书************************")
        id = input("请输入图书编号：")
        # 先确认对应的图书编号是否存在书籍
        sql1 = f'select * from books2 where id="{id}"'
        res = self.db.query_sql(sql1)
        if res:
            sql2 = f'delete from books2 where id="{id}"'
            self.db.execute_sql(sql2)
            print("删除编号为" + id + "的图书")
        else:
            print("您好，您输入的图书编号不存在")
        n = input("任意键回车退回主菜单， 继续删除图书请输入1")
        if n == '1':
            self.delete_book()


    def borrow_book(self):
        """出借图书"""
        print("*******************出借图书************************")
        id = input("请输入图书编号：")
        sql1 = f'select status from books2 where id="{id}"'
        res1 = self.db.query_sql(sql1)
        if res1[0]['status'] == '在库':
            username = input("请输入借阅人名字")
            sql2 = f'update books2 set borrorwer="{username}",status="出借" where id="{id}"'
            self.db.execute_sql(sql2)
            print("借阅成功")
        else:
            print("借阅失败，图书不存在或不在库")
        n = input("任意键回车退回主菜单， 继续借阅输入1")
        if n == '1':
            self.borrow_book()


    def giveback_book(self):
        """归还图书"""
        print("******************归还图书************************")
        id = input("请输入图书编号：")
        sql1 = f'select status from books2 where id="{id}"'
        res1 = self.db.query_sql(sql1)
        if res1[0]['status'] == '出借':
            sql2 = f'update books2 set borrorwer="", status="在库" where id ="{id}"'
            self.db.execute_sql(sql2)
            print("归还成功")
        else:
            print("归还失败，图书不存在或已经在库")
        n = input("任意键回车退回主菜单， 继续归还请输入1")
        if n == '1':
            self.giveback_book()


    def query_book(self):
        """查询图书"""
        print("*******************查询图书*************************")
        name = input("请输入书名：")
        sql = f'select * from books2 where name="{name}"'
        res = self.db.query_sql(sql)
        if res:
            print(f"找到了{len(res)}本名为{name}的书籍")
            for i in res:
                print(i)
        else:
            print("未找到该书籍")
        n = input("任意键回车退回主菜单， 继续查询输入1")
        if n == '1':
            self.query_book()

    def book_list(self):
        """图书列表"""
        print("****************图书列表***********************")
        sql = "select * from books2"
        res = self.db.query_sql(sql)
        for i in res:
            print(f'编号:{i["id"]},书名:{i["name"]},位置:{i["position"]},状态:{i["status"]},借阅人:{i["borrorwer"]}')
        n = input("任意键回车退回主菜单， 继续查看图书列表请输入1")
        if n == '1':
            self.book_list()

    def menu(self):
        menu = """
===================菜单==========================
【1】:添加图书
【2】:修改图书
【3】:删除图书
【4】:查询图书
【5】:图书列表
【6】:出借图书
【7】:归还图书
【8】:退出
        """
        print(menu)

    def run(self):
        print("=============欢迎进入图书管理系统===================")
        print("""
===================菜单==========================
【1】:添加图书
【2】:修改图书
【3】:删除图书
【4】:查询图书
【5】:图书列表
【6】:出借图书
【7】:归还图书
【8】:退出
        """)
        while True:
            num = input("请选择功能：")
            if num == '1':
                self.add_book()
            elif num == '2':
                print("修改图书")
                self.update_book()
            elif num == '3':
                print("删除图书")
                self.delete_book()
            elif num == '4':
                print("查询图书")
                self.query_book()
            elif num == '5':
                print('图书列表')
                self.book_list()
            elif num == '6':
                print("出借图书")
                self.borrow_book()
            elif num == '7':
                print("归还图书")
                self.giveback_book()
            elif num == '8':
                print("退出")
                self.db.close()
                break
            else:
                print("您的输入有误")
            self.menu()


if __name__ == '__main__':
    book = Books()
    book.run()
