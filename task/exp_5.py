# # 创建字典，初始化账号和密码
# dic = {
#     "user": "123456",
#     "admin": "123456",
# }

# # 定义最大尝试次数
# max_attempts = 3

# # 登录逻辑
# for attempt in range(1, max_attempts + 1):
#     # 输入账号和密码
#     username = input(f"尝试 {attempt}/{max_attempts} - 请输入账号：")
#     password = input("请输入密码：")
    
#     # 检查账号和密码是否匹配
#     if dic.get(username) == password:
#         print("登录成功！")
#         break
#     else:
#         print("账号或密码错误，请重试。")
        
#     # 如果超过最大尝试次数
#     if attempt == max_attempts:
#         print("登录失败，超过最大尝试次数。")


# # (1) 定义一个空集合
# my_set = set()

# # 定义列表对象
# my_list = ['广州理工学院', '计算机学院', '计算机系', '计算机学院', 'China', 'it', 'well', 'it', 'best']

# # (2) 通过for循环遍历列表
# for item in my_list:
#     # (3) 如果元素包含子字符串“学院”或“China”则添加到集合
#     if "学院" in item or "China" in item:
#         my_set.add(item)

# # (4) 打印输出集合对象
# print("集合 my_set:", my_set)

# # (5) 计算并打印集合的长度
# print("集合长度:", len(my_set))


# 练习1:定义两个列表
list_name = ["张无忌", "赵敏", "周芷若"]
list_room = [101, 102, 103]

# 使用zip函数将两个列表合并为字典
dict_room_to_name = dict(zip(list_room, list_name))

# 打印结果
print("练习1结果：", dict_room_to_name)


# 练习2:颠倒字典键值
dict_name_to_room = {value: key for key, value in dict_room_to_name.items()}

# 打印结果
print("练习2结果：", dict_name_to_room)
