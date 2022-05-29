import random

list_moves = ["rock","paper","scissors"]

computer_choice = random.choice(list_moves)

human_choice = input("Please input rock, paper or scissors: ")

if computer_choice == human_choice:
    print("You have a tie!")
else:
    
