# Espresso      - 50ml Water, 18g Coffee                    - $1.50
# Latte         - 200ml Water, 24g Coffee, 150ml Milk       - $2.50
# Cappuccino    - 250ml Water, 24g Coffee, 100ml Milk       - $3.00
drinks = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "price": 150
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 250
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 300
    }
}

# Resources: 300ml Water, 200ml Milk, 100g Coffee, 0 money
water = 300
milk = 200
coffee = 100
money = 400
# Coins: Penny - 1, Nickel - 5, Dime - 10, Quarter - 25

# Requirements: Report on resouces (include money)

def format_number(number):
    return f"{number / 100:.2f}"

def validate_drink(drink_type):
    drink_resources = drinks[drink_type]
    return water >= drink_resources["water"] and milk >= drink_resources["milk"] and coffee >= drink_resources["coffee"]

def validate_payment(total, drink_type, remainder):
    drink_resources = drinks[drink_type]
    return total >= drink_resources["price"] and money >= remainder

def take_payment():
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    return quarter * 25 + dime * 10 + nickel * 5 + penny

def calc_remainder(total, drink_type):
    drink_resources = drinks[drink_type]
    return total - drink_resources["price"]

def make_drink(drink_type):
    global water
    global milk
    global coffee
    global money
    
    drink_resources = drinks[drink_type]
    water -= drink_resources["water"]
    milk -= drink_resources["milk"]
    coffee -= drink_resources["coffee"]
    money += drink_resources["price"]

running = True
while running:
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if command == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${format_number(money)}")
    elif command == "quit" or command == "exit":
        running = False
    elif command == "espresso" or command == "latte" or command == "cappuccino":
        if validate_drink(command):
            total = take_payment()
            remainder = calc_remainder(total, command)
            if validate_payment(total, command, remainder):
                make_drink(command)
                print(f"Here is your ${format_number(remainder)} in change.")
                print(f"Here is your {command}, enjoy!")
            else:
                print("Not enough payment or machine can't return enough, please add the correct amount!")
        else:
            print("Not enough resources!")
    else:
        print("Invalid command")