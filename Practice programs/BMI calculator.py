weight = input("Enter your body weight in kg : ")
height = input("enter your height in m : ")

weight_integer = int(weight)
height_integer = float(height)

bmi = str(round(weight_integer / height_integer ** 2))

print("Body Mass Index (BMI) for your body weight " + weight + "kg and height " + height + "m is :" + bmi)
