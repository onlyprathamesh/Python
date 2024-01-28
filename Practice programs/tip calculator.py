print("Welcome to Python-Developed tip calculator :")

total_bill = float(input ("Enter total bill : "))
tip = int(input("Enter how many % tip do u want to give : "))
total_peoples = int(input("Enter number of peoples : "))

tip_offered = total_bill/100 * tip
bill_with_tip = total_bill + tip_offered
final_bill = round(bill_with_tip / total_peoples, 2)

print(f"The final amount of bill everyone should pay is : {final_bill} $")

