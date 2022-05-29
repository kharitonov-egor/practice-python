import random

list_moves = ("r","p","s")

computer_choice = random.choice(list_moves)

human_choice = input("Please input r, p or s: ")

if human_choice not in list_moves:
    print("Incorrect choise, my friend!")

print(f"Thanks for picking {human_choice}!")
print(f"Computer has picked {computer_choice}!")

if computer_choice == human_choice:
    print("You have a tie!")
elif computer_choice == "r" and human_choice == "p":
    print("You win!")
elif computer_choice == "r" and human_choice == "s":
    print("You lose!")
elif computer_choice == "p" and human_choice == "s":
    print("You win!")
elif computer_choice == "p" and human_choice == "r":
    print("You lose!")
elif computer_choice == "s" and human_choice == "r":
    print("You win!")
elif computer_choice == "s" and human_choice == "p":
    print("You lose!")


