import random

def visualize(list):
    return ''.join(list)

word_list = ["aardvark", "baboon", "camel"]
selected = random.choice(word_list)
selected_length = len(selected)
health = 3

visual_word = []
for id in range(0, selected_length):
    visual_word += "_"

guessed = False
hit = False
while not guessed and health > 0:
    print(f"You have to guess: {visualize(visual_word)} and you have {health} health left.")
    user_guess = str(input("Please guess a word:")).lower()
    
    for id in range(0, selected_length):
        if selected[id] == user_guess:
            visual_word[id] = user_guess
            hit = True

    if not hit:
        health -= 1
        if health <= 0:
            print(f"Game Over! The word was \"{selected}\"...")
    hit = False

    if selected == visualize(visual_word):
        guessed = True
        print(f"Congratulations! You have guessed the \"{visualize(visual_word)}\" word!")