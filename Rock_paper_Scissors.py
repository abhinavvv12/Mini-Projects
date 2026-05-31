# Work Flow
# 1. Get the user's choice (rock, paper, or scissors)
# 2. Generate a random choice for the computer
# 3. Compare the user's choice with the computer's choice to determine the winner
import random
# Get the user's choice0
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
# Generate a random choice for the computer
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
# Compare the user's choice with the computer's choice to determine the winner
if user_choice == computer_choice:
    print(f"Both chose {user_choice}. It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
    print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
else:
    print(f"You chose {user_choice} and the computer chose {computer_choice}. You lose!")

