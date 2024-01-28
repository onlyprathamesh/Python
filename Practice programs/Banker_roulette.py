from random import random


print("Python's Banker Roulette.")

import random

name_of_players = input("Enter name of peoples seperated by comma. ")

names = name_of_players.split(",")

length = len(names)

a = random.randint(0, length-1)

b = names[a]

print(f"{b} is going to pay the bill today.")