# Write a Python program to Read/Write to a File 

with open('example.txt', 'w') as file:
    file.write('Hello, world!')
    print("successfully example.txt file")


with open('example.txt', 'r') as file:
    content = file.read()

print('Content of example.txt:')
print(content)
