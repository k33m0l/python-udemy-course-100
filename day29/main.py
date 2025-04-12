from tkinter import *
from tkinter import messagebox
from password import gen_random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    password = gen_random()
    password_input.insert(0, f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("saved.txt", "a") as file:
        website = website_input.get()
        website_input.delete(0, END)
        user_id = user_id_input.get()
        password = password_input.get()
        password_input.delete(0, END)
        file.write(f"{website} | {user_id} | {password}\n")

        messagebox.showinfo(title="Success", message=f"{password} was saved successfully")

# ---------------------------- SEARCH --------------------------------#
def search_pass():
    try:
        with open("saved.txt") as file:
            website = website_input.get()
            data = {parts[0]: parts[1:] for line in file.readlines() if (parts := line.split(" | "))}
            user_id = data[website][0]
            password = data[website][1]
            messagebox.showinfo(title="Found", message=f"Your password was found!\nEmail:{user_id}\nPassword:{password}")
    except FileNotFoundError:
        messagebox.showerror(title="Not Found", message=f"Password for {website} not found!")
    except KeyError:
        messagebox.showerror(title="Not Found", message=f"Password for {website} not found!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

background_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=background_image)

website_label = Label(text="Website:")
user_id_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_input = Entry(width=40)
user_id_input = Entry(width=40)
password_input = Entry(width=21)

gen_pass_button = Button(text="Generate Password", command=gen_pass)
add_button = Button(text="Add", command=save, width=36)
search_button = Button(text="Search", command=search_pass)

canvas.grid(row=0, column=1, sticky=EW)

website_label.grid(row=1, column=0, sticky=EW)
user_id_label.grid(row=2, column=0, sticky=EW)
password_label.grid(row=3, column=0, sticky=EW)

website_input.grid(row=1, column=1, sticky=EW)
user_id_input.grid(row=2, column=1, columnspan=2, sticky=EW)
password_input.grid(row=3, column=1, sticky=EW)

gen_pass_button.grid(row=3, column=2, sticky=EW)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)
search_button.grid(row=1, column=2, sticky=EW)

website_input.focus()
user_id_input.insert(0, "example@example.com")

window.mainloop()