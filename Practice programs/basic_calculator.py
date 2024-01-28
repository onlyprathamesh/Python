logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a, b) :
    c = a + b
    return c

def sub(a, b) :
    c = a - b
    return c

def mul(a, b) :
    c = a * b
    return c

def div(a, b) :
    c = a / b
    return c

operations = {"+" : add,
            "-" : sub,
            "*" : mul,
            "/" : div}
print(logo)
def calculator() :
    num1 = int(input("What's the first number? : "))

    run_again = True
    while run_again :
        operation_symbol = input("Pick an operation(+, -, *, /) : ")
        num2 = int(input("What's the next number? : "))

        operation = operations[operation_symbol]
        result = operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        further_choice = input("do you want to continue further with the sum or new calculation? (y/n/new): ")
        if (further_choice == "n") : 
            run_again = False
        elif (further_choice == "y"):
            num1 = result
        elif (further_choice == "new") :
            calculator()
        else :
            break
            
calculator()

