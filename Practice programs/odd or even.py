print("Even or Odd number predictor!!")

number = int(input("Enter a number : "))

module = number % 2

if module == 0:
    print(f"{number} number is an even number.")
else:
    print(f"{number} number is an odd number.")

