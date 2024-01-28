'''
F21C26
Prathamesh Kamble
P2 Calculate Square root and Cube root of given number.
'''

print("Enter a number=")
num=int(input())

print("Enter nth root to find=")
root_nth=float(input())

Root=num**(1/root_nth)
print("Your nth root of given number is=",Root)