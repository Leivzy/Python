# # 用户输入一个整数，并同步赋值
# number = int(input("请输入一个整数: "))
# if number % 2 == 0:  
#     print(f"{number} 是偶数")
# else: 
#     print(f"{number} 是奇数")




# pm = float(input("请输入PM2.5的监测值: "))

# if pm <= 35:
#     print("空气质量等级：优")
# elif 35 < pm <= 75:
#     print("空气质量等级：良")
# elif 75 < pm <= 115:
#     print("空气质量等级：轻度污染")
# elif 115 < pm <= 150:
#     print("空气质量等级：中度污染")
# elif 150 < pm <= 250:
#     print("空气质量等级：重度污染")
# else:
#     print("空气质量等级：严重污染")

# #嵌套while:
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {j * i}", end="\t")
#         j += 1
#     print()  # 换行
#     i += 1

# # 嵌套for:
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {j * i}", end="\t")
#     print()  # 换行

# #for 和 while 混合嵌套
# for i in range(1, 10):
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {j * i}", end="\t")
#         j += 1
#     print()  # 换行


# for i in range(1, 101):
#     if i % 3 != 0:  
#         print(i, end=" ")

# # 初始值
# numerator = 2  # 分子
# denominator = 1  # 分母
# sum_series = 0  # 累加和

# # 计算前 100 项和
# for _ in range(100):
#     sum_series += numerator / denominator
#     # 更新分子和分母，斐波那契数列的下一项
#     numerator, denominator = numerator + denominator, numerator

# # 输出结果
# print(f"数列前100项的和是: {sum_series}")


# # 输出100以内的素数
# for num in range(2, 101): 
#     is_prime = True  
#     for i in range(2, int(num ** 0.5) + 1): 
#         if num % i == 0:  
#             is_prime = False
#             break 
#     if is_prime:  
#         print(num, end=" ")
