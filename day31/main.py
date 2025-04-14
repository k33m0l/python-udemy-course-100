BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
FRENCH_LANGUAGE_KEY = "French"
ENGLISH_LANGUAGE_KEY = "English"

from tkinter import *
import pandas
import random

try:
    dictionary = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    print("Saved file not found, falling back to default list")
    dictionary = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
current_card = {}

def flip_card():
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(language_text, text=ENGLISH_LANGUAGE_KEY)
    canvas.itemconfig(word_text, text=current_card[ENGLISH_LANGUAGE_KEY])

def missed_word():
    next_word()

def save_dict():
    words_to_learn = pandas.DataFrame.from_dict(dictionary)
    words_to_learn.to_csv("data/words_to_learn.csv")

def knew_word():
    try:
        dictionary.remove(current_card)
        save_dict()
    except ValueError:
        window.destroy()
    next_word()

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_bg, image=card_front)
    current_card = random.choice(dictionary)
    canvas.itemconfig(language_text, text=FRENCH_LANGUAGE_KEY)
    canvas.itemconfig(word_text, text=current_card[FRENCH_LANGUAGE_KEY])
    flip_timer = window.after(3000, flip_card)

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

language_text = canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)

accept_image = PhotoImage(file="images/right.png")
accept_button = Button(image=accept_image, highlightthickness=0, command=knew_word)
accept_button.grid(row=1, column=1)
deny_image = PhotoImage(file="images/wrong.png")
deny_button = Button(image=deny_image, highlightthickness=0, command=missed_word)
deny_button.grid(row=1, column=0)

# Init a first card to show
flip_timer = window.after(3000, flip_card)
next_word()

window.mainloop()