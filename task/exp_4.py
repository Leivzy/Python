# 使用 range() 函数生成 1 到 20 之间的所有偶数列表
# even_list = list(range(2, 21, 2))
# even_tuple = tuple(even_list)
# print(even_tuple)


# # 使用列表推导式生成 1 到 20 之间的所有偶数列表
# even_list = [x for x in range(1, 21) if x % 2 == 0]
# even_tuple = tuple(even_list)
# print(even_tuple)

# import random

# # 生成1到20之间的所有偶数，并转换为元组
# even_list = [x for x in range(1, 21) if x % 2 == 0]
# even_tuple = tuple(even_list)
# print(f"1到20之间的所有偶数组成的元组: {even_tuple}")

# # 创建8个老师和3个办公室
# teachers = ['Teacher1', 'Teacher2', 'Teacher3', 'Teacher4', 'Teacher5', 'Teacher6', 'Teacher7', 'Teacher8']
# offices = [[], [], []]

# # 随机分配老师到办公室
# for teacher in teachers:
#     random.choice(offices).append(teacher)

# # 格式化输出办公室及老师分配情况
# for i, office in enumerate(offices, 1):
#     print(f"\n办公室 {i} 的老师: {', '.join(office) if office else '无'}")



import random

# (1) 生成一个包含10个随机整数的列表，范围在1到100之间
random_list = [random.randint(1, 100) for _ in range(10)]
print(f"生成的随机整数列表: {random_list}")

# (2) 将列表中的每两个相邻整数组合成一个元组，形成一个新的元组列表
tuple_list = [(random_list[i], random_list[i+1]) for i in range(0, len(random_list), 2)]
print(f"组合后的元组列表: {tuple_list}")

# (3) 按照元组的第一个元素进行排序，如果第一个元素相同，则按照第二个元素排序
sorted_tuple_list = sorted(tuple_list, key=lambda x: (x[0], x[1]))

# (4) 打印排序后的元组列表
print(f"排序后的元组列表: {sorted_tuple_list}")
