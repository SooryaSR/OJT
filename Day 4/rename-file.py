#Write a Python program that renames a file named ‘old_name.txt to’ ‘new_name.txt’.

import os
old_name = 'example.txt'
new_name = 'myfile.txt'


if os.path.exists(old_name):
   
    os.rename(old_name, new_name)
    print(f'{old_name} has been renamed to {new_name}.')
else:
    print(f'{old_name} does not exist.')
