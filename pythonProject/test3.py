import numpy as np
teacher = ["a", "b", "c", "d", "e" , "f", "g","h"]
office = [[],[],[]]
for i in teacher:
    num = np.random.randint(0,3)
    office[num].append(i)
index = 1
for j in office:
    print(f'第{index}个办公室的人数为{len(j)}')
    for name in j:
        print(name)
    index += 1

print("===========================")



num = np.random.randint(0,101,10)
num_tuple = tuple(num)
odd = (i for i in num_tuple if i % 2 != 0)
print(tuple(odd))



print("===========================")




dic = {"123":"123", "456":"456", "789":"789"}
number = input("请输入账号")
password = input("请输入密码")
if number in dic.keys():
    if dic[number] == password:
        print("登录成功")
    else:
        print("密码错误")
else:
    print("账号不存在")




print("===========================")



entrance = ""
set1 = set()
while entrance != '0':
    entrance = input("请输入元素: ")
    set1_len = len(set1)
    if entrance != '0':
        set1.add(entrance)
        if set1_len == len(entrance):
            print("输入重复")
            break




