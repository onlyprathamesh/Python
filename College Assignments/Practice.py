print("Subject 1=")
s1=int(input())
print("Subject 2=")
s2=int(input())
print("Subject 3=")
s3=int(input())
print("Subject 4=")
s4=int(input())
print("Subject 5=")
s5=int(input())
avg=(s1+s2+s3+s4+s5)/5
print("Average of subjects=",avg)

if s1>=40 and s2>=40 and s3>=40 and s4>=40 and s5>=40:
    print("pass")
    if avg>=75:
        print("First class")
    elif avg>=60:
        print("second class")
    elif avg>=50:
        print("third class")
else:
    print("fail")
