def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

result = recursive_sum(100)
print("1到100的累加和是:", result)

print("===========")

def decimalToBinary(n):
    if n >= 1:
        decimalToBinary(n // 2)
    print(n % 2,end=' ')

decimal = int(input("请输入一个整数"))
print("其二进制数为:",end=' ')
decimalToBinary(decimal)

print()
print("=========")


# input_length = input("请输入一个列表，用空格分隔元素: ")
# length = len(input_length)
# for i in range(length//2):
#     tmp = input_length[i]
#     input_length[i] = input_length[length -1 -i]
#     input_length[length -1 -i] = tmp
# print(input_length)
#

def reverse_list(lst):
    length = len(lst)
    for i in range(length // 2):
        tmp = lst[i]
        lst[i] = lst[length - 1 - i]
        lst[length - 1 - i] = tmp
    return lst

user_input = input("请输入一个列表，用空格分隔元素: ")
input_list = user_input.split()

reversed_list = reverse_list(input_list)
print("反转后的列表是:", reversed_list)

print()
print("=========")

def add(num1, num2):
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')

def subtract(num1, num2):
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')

def multiply(num1, num2):
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')

def divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
    else:
        print("除数不能为零")

option = input("选择你要使用的功能: 1. 加法 2. 减法 3. 乘法 4. 除法: ")
num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))

switcher = {
    "1": lambda: add(num1, num2),
    "2": lambda: subtract(num1, num2),
    "3": lambda: multiply(num1, num2),
    "4": lambda: divide(num1, num2)
}

func = switcher.get(option, None)
if func:
    func()
else:
    print("请输入正确的功能标号(1~4)")

