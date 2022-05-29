import random

list_moves = ("rock","paper","scissors")

computer_choice = random.choice(list_moves)

human_choice = input("Please input rock, paper or scissors: ")

if human_choice not in list_moves:
    print("Incorrect choise, my friend!")

if computer_choice == human_choice:
    print("You have a tie!")
elif computer_choice == "rock" and human_choice == "paper":
    print("You win!")
elif computer_choice == "rock" and human_choice == "scissors":
    print("You lose!")
elif computer_choice == "paper" and human_choice == "scissors":
    print("You win!")
elif computer_choice == "paper" and human_choice == "rock":
    print("You lose!")
elif computer_choice == "scissors" and human_choice == "rock":
    print("You win!")
elif computer_choice == "scissors" and human_choice == "paper":
    print("You lose!")


