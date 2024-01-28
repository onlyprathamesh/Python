'''
F21C26
Prathamesh Kamble
Assignment-1 Find out NET SALARY including HRA and TA and excluding TAX
'''

from functools import total_ordering


print("Enter your Basic Pay=")
Basic_pay=int(input())

HRA=10/100*Basic_pay
print("\nTotal HRA you get=",HRA)

TA=5/100*Basic_pay
print("\nTotal TA you get=",TA)

Total=Basic_pay+HRA+TA
print("\nYour Total Salary=",Total)

Tax=2/100*Total
print("\nTotal Tax u pay=",Tax)

Net_Salary=Total-Tax
print(" \nTotal Net Salary=",Net_Salary)
