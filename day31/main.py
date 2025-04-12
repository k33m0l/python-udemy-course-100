BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

from tkinter import *

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT)
canvas.create_text(400, 263, text="Word", font=WORD_FONT)

accept_image = PhotoImage(file="images/right.png")
accept_button = Button(image=accept_image, highlightthickness=0)
accept_button.grid(row=1, column=0)
deny_image = PhotoImage(file="images/wrong.png")
deny_button = Button(image=deny_image, highlightthickness=0)
deny_button.grid(row=1, column=1)

window.mainloop()