#Write a Python program to print the multiplication table of a number using a for loop.

num= int(input("enter number:"))

print("multiplication table of ", num)

for i in range (1,11):
    print(num,"x",i,"=",num* i)