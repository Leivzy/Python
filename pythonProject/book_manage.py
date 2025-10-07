book_info = [
    {"name": "操作系统", "author": "吴欢", "price": "50"},
    {"name": "高级架构技术", "author": "孙伟", "price": "60"},
    {"name": "编译原理", "author": "李畅", "price": "70"},
    {"name": "算法与数据结构", "author": "原福永", "price": "80"},
]
def print_menu():
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
    # print("书名---作者---价格")
    print("图书列表:")
    for book in book_info:
        print("书名:",book["name"],"\t","作者:",book["author"],"\t","价格:",book["price"],"￥")
    print("\n")
def add_book():
    print("欢迎使用图书添加功能")
    global book_info
    name = input("请输入图书名:")
    author = input("请输入图书作者:")
    price = input("请输入图书价格")

    # for i in book_info:
    #     if i["name"] == name:
    #         print("图书已存在!")
    #     else:
    #         book = {
    #             "name": name,
    #             "author": author,
    #             "price": price
    #         }
    #
    #         book_info.append(book)
    #         print("图书添加成功!")
    #         break
    book_exists = False
    for i in book_info:
        if i["name"] == name:
            book_exists = True
            break

    if book_exists:
        print("\n=== 图书已存在! ===\n")
    else:
        book = {
            "name": name,
            "author": author,
            "price": price
        }
        book_info.append(book)
        print("\n=== 图书添加成功! ===\n")


def del_book():
    print("图书删除功能")
    global book_info
    name = input("请输入删除的书名:")
    for i in book_info:
        if i["name"] == name:
            book_info.remove(i)
            print("\n=== 图书删除成功! ===\n")
            return

    print("\n=== 图书不存在 ===\n")


def modify_book():
    global book_info
    name = input("请输入需要修改的图书名称:")
    for i in book_info:
        if i["name"] == name:
            i["name"] = input("请输入修改后的书名:")
            i["author"] = input("请输入修改后的作者:")
            i["price"] = input("请输入修改后的价格:")
            print("\n=== 图书修改成功! ===\n")
            return

    print("\n=== 图书不存在 ===\n")


def search_book():
    global book_info
    name = input("请输入需要查找的书名:")
    for i in book_info:
        if i["name"] == name:

            print("-------")
            print("查询结果:")
            print("书名:",i["name"])
            print("作者:",i["author"])
            print("价格:",i["price"],"￥")
            print("-------")
            return
    print("\n=== 图书不存在 ===\n")


def main():
    while True:
        # print("--")
        print_menu()
        choose = int(input("请输入您需要的功能:"))

        if choose == 1:
            show_book()
        elif choose == 2:
            add_book()
        elif choose == 3:
            del_book()
        elif choose == 4:
            modify_book()
        elif choose == 5:
            search_book()
        elif choose == 6:
            print("\n=== 退出系统 ===\n")
            break
        else:
            print("无效选择，请重新输入.")



if __name__ == "__main__":
    main()
