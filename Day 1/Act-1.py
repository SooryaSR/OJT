#  Write a Python program to swap two numbers without using a temporary variable.

a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("first number is",a)
print("second number is",b)

a=a+b
b=a-b
a=a-b

print("a=",a)
print("b=",b)
  