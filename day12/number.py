import random

number = random.randint(1, 100)
print(f"DEBUG! Number is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def game_loop(lifes):
    winner = False
    while lifes > 0 and not winner:
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high!")
            lifes -= 1
            print(f"Your health is {lifes}!")
        elif guess < number:
            print("Too low!")
            lifes -= 1
            print(f"Your health is {lifes}!")
        else:
            winner = True
            print("Congratulations!")
    if lifes == 0:
        print("Unfortunately you lost!")


if difficulty == "easy":
    game_loop(10)
elif difficulty == "hard":
    game_loop(5)
else:
    print("An invalid difficulty was selected")