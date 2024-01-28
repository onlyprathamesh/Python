MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Make a function to Take input of coines (quarters, dimes, nickles, pennies)
# Calculate total money recieved, deduce cost of selected item and return change money.
def money_work(price) :
    print("Please insert coins.")
    quarters = 0.25 * float(input("how manu quarters?: "))
    dimes = 0.10 * float(input("how manu dimes?: "))
    nickles = 0.05 * float(input("how manu nickles?: "))
    pennies = 0.01 * float(input("how manu penniess?: "))

    total = round(quarters + dimes + nickles + pennies, 2)
    change = round(total - price, 2)
    if total < price :
        return "Sorry that's not enough money. Money refunded."
    else :
        return f"Here is ${change} in change."



money = 0

# Take input from user 
run_again = True
while run_again : 
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # if choice = report show the remaining resoruces

    if choice == 'report' :
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${money}")
        

    # for different choices
    elif choice == 'espresso' :
        if (resources["water"] < MENU["espresso"]["ingredients"]["water"]) :
            print("Sorry there is not enough water.")
        elif(resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]) :
            print("Sorry there is not enough coffee.")
        else :
            price = MENU['espresso']['cost']
            print(money_work(price))
            print("Here is your espresso ☕️. Enjoy!")
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            money += price

    elif choice == 'latte' :
        if (resources["water"] < MENU["latte"]["ingredients"]["water"]) :
            print("Sorry there is not enough water.")
        elif(resources["milk"] < MENU["latte"]["ingredients"]["milk"]) :
            print("Sorry there is not enough milk.")
        elif(resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]):
            print("Sorry there is not enough coffee.")
        else :
            price = MENU["latte"]["cost"]
            print(money_work(price))
            print("Here is your latte ☕️. Enjoy!")
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            money += price


    elif choice == 'cappuccino' :
        if (resources["water"] < MENU["cappuccino"]["ingredients"]["water"]) :
            print("Sorry there is not enough water.")
        elif(resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]) :
            print("Sorry there is not enough milk.")
        elif(resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]):
            print("Sorry there is not enough coffee.")
        else :
            price = MENU['cappuccino']['cost']
            print(money_work(price))
            print("Here is your cappuccino ☕️. Enjoy!")
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            money += price
    else :
        run_again = False

# Final output e.g enjoy coffee



