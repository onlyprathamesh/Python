# get gamedata into the main file

from gamedata import data

# get art into the main file

from art import logo, vs

# get function to clear terminal
import os

# get the length of data & select a random number between the lenght

import random

def get_comparision() :
    return random.randint(0, len(data)-1)

# function to check for highes followers 

def highest_follower(comparision_a, comparision_b) :
    '''Will take input comparision_a & comparision_b and return who have more followers'''
    follower_a = data[comparision_a]['follower_count']
    follower_b = data[comparision_b]['follower_count']

    if follower_a > follower_b :
        return 'a'

    return 'b'

# function to play again

while input("Do you want to play the Higher Lower Game? 'yes' or 'no': ").lower() == 'yes' :
    os.system('cls||clear')

    print(logo)

    comparision_a = get_comparision()
    comparision_b = get_comparision()
    if comparision_a == comparision_b :
        comparision_b = get_comparision()

    # Make a loop to run again

    output = True
    score = 0
    while output :

        # Display the values of data A & B such as name, description, country

        print(f"Compare A: {data[comparision_a]['name']}, a {data[comparision_a]['description']}, from {data[comparision_a]['country']}")

        print(vs)

        print(f"Against B: {data[comparision_b]['name']}, a {data[comparision_b]['description']}, from {data[comparision_b]['country']}")

        # Ask the question. eg : who has more followers?

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        os.system('cls||clear')

        # final checking and printing

        answer = highest_follower(comparision_a, comparision_b)
        if answer == choice :
            score += 1
            print(f"You are right! Current score: {score}")
            if choice == 'b' :
                comparision_a = comparision_b
            comparision_b = get_comparision()
        else :
            print(f"Sorry, that's wrong. Final score: {score}")
            output = False

