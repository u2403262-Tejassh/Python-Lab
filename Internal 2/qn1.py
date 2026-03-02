'''
1. Create a class named Polygon with methods ‘no_of_sides’ and ‘area’. Calculate the areas
of the shapes ‘Square’, ‘Rectangle’, and ‘Triangle’ with the help of function overloading
'''

import math

class Polygon:
    def __init__(self, *args):
        self.sides = args
    def no_of_sides(self):
        self.n_sides = len(self.sides)
        return(self.n_sides)
    def area(self):
        if self.n_sides == 3:
            s = (self.sides[0]+self.sides[1]+self.sides[2])/2
            area = math.sqrt(s*(s-self.sides[0])*(s-self.sides[1])*(s-self.sides[2]))
            return(area)
        if self.n_sides == 4:
            if len(set(self.sides)) == 1:
                area = self.sides[0]*self.sides[0]
                return(area)
            else:
                for i in range(3):
                    if self.sides[i] != self.sides[i+1]:
                        area = self.sides[i]*self.sides[i+1]
                        return(area)
Square = Polygon(4,4,4,4)
print(f"Square: Number of Sides = {Square.no_of_sides()}, Area = {Square.area()}")
Rectangle = Polygon(4,2,4,2)
print(f"Rectangle: Number of Sides = {Rectangle.no_of_sides()}, Area = {Rectangle.area()}")
Triangle = Polygon(5,6,7)
print(f"Triangle: Number of Sides = {Triangle.no_of_sides()}, Area = {Triangle.area()}")
