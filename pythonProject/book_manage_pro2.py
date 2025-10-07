import decimal
import mysql.connector
from mysql.connector import Error
# 配置数据库连接
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'book_management'
}

def connect_db():
    """连接数据库并返回连接对象"""
    return mysql.connector.connect(**config)

def print_menu():
    """打印系统菜单"""
    print("┌--------------------┐")
    print("│     图书管理系统     │")
    print("│ 1.显示所有图书       │")
    print("│ 2.添加图书          │")
    print("│ 3.删除图书          │")
    print("│ 4.修改图书          │")
    print("│ 5.查询图书          │")
    print("│ 6.退出系统          │")
    print("└--------------------┘")

def show_book():
    """显示所有图书信息"""
    db = connect_db()  # 连接数据库
    cursor = db.cursor()  # 创建游标对象
    cursor.execute("SELECT name, author, price FROM books")  # 执行查询
    rows = cursor.fetchall()  # 获取所有查询结果
    db.close()  # 关闭数据库连接

    # 打印图书列表
    print("图书列表:")
    print("-------")
    for book in rows:
        print("书名:", book[0], "\t", "作者:", book[1], "\t", "价格:", book[2], "￥")
    print("-------")
    print("\n")

def add_book():
    """添加图书"""
    print("欢迎使用图书添加功能")
    name = input("请输入图书名: ")
    author = input("请输入图书作者: ")
    price = input("请输入图书价格: ")

    try:
        price = decimal.Decimal(price)
    except decimal.InvalidOperation:
        print("\n=== 无效的价格! 请输入一个有效的数字 ===\n")
        return

    db = connect_db()  # 连接数据库
    cursor = db.cursor()  # 创建游标对象
    cursor.execute("SELECT COUNT(*) FROM books WHERE name = %s", (name,))
    if cursor.fetchone()[0] > 0:
        print("\n=== 图书已存在! ===\n")
    else:
        cursor.execute("INSERT INTO books (name, author, price) VALUES (%s, %s, %s)", (name, author, price))
        db.commit()  # 提交事务
        print("\n=== 图书添加成功! ===\n")
    db.close()  # 关闭数据库连接

def delete_book():
    """删除图书"""
    print("图书删除功能")
    name = input("请输入删除的书名: ")

    db = connect_db()  # 连接数据库
    cursor = db.cursor()  # 创建游标对象
    cursor.execute("DELETE FROM books WHERE name = %s", (name,))
    if cursor.rowcount > 0:
        db.commit()  # 提交事务
        print("\n=== 图书删除成功! ===\n")
    else:
        print("\n=== 图书不存在 ===\n")
    db.close()  # 关闭数据库连接

def modify_book():
    """修改图书信息"""
    print("图书修改功能")
    name = input("请输入需要修改的图书名称: ")

    db = connect_db()  # 连接数据库
    cursor = db.cursor()  # 创建游标对象
    cursor.execute("SELECT COUNT(*) FROM books WHERE name = %s", (name,))
    if cursor.fetchone()[0] == 0:
        print("\n=== 图书不存在 ===\n")
    else:
        new_name = input("请输入修改后的书名: ")
        new_author = input("请输入修改后的作者: ")
        new_price = input("请输入修改后的价格: ")
        cursor.execute("UPDATE books SET name = %s, author = %s, price = %s WHERE name = %s",
                       (new_name, new_author, new_price, name))
        db.commit()  # 提交事务
        print("\n=== 图书修改成功! ===\n")
    db.close()  # 关闭数据库连接

def search_book():
    """查询图书信息"""
    print("图书查询功能")
    name = input("请输入需要查找的书名: ")

    db = connect_db()  # 连接数据库
    cursor = db.cursor()  # 创建游标对象
    cursor.execute("SELECT name, author, price FROM books WHERE name = %s", (name,))
    row = cursor.fetchone()  # 获取查询结果
    db.close()  # 关闭数据库连接

    if row:
        # 打印查询结果
        print("-------")
        print("查询结果:")
        print("书名:", row[0])
        print("作者:", row[1])
        print("价格:", row[2], "￥")
        print("-------")
    else:
        print("\n=== 图书不存在 ===\n")

def main():
    """主函数，显示菜单并处理用户输入"""
    while True:
        print_menu()  # 打印菜单
        # choose = int(input("请输入您需要的功能:"))
        choose = input("请输入您需要的功能:")
        if choose == "1":
            show_book()  # 显示所有图书
        elif choose == "2":
            add_book()  # 添加图书
        elif choose == "3":
            delete_book()  # 删除图书
        elif choose == "4":
            modify_book()  # 修改图书
        elif choose == "5":
            search_book()  # 查询图书
        elif choose == "6":
            print("\n=== 退出系统 ===\n")
            break  # 退出循环
        else:
            print("\n=== 无效选择，请重新输入 ===\n")

if __name__ == "__main__":
    main()  # 运行主函数
