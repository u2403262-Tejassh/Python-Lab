'''
Write a program to take inputs for the coefficients a, b, and c of a quadratic equation
ax^2 + bx + c = 0. Calculate and display the roots of the equation (real or complex).
'''
import math
a = int(input("Eqn: ax^2 + bx + c\nEnter value of coefficient a: "))
b = int(input("Enter value of coefficient b: "))
c = int(input("Enter value of coefficient c: "))
D = b*b-4*a*c
if D>0:
    root1 = (-b+math.sqrt(D))/(2*a)
    root2 = (-b-math.sqrt(D))/(2*a)
    print("The real roots are",root1,"and",root2)
elif D==0:
    root = -b/(2*a)
    print("The root is",root)
else:
    root1 = complex(imag =(-b+math.sqrt(-D))/(2*a))
    root2 = complex(imag =(-b-math.sqrt(-D))/(2*a))
    print("The imaginary roots are",root1,"and",root2)
