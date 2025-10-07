class_num = 10
avg_salary = 10000
message = "num:%s, salary:%s" % (class_num, avg_salary)
print(message)

a = "某公司"
b = 2002
c = 19.9
print("%s成立于%d年，注册资本为%.2f亿" % (a, b, c))
print(a + "成立于", b, "年，注册资本为", c, "亿")
print("{}成立于{}年，注册资本为{:.2f}亿".format(a, b, c))
print(f"{a}成立于{b}年，注册资本为{c:.2f}亿")

num1 = 11
num2 = 11.2345

print("num1的值为%5d" % num1)
print("num2的值为%5.2f" % num2)
print(f"num1:{num1},num2:{num2}")
