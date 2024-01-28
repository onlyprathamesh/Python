print("Rock Paper Scissor Game.")

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = int(input("What would u like to choose? : 1 for Rock, 2 for Paper, 3 for Scissor :\n"))
if choice == 1 :
    print(f"Your choice : Rock {rock}")
elif choice == 2 :
    print(f"Your choice : Paper {paper}")
elif choice == 3 :
    print(f"Your choice : Scissiors {scissors}")
else :
    print("You have selected invalid option. Please play again!")

    
computer_choice = random.randint(1, 3)
if computer_choice == 1 :
    print(f"Computer's choice : Rock {rock}")
elif computer_choice == 2 :
    print(f"Computer's choice : Paper {paper}")
else :
    print(f"Computer's choice : Scissor {scissors}")


if choice == 1 :
    if computer_choice == 2:
        print("Results : YOU LOOSE.")
    elif computer_choice == 3 :
        print("Results : YOU WON.")
    else :
        print("Results : Its TIE.")
elif choice == 2 :
    if computer_choice == 1 :
        print("Results : YOU WON.")
    elif computer_choice == 3:
        print("Results : YOU LOOSE.")
    else :
        print("Results : Its TIE.")
elif choice == 3 :
    if computer_choice == 1 :
        print("Results : YOU LOOSE.")
    elif computer_choice == 2 :
        print("Results : YOU Won.")
    else :
        print("Results : Its TIE.")

