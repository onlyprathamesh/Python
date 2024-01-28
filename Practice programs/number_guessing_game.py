logo ="""    ______                                  _   __              ____  _____                       __                       
 .' ___  |                                / |_[  |            |_   \|_   _|                     [  |                      
/ .'   \_| __   _   .---.  .--.   .--.   `| |-'| |--.  .---.    |   \ | |  __   _   _ .--..--.   | |.--.   .---.  _ .--.  
| |   ____[  | | | / /__\\( (`\] ( (`\]   | |  | .-. |/ /__\\   | |\ \| | [  | | | [ `.-. .-. |  | '/'`\ \/ /__\\[ `/'`\] 
\ `.___]  || \_/ |,| \__., `'.'.  `'.'.   | |, | | | || \__.,  _| |_\   |_ | \_/ |, | | | | | |  |  \__/ || \__., | |     
 `._____.' '.__.'_/ '.__.'[\__) )[\__) )  \__/[___]|__]'.__.' |_____|\____|'.__.'_/[___||__||__][__;.__.'  '.__.'[___]    
                                                                                                                          """


import random
import os

def difficuilty_level() :
    difficuilty = input("Choose a difficulty. Type 'easy' or 'hard' : ")

    if difficuilty == 'easy' :
        return EASY_ATTEMPTS
    elif difficuilty == 'hard' :
        return HARD_ATTEMPTS

def check_answer(guess, number, attempts) :
    if guess > number :
        print("Too High!")
    elif guess < number :
        print("Too Low!")
    else :
        print(f"You got it! The answer was {number}.")
        return 0
    if attempts == 1 :
        print ("You've run out of guesses, you lose.")
        print(f"The Number was {number}")
        return 0
    print(f"You have {attempts-1} attempts remaining to guess the number.")
    print("Guess again.")


EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

while input("Do you want to play the Number Guessing Game? (y/n) : ") == 'y' :
    number = random.randint(1, 100)
    os.system('cls||clear')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 to 100.")

    attempts = difficuilty_level()

    print(f"You have {attempts} attempts remaining to guess the number.")
    next_guess = True
    while next_guess == True :
        guess = int(input("Make a guess : "))

        if check_answer(guess, number, attempts) == 0 :
            next_guess = False
        attempts -= 1

