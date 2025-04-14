BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
FRENCH_LANGUAGE_KEY = "French"
ENGLISH_LANGUAGE_KEY = "English"

from tkinter import *
import pandas
import random

dictionary = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

def next_word():
    current = random.choice(dictionary)
    canvas.itemconfig(language_text, text=FRENCH_LANGUAGE_KEY)
    canvas.itemconfig(word_text, text=current[FRENCH_LANGUAGE_KEY])

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

language_text = canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)

accept_image = PhotoImage(file="images/right.png")
accept_button = Button(image=accept_image, highlightthickness=0, command=next_word)
accept_button.grid(row=1, column=1)
deny_image = PhotoImage(file="images/wrong.png")
deny_button = Button(image=deny_image, highlightthickness=0)
deny_button.grid(row=1, column=0)

window.mainloop()