import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\nPlayer choice: "))
computer_choice = random.randint(0, 2)

print(f"Computer chose: {computer_choice}")

def player_win_scenarios():
    return (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1)

def computer_win_scenarios():
    return (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0)

if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice < 0 or player_choice > 2:
    print("You typed an invalid number, you lose!")
elif player_win_scenarios():
    print("You win!")
elif computer_win_scenarios():
    print("You lose!")
else:
    print("It's a draw!")