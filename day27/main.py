from tkinter import *

def convert_to_km(miles):
    return round(miles * 1.609, 2)

def calculate():
    miles = int(mile_input.get())
    kilometers = convert_to_km(miles)
    result_text.config(text=str(kilometers))

window = Tk()
window.title("Converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=10)
mile_input.focus()
miles_text = Label(text="Miles")
equal_text = Label(text="is equal to")
result_text = Label(text="0")
km_text = Label(text="Km")
calculate_button = Button(text="Calculate", command=calculate)

mile_input.grid(row=0, column=1)
miles_text.grid(row=0, column=2)
equal_text.grid(row=1, column=0)
result_text.grid(row=1, column=1)
km_text.grid(row=1, column=2)
calculate_button.grid(row=2, column=1)

window.mainloop()