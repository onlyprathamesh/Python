'''Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1'''



print("Welcome to Pizza Order program !!")

size = input(" What size pizza do you want ? S, M or L\n")
add_pepperoni = input("Do you want to add pepperoni? Y or N\n")
extra_cheese = input ("Do you want extra cheese on your pizza? Y or N\n")

bill = 0
if size == "S" :
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M" :
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L" :
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y" :
    bill += 1

print("Your total bill is : ",bill)