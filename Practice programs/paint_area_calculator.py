<<<<<<< HEAD
print("Paint Area Calculator")

import math

def paint_calc (height, width, cover) :
    no_of_cans = (height * width) / cover
    print(f"You'll need {math.ceil(no_of_cans)} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
=======
print("Paint Area Calculator")

import math

def paint_calc (height, width, cover) :
    no_of_cans = (height * width) / cover
    print(f"You'll need {math.ceil(no_of_cans)} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
>>>>>>> d6923851b62279e23da6ef0dfb58ffafc1517201
paint_calc(height=test_h, width=test_w, cover=coverage)