
# 有一个列表，内容是：[21，25，21，23，22，20]，记录的是一批学生的年龄。

# 请通过列表的功能（方法），对其进行：

#     定义这个列表，并用变量接收它
#     追加一个数字31，到列表的尾部
#     追加一个新列表[29，33，30]，到列表的尾部
#     取出第一个元素（应是：21）
#     取出最后一个元素（应是：30）
# #     查找元素31，在列表中的下标位置

# 1. 定义列表，并使用变量接收它
student_ages = [21, 25, 21, 23, 22, 20]

# 2. 添加一个数字31，到列表的尾部
student_ages.append(31)

# 3. 添加一个新列表[29, 33, 30]，到列表的尾部
student_ages.extend([29, 33, 30])

# 4. 取出第一个元素
first_element = student_ages[0]
print(f"第一个元素是: {first_element}")

# 5. 取出最后一个元素
last_element = student_ages[-1]
print(f"最后一个元素是: {last_element}")

# 6. 查找元素31，在列表中的下标位置
index_of_31 = student_ages.index(31)
print(f"元素31的下标位置是: {index_of_31}")

# 打印最终的列表
print(f"更新后的列表: {student_ages}")
