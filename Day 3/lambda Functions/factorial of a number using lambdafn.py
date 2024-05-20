from functools import reduce

# Define a lambda function to calculate the factorial of a number

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else 1
number = 5
result = factorial(number)
print("Factorial of", number, "is:", result)