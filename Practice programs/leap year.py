print("Welcome to Leap Year checker program!")

year = int(input("Enter the year : "))

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("It is an leap year.")
        else :
            print("It is not an leap year.")
    else :
        print("It is an leap year.")
else :
    print("It is not an leap year")