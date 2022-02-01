# encoding: utf-8
'''
@author: developer
@software: python
@file: bookManage.py
@time: 2022/2/1 11:49
@desc:
'''

'''
操作mysql数据库进行crud操作 

'''
import pymysql


class DB:
    """操作数据库的类封装"""

    def __init__(self):
        # 连接数据库
        self.con = pymysql.connect(host="127.0.0.1",
                                   user="root",
                                   password="root",
                                   database='test',
                                   port=3306,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def execute_sql(self, sql):
        # 执行增删改sql的方法
        res = self.cur.execute(sql)
        self.con.commit()
        return res

    def find_sql(self, sql):
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def close(self):
        """关闭游标，断开数据库连接"""
        self.cur.close()
        self.con.close()


class BookManage:
    def __init__(self):
        self.db = DB()

    def print_menu(self):
        """打印菜单"""
        print("-------------菜单------------------")
        print("【1】：添加图书")
        print("【2】：修改图书")
        print("【3】：删除图书")
        print("【4】：查询图书")
        print("【5】：图书列表")
        print("【6】：出借图书")
        print("【7】：归还图书")
        print("【8】：退出")

    def add_book(self):
        """添加图书"""
        print("**************添加图书****************")
        name = input("请输入图书名：")
        position = input("请输入图书位置：")
        if name and position:
            sql = "insert into books(name,position) value ('{}','{}')".format(name, position)
            self.db.execute_sql(sql)
            print("***************图书添加成功！*******************")
        else:
            print("书名和位置不能为空！")
        n = input("继续添加请输入1，回车退回主菜单:")
        if n == '1':
            self.add_book()
        else:
            return
            # or pass

    def update_book(self):
        """修改图书"""
        print("**************修改图书****************")
        id = input("请输入要修改书籍的编号：")
        res = self.db.find_sql("select * from books where id={}".format(id))
        if res:
            print('当前书籍信息如下', res)
            name = input('请输入新的书名，如果不修改直接回车:')
            position = input('请输入位置，如果不修改直接回车:')
            if name and position:
                sql = 'update books set name ="{}" position ="{}" where id={}'.format(name, position, id)
                self.db.execute_sql(sql)
                print("*****************修改成功******************")
            elif name:
                sql = 'update books set name ="{}" where id={}'.format(name, id)
                self.db.execute_sql(sql)
                print("*****************修改成功******************")
            elif position:
                sql = 'update books set position ="{}" where id={}'.format(position, id)
                self.db.execute_sql(sql)
                print("*****************修改成功******************")
            else:
                print("没有输入新的内容，未进行修改操作！")
        else:
            print('您输入的的id有误！')

    def del_book(self):
        """删除图书"""
        print("**************删除图书****************")
        id = input("请输入需要删除的图书id:")
        res = self.db.execute_sql("select * from books where id='{}'".format(id))
        if res:
            sql = "delete from books where id='{}'".format(id)
            self.db.execute_sql(sql)
            print("**********************删除成功！*******************")
        else:
            print("系统中没有找到这本书！")
        n = input("继续删除请输入3, 回车退回主菜单：")
        if n == '3':
            self.del_book()
        else:
            return

    def find_book(self):
        """查询图书"""
        print("**************查询图书****************")
        name = input("请输入图书名：")
        if name:
            sql = "select * from books where name='{}'".format(name)
            res = self.db.find_sql(sql)
            print("找到的图书信息如下：")
            for item in res:
                print(item)
        else:
            print("书名不能为空！")
        n = input("继续查询请输入4，回车退回主菜单！")
        if n == '4':
            self.find_book()
        else:
            return

    def book_list(self):
        """图书列表"""
        print("**************图书列表****************")
        sql = "select * from books"
        res = self.db.find_sql(sql)
        # print(res)
        for item in res:
            # print(item)
            print(
                f"编号：{item['id']}，书名:{item['name']}， 位置:{item['position']}，状态:{item['status']}，借阅人:{item['borrower']}")

    def lend_book(self):
        """出借图书"""
        print("**************出借图书****************")
        bookId = input("请输入需要借阅的书籍的编号:")
        borrowerName =input("请输入您的名字")
        sql1 = "select status from books where id='{}'".format(bookId)
        res = self.db.find_sql(sql1)
        #print(res)
        if res[0]['status'] == '在库':
            sql2 = "update books set status='出借', borrower='{}' where id='{}'".format(borrowerName, bookId)
            print(sql2)
            self.db.execute_sql(sql2)
        elif res[0]['status'] == '出借':
            print("图书已经借出，无法借阅！请查询其他书籍~")
        else:
            print("图书馆馆藏查无此书！")





    def revert_book(self):
        """归还图书"""
        print("**************归还图书****************")
        bookId = input("请输入需要归还的书籍的编号:")
        borrowerName = input("请输入您的名字")
        sql1 = "select status from books where id='{}'".format(bookId)
        sql2 = "select borrower from books where id='{}'".format(bookId)
        res = self.db.find_sql(sql1)
        res2 = self.db.find_sql(sql2)
        if res[0]['status'] == '出借' and res2[0]['borrower'] == borrowerName:
            sql3 = "update books set status='在库', borrower='' where id='{}'".format(bookId)
            print(sql3)
            self.db.execute_sql(sql3)
        elif res[0]['status'] == '在库':
            print("图书已经在库，无法归还！请确认后再归还~")
        else:
            print("图书馆馆藏查无此书！")

    def quit(self):
        """退出程序"""
        """断开数据库连接"""
        self.db.close()

    def main(self):
        """程序运行的流程控制"""
        print("-----------欢迎进入图书管理系统------------")
        while True:
            self.print_menu()
            number = input("请输入选项：")
            # 判断用户输入的数据
            if number == '1':
                # 添加图书
                self.add_book()
            elif number == '2':
                # 修改图书
                self.update_book()
            elif number == '3':
                # 删除图书
                self.del_book()
            elif number == '4':
                # 查询图书
                self.find_book()
            elif number == '5':
                # 图书列表
                self.book_list()
            elif number == '6':
                # 出借图书
                self.lend_book()
            elif number == '7':
                # 归还图书
                self.revert_book()
            elif number == '8':
                # 退出
                self.quit()
                break
            else:
                print("您输入的选项有误！请参照菜单进行输入")


if __name__ == '__main__':
    BookManage().main()
