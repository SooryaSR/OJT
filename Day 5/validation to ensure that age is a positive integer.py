 #Create a class called Person with attributes for name, age, and email. 
 #Implement validation to ensure that age is a positive integer and email follows a valid format.

import re

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age if isinstance(age, int) and age > 0 else None
        self.email = email if re.match(r"[^@]+@[^@]+\.[^@]+", email) else None

person1 = Person("soorya", 25, "soorya@gmail.com")
person2 = Person("Beckham", -30, "beckham@gmail")
person3 = Person("Jonas", 35, "khanwald@gmail.com")

print(person1.name, person1.age, person1.email) 
print(person2.name, person2.age, person2.email)
print(person3.name, person3.age, person3.email)
