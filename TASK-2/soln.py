#!/bin/python3

import math
import os
import random
import re
import sys



class Rectangle:
    def __init__(self,length, width):
        self.length=length
        self.width=width
        #print(self.length)
    def area(self):
        a=self.length*self.width
        return a
class Circle:
    def __init__(self,radius):
        self.radius=radius
        #print(self.radius)
    def area(self):
        #print(self.radius)
        a=self.radius*self.radius*math.pi
        return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
