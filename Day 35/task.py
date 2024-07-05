def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def sum_proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def check_amicable_numbers(num1, num2):
    if num1 == num2:
        return False
    return sum_proper_divisors(num1) == num2 and sum_proper_divisors(num2) == num1

def right_shift(num, n):
    return num >> n

def factorial_digit(digit):
    if digit == 0:
        return 1
    else:
        return factorial(digit)

def check_strong_number(num):
    num_str = str(num)
    sum_factorials = sum(factorial_digit(int(digit)) for digit in num_str)
    return sum_factorials == num

num1 = 12321
num2 = 12345
if is_palindrome(num1):
    print(f"Given number {num1} is a palindrome")
else:
    print(f"Given number {num1} is not a palindrome")

if is_palindrome(num2):
    print(f"Given number {num2} is a palindrome")
else:
    print(f"Given number {num2} is not a palindrome")

num1 = 220
num2 = 284
if check_amicable_numbers(num1, num2):
    print(f"{num1} and {num2} are amicable numbers")
else:
    print(f"{num1} and {num2} are not amicable numbers")

num = 60
n = 2
result = right_shift(num, n)
print(f"Result of right shift of {num} by {n} positions is {result}")

num = 145
if check_strong_number(num):
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")
