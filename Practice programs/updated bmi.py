print("Welcome to BMI calculator!")

weight = int(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f"Your BMI score is {bmi}. You are Underweight.")
elif 25 > bmi > 18.5:
    print(f"Your BMI score is {bmi}. You have Normal weight.")
elif 25 < bmi < 30 :
    print(f"Your BMI score is {bmi}. You are Slightly Overweight.")
elif 30 > bmi < 35:
    print(f"Your BMI score is {bmi}. You are Obese(OVERWEIGHT).")
else:
    print(f"Your BMI score is {bmi}. You are Clinically Obese(Go to the fucking doctor).")

