# # 获取用户输入
# name = input("请输入您的姓名: ")
# age = input("请输入您的年龄: ")
# gender = input("请输入您的性别: ")

# # 使用 .format() 格式化字符串
# output = "我叫{}，今年{}岁，性别是{}。".format(name, age, gender)

# # 输出结果
# print(output)



# # 获取用户输入的华氏温度
# F = float(input("请输入华氏温度: "))

# # 将华氏温度转换为摄氏温度
# C = (F - 32) * 5 / 9

# # 输出转换后的摄氏温度
# print("对应的摄氏温度是: {:.2f}°C".format(C))



# # 获取每一科的成绩，注意这里是分别输入
# english = float(input("请输入大学英语成绩: "))
# python = float(input("请输入Python语言编程成绩: "))
# marxism = float(input("请输入马克思主义哲学成绩: "))
# algebra = float(input("请输入线性代数成绩: "))

# # 计算总和
# total = english + python + marxism + algebra

# # 计算平均值
# average = total / 4

# # 计算最大值和最小值
# max_score = max(english, python, marxism, algebra)
# min_score = min(english, python, marxism, algebra)

# # 输出结果
# print("成绩总和: {:.2f}".format(total))
# print("成绩平均值: {:.2f}".format(average))
# print("最高分: {:.2f}".format(max_score))
# print("最低分: {:.2f}".format(min_score))



# # 获取用户输入的四位整数
# number = int(input("请输入一个四位整数: "))

# # 计算各位数字
# ones = number % 10           # 个位
# tens = (number // 10) % 10    # 十位
# hundreds = (number // 100) % 10   # 百位
# thousands = (number // 1000) % 10 # 千位

# # 输出结果
# print("千位: {}".format(thousands))
# print("百位: {}".format(hundreds))
# print("十位: {}".format(tens))
# print("个位: {}".format(ones))





# # 导入 math 模块
# import math

# # 获取用户输入的半径，并转换为浮点数
# r = float(input("请输入圆的半径: "))

# # 计算圆的面积，使用 math.pi
# area = math.pi * r ** 2

# # 输出结果
# print("圆的面积是: {:.2f}".format(area))





# 创建变量并赋值
x = "Learning Python makes me happy"

# 1. 判断 'e' 出现的次数
e_count = x.count('e')

# 2. 判断字符串是否为空
is_empty = len(x) == 0

# 3. 判断字符串是否为大写
is_upper = x.isupper()

# 4. 判断字符串是否由字母和数字组成
is_alnum = x.isalnum()

# 5. 求字符串的长度
length = len(x)

# 输出结果
print("字符 'e' 出现的次数: {}".format(e_count))
print("字符串是否为空: {}".format(is_empty))
print("字符串是否为大写: {}".format(is_upper))
print("字符串是否由字母和数字组成: {}".format(is_alnum))
print("字符串的长度: {}".format(length))
