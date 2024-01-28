'''
# PRINT FUNCTION
name="Tony Stark"
age=51
is_genius = True
print(name,age)
print(is_genius)

# INPUT FUNCTION , PRINTING INPUT FUNCTION
name = input("Your name=")
superhero_name = input("Enter your favourite SuperHero=")
print(" Your Name is = " + name)
print(" Your SuperHero Name is = " + superhero_name)

# TYPE CONVERSION ( TYPECAST) [float(),bool(),str(),int()]
birth_year = input(" Enter Your Birth Year = ")
age = 2021 - int(birth_year)
print(" Your Current Age = " + str(age))

# STRINGS 
name = "Tony Stark"
print(name.upper())
print(name.lower())
print(name.find(" Stark"))
print(name.replace(" Tony "," Iron "))
print('S' in name)

# ARITHIMATIC OPERATORS ( + , - , * , / , % , ** )
num1 = int(input( " Enter first number : "))
num2 = int( input(" Enter Second number : "))
print( " Addition : " ,num1 + num2 )
print( " Substraction : " ,num1 - num2 )
print( " Multiplication : " ,num1 * num2 )
print( " Division : " ,num1 / num2 )
print( " Remainder : " ,num1 % num2 )
print( "Power : ",num1 ** num2 )

# SHORTCUTS 
i = 5
i = i + 2
# instead of this we can use shortcuts
i += 2
i -= 2
i *= 2
print(i)

# COMPARISION OPERATOR
is_greater = x > y
print(3 > 2)
print(3 >= 2)

is_less = x < y
print(3 < 2)
print(3 <= 2)

is_equal = x == y
print(3 == 2)
print(3 == 3)
is_notequal = x != y
print(3 != 2)

# LOGICAL OPERATORS (OR=ATLEST ONE IS TRUE:TRUE, AND=IF BOTH ARE TRUE:TRUE, NOT=REVERSE THE VALUE)
print(3>2 or 4>5)
print(4<2 and 4<6)
print(not 3>1)

# IF-ELSE
age = 13

if age >= 18:
    print("you are an adult")
    print("you can vote")
elif age < 3:
    print("you are a child")
else:
    print("you are in school")
print("thank you")


#BASIC TRIAL PROGRAM FOR CALCULATOR
num1 = int(input( "Enter first number :" ))
operator = input("Enter Operator to peform calculation (+,-,*,/,%,**):")
num2 = int(input("Enter seccond number :"))
if operator == "+":
    print("Addition of two numbers is :" , (num1+num2))
if operator == "-":
    print("Substraction of two numbers is :" , (num1-num2))
if operator == "*":
    print("Multiplication of two numbers is :" , (num1*num2))
if operator == "/":
    print("Division of two numbers is :" , (num1/num2))
if operator == "%":
    print("Remainder of two numbers is :" , (num1%num2))
if operator == "**":
    print("Power of two numbers is :" , (num1**num2))

# RANGE FUNCTION
num=range(5)
print(num)

# LOOPS
# WHILE LOOP
i = 0
while i < 5:
    print(i)
    i +=1

i = 5
while i > 0:
    print(i* "*")
    i -= 1

# FOR LOOP
for i in range(5):
    print(i)

for i in range(5):
    print(i* "*")

# LIST
friends = ["amar", "akbar", "anthony"]
print(friends[0])
print(friends[1])
print(friends[-1])
print(friends[-2])

friends[0] = "aman"
print(friends)

print(friends[0:2]) #returns a new list

for x in friends:
    print(x)

marks = ["english", 95, "chemistry", 98]
marks.append("physics")
marks.append(97)
print(marks)

marks.insert(0, "math")
marks.insert(1, 99)
print(marks)

print("math" in marks)

print(len(marks)/2)
marks.clear()
print(marks)

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 2

# BREAK AND CONTINUE
students = ["prathamesh", "prakash", "kamble", "harsh", "pratiksha"]
for student in students:
    if student == "kamble":
        break
    print(student)

for absent in students:
    if absent == "harsh":
        continue
    print(absent)

# TUPLES (tuples cant be edited as lists)
marks = (91, 93, 96, 96, 96, 96)
print(marks.count(96))
print(marks.index(96))

# SET
marks = {91, 96, 76, 99, 99, 99}
print(marks)

print(marks[0]) # this will give error because we cannot access specific index in sets

for score in marks:
    print(score)

# DICTIONARY
marks = {"Chemistry" : 91, "Maths" : 94, "English" : 86}
print(marks)
print(marks["Maths"])

marks["Mechanics"] = 92
print(marks)

marks["Chemistry"] = 93
print(marks)

# FUNCTIONS
# 1.Inbuilt functions int(), str(), float(), range() etc...,
# 2.Module functions : file that contains some functions or variables which can be imported.eg. math(), random(), string()
import math
print(dir(math))

import random
print(dir(random))

import string
print(dir(string))

from math import sqrt
print(sqrt(16))
# 3.User defined functions : functions which user can define.
def product(a,b):
    print(a*b)
product(5,6)
''' 