import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcom tp the password validator!")
letter_num = int(input("How many letters should the password contain? "))
number_num = int(input("How many numbers should the password contain? "))
symbol_num = int(input("How many symbols should the password contain? "))
        
password = []
for character in range(0, letter_num):
    password += random.choice(letters)
for character in range(0, number_num):
    password += random.choice(numbers)
for character in range(0, symbol_num):
    password += random.choice(symbols)
random.shuffle(password)
password = "".join(password)

print(f"Your password is: {password}")