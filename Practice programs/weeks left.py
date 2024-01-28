age = int(input("Enter your current age :"))

years_left_to_live = 90 - age

months_left = years_left_to_live * 12
weeks_left = years_left_to_live * 52
days_left = years_left_to_live * 365

print(f"You have left {months_left} months, {weeks_left} weeks and {days_left} days left to live")