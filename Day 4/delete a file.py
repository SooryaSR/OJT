#  Write a python program to Delete a file

import os

file_name = 'example.txt'

if os.path.exists(file_name):
   
    os.remove(file_name)
    print(f'{file_name} has been deleted.')
else:
    print(f'{file_name} does not exist.')
