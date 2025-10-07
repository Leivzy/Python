# 2-1
# print("命运掌握在自己手里，命运的好坏由自己去创造")

# 2-2
# x = "知识";y = "就是";z = "力量";print(x,y,z)

# 2-3
# a = "你有多努力"
# b = "就有多幸运"
# c = b
# print(a,b)
# print(a,c)

# 2-4
# x = 10+\
#     2+\
#     3
# print(x)
# y = (10+
#      2+
#      3)
# print(y)

# 2-5
# x = int(input("请输入x="))
# y = int(input("请输入y="))
# z = int(input("请输入z="))
# if x >= y:
#     x,y = y,x
# if x >= z:
#     x,z = z,x
# if y >= z:
#     y,z = z,y
# print("x:",x)
# print("y:",y)
# print("z:",z)

# 2-6
def print_hearts(num):
    hearts = '♥' * num
    print(hearts)

book = input("请输入最喜欢的书籍: ")
num = int(input("请为<<{}>>打分(1~10):".format(book)))

if num < 1 or num > 10:
    print("请输入有效的评分(1~10之间的整数)!")
else:
    print("你对<<{}>>的评分为: ".format(book))
    print_hearts(num)