num=int(input("Enter numbers : "))
x=0
while num>0:
    x=(x*10)+num%10
    num=num//10
print("Reverse of numbers is: ",x)

