#Write a Python program that reads a file and prints its content. 
#Handle ‘FileNotFoundError’ and ‘PermissionError’ exceptions.

file_name = 'myfile.txt'

try:
    with open(file_name, 'r') as file:
       
        content = file.read()
   
    print('Content of example.txt:')
    print(content)

except FileNotFoundError:
    print(f'Error: {file_name} does not exist.')

except PermissionError:
    print(f'Error: You do not have permission to read {file_name}.')
