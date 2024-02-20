#1Write a Python program to convert degree to radian.
import math
def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees = float(input())
radians = degrees_to_radians(degrees)
print("Degrees:", degrees)
print("Radians:", radians)

#2Write a Python program to calculate the area of a trapezoid.
def s_of_trap(a, b, h):
    s = (a+b)*h/2
    return s
h = int(input())
a = int(input())
b = int(input())
area = s_of_trap(a, b, h)
print(area)

#3Write a Python program to calculate the area of regular polygon.
import math
def s_of_polugon(sides, lenght):
    a = lenght/(2 * math.tan(math.pi/sides))
    s = (a * (sides*lenght))/2
    return s
sides = int(input())
lenght = int(input())
area = s_of_polugon(sides, lenght)
print(int(area))


#4Write a Python program to calculate the area of a parallelogram.
def s_of_parallelogram(a, h):
    s = a * h
    return s
a = int(input())
h = int(input())
area = s_of_parallelogram(a, h)
print(int(area))