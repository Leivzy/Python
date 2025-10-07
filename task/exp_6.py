# def filter_and_group(lst, condition):
#     satisfied = [item for item in lst if condition(item)]
#     not_satisfied = [item for item in lst if not condition(item)]
#     return satisfied, not_satisfied

# def is_even(num):
#     return num % 2 == 0

# if __name__ == "__main__":
#     example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     even_numbers, odd_numbers = filter_and_group(example_list, is_even)

#     print("满足条件的元素（偶数）:", even_numbers)
#     print("不满足条件的元素（奇数）:", odd_numbers)



# def fibonacci_sum(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci_sum(n - 1) + fibonacci(n - 1)

# def fibonacci(k):
#     if k == 0:
#         return 0
#     if k == 1:
#         return 1
#     return fibonacci(k - 1) + fibonacci(k - 2)

# if __name__ == "__main__":
#     n = 10
#     result = fibonacci_sum(n)
#     print(f"斐波那契数列前 {n} 项的和为: {result}")


def factorial(n):
    if n < 0:
        raise ValueError("n 必须是非负整数")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n, k):
    if k < 0 or k > n:
        raise ValueError("k 必须满足 0 <= k <= n")
    return factorial(n) // (factorial(k) * factorial(n - k))

if __name__ == "__main__":
    n = 5
    fact_result = factorial(n)
    print(f"{n}! = {fact_result}")

    n, k = 5, 2
    comb_result = combination(n, k)
    print(f"C({n}, {k}) = {comb_result}")
