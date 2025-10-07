# class Student:
#     def __init__(self, student_id, name, age, scores):

#         self.student_id = student_id
#         self.name = name
#         self.age = age
#         self.scores = scores

#     def calculate_average(self):

#         if len(self.scores) == 0:
#             return 0
#         total_score = sum(self.scores.values())
#         num_courses = len(self.scores)
#         return total_score / num_courses

#     def print_student_info(self):

#         print(f"学号: {self.student_id}")
#         print(f"姓名: {self.name}")
#         print(f"年龄: {self.age}")
#         print("成绩:")
#         for course, score in self.scores.items():
#             print(f"  {course}: {score}")
#         print(f"平均成绩: {self.calculate_average():.2f}")


# student1 = Student(
#     student_id="20230101",
#     name="张三",
#     age=20,
#     scores={"数学": 85, "英语": 90, "物理": 78},
# )


# student1.print_student_info()


# class BankAccount:
#     def __init__(self, account_number, account_name, balance=0):
#         # 初始化账户的属性
#         self.account_number = account_number  # 账户号
#         self.account_name = account_name      # 账户名
#         self.balance = balance                # 账户余额

#     def deposit(self, amount):
#         # 存款方法
#         if amount > 0:
#             self.balance += amount
#             print(f"成功存款 {amount} 元。当前余额: {self.balance} 元")
#         else:
#             print("存款金额必须大于 0")

#     def withdraw(self, amount):
#         # 取款方法（基础方法，没有考虑特殊费用或利息）
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"成功取款 {amount} 元。当前余额: {self.balance} 元")
#         else:
#             print("取款金额无效或余额不足")

#     def check_balance(self):
#         # 查看余额方法
#         return self.balance

#     def print_account_info(self):
#         # 打印账户的详细信息
#         print(f"账户号: {self.account_number}")
#         print(f"账户名: {self.account_name}")
#         print(f"账户余额: {self.balance} 元")


# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, account_name, balance=0, interest_rate=0.02):
#         # 储蓄账户继承银行账户，新增利率属性
#         super().__init__(account_number, account_name, balance)
#         self.interest_rate = interest_rate  # 利率

#     def withdraw(self, amount):
#         # 重写取款方法，考虑利息
#         if amount > 0 and amount <= self.balance:
#             # 计算取款后的余额和利息
#             interest = self.balance * self.interest_rate
#             self.balance -= amount
#             self.balance += interest  # 取款后加上利息
#             print(f"成功取款 {amount} 元，利息 {interest:.2f} 元。当前余额: {self.balance:.2f} 元")
#         else:
#             print("取款金额无效或余额不足")

#     def print_account_info(self):
#         # 打印储蓄账户的详细信息
#         super().print_account_info()
#         print(f"利率: {self.interest_rate * 100}%")


# class CheckingAccount(BankAccount):
#     def __init__(self, account_number, account_name, balance=0, transaction_fee=5):
#         # 支票账户继承银行账户，新增手续费属性
#         super().__init__(account_number, account_name, balance)
#         self.transaction_fee = transaction_fee  # 取款手续费

#     def withdraw(self, amount):
#         # 重写取款方法，考虑手续费
#         if amount > 0 and amount <= self.balance:
#             total_deduction = amount + self.transaction_fee
#             if total_deduction <= self.balance:
#                 self.balance -= total_deduction
#                 print(f"成功取款 {amount} 元，手续费 {self.transaction_fee} 元。当前余额: {self.balance} 元")
#             else:
#                 print("余额不足以支付取款金额和手续费")
#         else:
#             print("取款金额无效或余额不足")

#     def print_account_info(self):
#         # 打印支票账户的详细信息
#         super().print_account_info()
#         print(f"取款手续费: {self.transaction_fee} 元")


# # 创建不同类型的账户对象

# # 创建一个普通银行账户
# bank_account = BankAccount("1001", "张三", 1000)

# # 创建一个储蓄账户
# savings_account = SavingsAccount("1002", "李四", 5000, interest_rate=0.03)

# # 创建一个支票账户
# checking_account = CheckingAccount("1003", "王五", 2000, transaction_fee=10)

# # 执行一些操作

# print("\n--- 普通银行账户 ---")
# bank_account.deposit(500)  # 存款
# bank_account.withdraw(200)  # 取款
# print(f"当前余额: {bank_account.check_balance()} 元")
# bank_account.print_account_info()

# print("\n--- 储蓄账户 ---")
# savings_account.deposit(1000)  # 存款
# savings_account.withdraw(2000)  # 取款
# print(f"当前余额: {savings_account.check_balance():.2f} 元")
# savings_account.print_account_info()

# print("\n--- 支票账户 ---")
# checking_account.deposit(500)  # 存款
# checking_account.withdraw(1000)  # 取款
# print(f"当前余额: {checking_account.check_balance()} 元")
# checking_account.print_account_info()


class Book:
    def __init__(self, title, author, isbn, published_year, price):
        # 初始化图书的属性
        self.title = title  # 标题
        self.author = author  # 作者
        self.isbn = isbn  # ISBN
        self.published_year = published_year  # 出版年份
        self.price = price  # 价格

    def __str__(self):
        # 返回图书的字符串表示
        return (
            f"书名: {self.title}\n"
            f"作者: {self.author}\n"
            f"ISBN: {self.isbn}\n"
            f"出版年份: {self.published_year}\n"
            f"价格: ¥{self.price:.2f}"
        )

    def discount_price(self, discount_rate):
        # 计算并返回打折后的价格
        if 0 <= discount_rate <= 1:
            discounted_price = self.price * (1 - discount_rate)
            return discounted_price
        else:
            raise ValueError("折扣率必须在0到1之间")


# 创建一个 Book 对象
book1 = Book(
    title="Python编程从入门到实践",
    author="Eric Matthes",
    isbn="978-7-115-51671-4",
    published_year=2019,
    price=89.00,
)

# 打印图书的详细信息
print(book1)

# 计算并打印打折后的价格
discount_rate = 0.2  # 假设20%的折扣
print(f"\n打折后的价格: ¥{book1.discount_price(discount_rate):.2f}")
