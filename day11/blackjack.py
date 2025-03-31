import random

cards = {
    "2": [2],
    "3": [3],
    "4": [4],
    "5": [5],
    "6": [6],
    "7": [7],
    "8": [8],
    "9": [9],
    "J": [10],
    "Q": [10],
    "K": [10],
    "10": [10],
    "A": [1, 11],
}

def select_random_card():
    return random.choice(list(cards.keys()))

def calculate_points(cards_in_hand):
    points = 0
    for card in cards_in_hand:
        points += cards[card][0]
    return points

user_cards = []
user_cards += select_random_card()
user_cards += select_random_card()
print(f"Your cards: [{', '.join(user_cards)}]")

computer_cards = []
computer_cards += select_random_card()
print(f"Computer's first card: {computer_cards[0]}")

game_over = False
while not game_over:
    user_input = input("Type 'y' to get another card, type anything else to pass: ")
    if user_input == "y":
        user_cards += select_random_card()
        print(f"Your cards: [{', '.join(user_cards)}]")
        computer_cards += select_random_card()
        print(f"Computer cards: [{', '.join(computer_cards)}]")
    else:
        game_over = True
        player_points = calculate_points(user_cards)
        computer_points = calculate_points(computer_cards)
        if player_points > 21 and computer_points > 21:
            print("Unfortunately, you both went over and ended with a draw")
        elif player_points > 21:
            print("Unfortunately, you went over and lost")
        elif computer_points > 21:
            print("Computer went over and lost, Congratulations!")
        elif player_points == computer_points:
            print("Draw")
        elif player_points > computer_points:
            print("Congratulations! You won!")
        else:
            print("Unfortunately, the computer won this time.")
