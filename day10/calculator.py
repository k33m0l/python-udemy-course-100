def select_op():
    operation = input("Pick an operation (+, -, *, /): ")
    if operation != "+" and operation != "-" and operation != "*" and operation != "/":
        print("Invalid operation selected!")
        return select_op()
    return operation

def print_calculation(first_number, second_number, operation, result):
    print(f"{first_number} {operation} {second_number} = {result}")

def calculate(first_number, second_number, operation):
    result = 0
    if operation == "+":
        result = first_number + second_number
        print_calculation(first_number, second_number, operation, result)
    if operation == "-":
        result = first_number - second_number
        print_calculation(first_number, second_number, operation, result)
    if operation == "*":
        result = first_number * second_number
        print_calculation(first_number, second_number, operation, result)
    if operation == "/":
        result = first_number / second_number
        print_calculation(first_number, second_number, operation, result)
    
    user_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to stop the calculation: ")
    if user_input == "y":
        operation = select_op()
        second_number = int(input("What's the next number?: "))
        return calculate(result, second_number, operation)
    else:
        return result
    

first_number = int(input("What's the first number?: "))
operation = select_op()
second_number = int(input("What's the next number?: "))

print(f"The result is: {calculate(first_number, second_number, operation)}")