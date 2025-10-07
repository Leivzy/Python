import tkinter as tk
from tkinter import messagebox
import mysql.connector

# 配置数据库连接
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'book_management'
}

def connect_db():
    return mysql.connector.connect(**config)

def show_books():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT name, author, price FROM books")
    rows = cursor.fetchall()
    db.close()

    book_list.delete(0, tk.END)
    for book in rows:
        book_list.insert(tk.END, f"书名: {book[0]}, 作者: {book[1]}, 价格: {book[2]} ￥")

def add_book():
    name = entry_name_add.get()
    author = entry_author_add.get()
    price = entry_price_add.get()

    if not name or not author or not price:
        messagebox.showwarning("输入错误", "所有字段都是必填的")
        return

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM books WHERE name = %s", (name,))
    if cursor.fetchone()[0] > 0:
        messagebox.showwarning("添加失败", "图书已存在!")
    else:
        cursor.execute("INSERT INTO books (name, author, price) VALUES (%s, %s, %s)", (name, author, price))
        db.commit()
        messagebox.showinfo("添加成功", "图书添加成功!")
        show_books()
    db.close()

def delete_book():
    name = entry_name_delete.get()

    if not name:
        messagebox.showwarning("输入错误", "请输入书名")
        return

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM books WHERE name = %s", (name,))
    if cursor.rowcount > 0:
        db.commit()
        messagebox.showinfo("删除成功", "图书删除成功!")
        show_books()
    else:
        messagebox.showwarning("删除失败", "图书不存在")
    db.close()

def modify_book():
    name = entry_name_modify.get()
    new_name = entry_new_name_modify.get()
    new_author = entry_new_author_modify.get()
    new_price = entry_new_price_modify.get()

    if not name or not new_name or not new_author or not new_price:
        messagebox.showwarning("输入错误", "所有字段都是必填的")
        return

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM books WHERE name = %s", (name,))
    if cursor.fetchone()[0] == 0:
        messagebox.showwarning("修改失败", "图书不存在")
    else:
        cursor.execute("UPDATE books SET name = %s, author = %s, price = %s WHERE name = %s", (new_name, new_author, new_price, name))
        db.commit()
        messagebox.showinfo("修改成功", "图书修改成功!")
        show_books()
    db.close()

def search_book():
    name = entry_name_search.get()

    if not name:
        messagebox.showwarning("输入错误", "请输入书名")
        return

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT name, author, price FROM books WHERE name = %s", (name,))
    row = cursor.fetchone()
    db.close()

    book_list.delete(0, tk.END)
    if row:
        book_list.insert(tk.END, f"书名: {row[0]}, 作者: {row[1]}, 价格: {row[2]} ￥")
    else:
        messagebox.showwarning("查询失败", "图书不存在")

def hide_all_frames():
    frame_add.grid_forget()
    frame_delete.grid_forget()
    frame_modify.grid_forget()
    frame_search.grid_forget()

# 创建主窗口
root = tk.Tk()
root.title("图书管理系统")

# 创建功能按钮
tk.Button(root, text="显示所有图书", command=show_books).grid(row=0, column=0, columnspan=2)
tk.Button(root, text="添加图书", command=lambda: show_frame(frame_add)).grid(row=1, column=0, columnspan=2)
tk.Button(root, text="删除图书", command=lambda: show_frame(frame_delete)).grid(row=2, column=0, columnspan=2)
tk.Button(root, text="修改图书", command=lambda: show_frame(frame_modify)).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="查询图书", command=lambda: show_frame(frame_search)).grid(row=4, column=0, columnspan=2)

# 创建图书列表框
book_list = tk.Listbox(root, width=50, height=15)
book_list.grid(row=5, column=0, columnspan=2)

# 创建各功能的输入框和按钮
frame_add = tk.Frame(root)
tk.Label(frame_add, text="书名:").grid(row=0, column=0)
entry_name_add = tk.Entry(frame_add)
entry_name_add.grid(row=0, column=1)
tk.Label(frame_add, text="作者:").grid(row=1, column=0)
entry_author_add = tk.Entry(frame_add)
entry_author_add.grid(row=1, column=1)
tk.Label(frame_add, text="价格:").grid(row=2, column=0)
entry_price_add = tk.Entry(frame_add)
entry_price_add.grid(row=2, column=1)
tk.Button(frame_add, text="添加", command=add_book).grid(row=3, column=0, columnspan=2)

frame_delete = tk.Frame(root)
tk.Label(frame_delete, text="书名:").grid(row=0, column=0)
entry_name_delete = tk.Entry(frame_delete)
entry_name_delete.grid(row=0, column=1)
tk.Button(frame_delete, text="删除", command=delete_book).grid(row=1, column=0, columnspan=2)

frame_modify = tk.Frame(root)
tk.Label(frame_modify, text="书名:").grid(row=0, column=0)
entry_name_modify = tk.Entry(frame_modify)
entry_name_modify.grid(row=0, column=1)
tk.Label(frame_modify, text="新书名:").grid(row=1, column=0)
entry_new_name_modify = tk.Entry(frame_modify)
entry_new_name_modify.grid(row=1, column=1)
tk.Label(frame_modify, text="新作者:").grid(row=2, column=0)
entry_new_author_modify = tk.Entry(frame_modify)
entry_new_author_modify.grid(row=2, column=1)
tk.Label(frame_modify, text="新价格:").grid(row=3, column=0)
entry_new_price_modify = tk.Entry(frame_modify)
entry_new_price_modify.grid(row=3, column=1)
tk.Button(frame_modify, text="修改", command=modify_book).grid(row=4, column=0, columnspan=2)

frame_search = tk.Frame(root)
tk.Label(frame_search, text="书名:").grid(row=0, column=0)
entry_name_search = tk.Entry(frame_search)
entry_name_search.grid(row=0, column=1)
tk.Button(frame_search, text="查询", command=search_book).grid(row=1, column=0, columnspan=2)

def show_frame(frame):
    hide_all_frames()
    frame.grid(row=6, column=0, columnspan=2)

# 隐藏所有功能框
hide_all_frames()

# 启动主循环
root.mainloop()
