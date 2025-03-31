bidders = {}

print("Welcome to the secret auction program.")

def bid():
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid

bid()
bidding = True
while bidding:
    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "yes":
        bid()
    else:
        bidding = False

highest_name = ''
highest = 0
for name, amount in bidders.items():
    if amount >= highest:
        highest_name = name
        highest = amount
print(f"The winner is \"{highest_name}\" with the bid of ${highest}.")