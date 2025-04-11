from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

background_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=background_image)

website_label = Label(text="Website:", anchor=E)
user_id_label = Label(text="Email/Username:", anchor=E)
password_label = Label(text="Password:", anchor=E)

website_input = Entry(width=35)
user_id_input = Entry(width=35)
password_input = Entry(width=21)

gen_pass_button = Button(text="Generate Password", command=gen_pass)
add_button = Button(text="Add", command=save, width=36)

canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
user_id_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_input.grid(row=1, column=1, columnspan=2)
user_id_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)

gen_pass_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()