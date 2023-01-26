"""
This program computes the various parameters; moment of inertia and area; connected with an annular section.
"""

import math

cont=True
while cont:
    d1=float(input("Inside Diameter: "))
    d2=float(input("Outside Diameter: "))
    i = round(math.pi*(d2**4 - d1**4)/64,3)
    j = round(i**2,3)
    a = round(math.pi*(d2**2 - d1**2)/16,3)
    print("Moment of inertia = "+str(i))
    print("Polar moment of inertia = "+str(j))
    print("Area of section = "+str(a))
    z=input("Type 1 to continue: ")
    cont = z=="1"
