# 获取用户输入的身高
height = int(input("请输入你的身高（cm）："))

# 判断身高是否超过120cm
if height > 120:
    print(f"欢迎来到白云山公园\n您的身高是{height}cm，游玩需要购票，票价10元。\n祝您游玩愉快！")
else:
    print(f"欢迎来到白云山公园\n您的身高是{height}cm，您的身高未超过120cm，可以免费游玩。\n祝您游玩愉快！")
