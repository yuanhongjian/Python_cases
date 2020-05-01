
import random

# Preparation
punches = ["stone", "paper", "scissor"]
computer_choice = random.choice(punches)
user_choice = input("Please choose your punch: ")
while user_choice not in punches:
    print("Error, please choose again")
    user_choice = input()

# Compete
def print_result(user_choice):
    if computer_choice == user_choice:
        print("draw")
    else:
#        if (computer_choice == "paper" and user_choice == "stone") or (computer_choice == "stone" and
#       user_choice == "scissor") or (computer_choice == "scissor" and user_choice == "paper"):
        if user_choice == punches[punches.index(computer_choice) - 1]:
            print("computer wins!")
        else:
            print("user wins!")

print_result(user_choice)


