############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): # change 20 to 21 to print
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)    # change the range of numbers as(0, 5) 6 is going out of list
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:     # put <= to give output for year 1994
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")     # typcast into int for comparision
# if age > 18:
# print("You can drive at age {age}.")    # chech indent also f string to print age

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))   # == operator
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)   # not inside for loop
#   print(b_list)

# mutate([1,2,3,5,8,13])