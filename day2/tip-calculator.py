print("Welcome to the Tip Calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = total_bill * tip_percentage / 100
total = total_bill + tip
split = total / people
split = round(split, 2)
print(f"Each person should pay: ${split}")