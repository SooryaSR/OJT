#Write a Python function to calculate the area of a circle given its radius.

import math
def area(radius):
   return math.pi*(radius**2)
radius=5
Area=area(radius)
print("Area of the circle : ",Area)