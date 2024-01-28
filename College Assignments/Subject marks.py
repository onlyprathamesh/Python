'''
F21C26
Prathamesh Kamble

Program on subject marks
'''
mylist=[]

print("Enter number of subjects=")
n=int(input())

print("Enter marks of subject=") 
for x in range(n):
    mylist.append(int(input()))
print(mylist)

sum=sum(mylist)/n
print("Average of your score is=",sum)

for i in mylist:
    if i<= 40:
        print("fail")
        break
if sum>=75:
    print("First class")
elif sum>=60:
    print("Second class")
elif sum>=50:
    print("Third class")

