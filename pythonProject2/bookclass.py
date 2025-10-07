class Book:
    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"书名: {self.title}")
        print(f"作者: {self.author}")
        print(f"页数: {self.pages}")


if __name__ == "__main__":
    # 创建一个 Book 实例
    my_book = Book("Python编程", "Guido van Rossum", 350)
    # 显示书的信息
    my_book.display_info()
