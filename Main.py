# CMDCalc Version 1.
# Created by, Trevor Hodsdon.

first_number = ""
operation = ""
second_number = ""

# Main method for the Program.
def main():
    # Print info.
    print("CMDCalc Version 1.")
    print("Type 'help' for a list of commands.")
    print("Type 'quit' to quit.")

    # Get command from the user.
    command = input("Enter a calculation: ")

    # Check what the command is.
    if command.lower() == "help":
        show_commands()
    elif command.lower() == "quit":
        exit()
    else:
        # Attempt to split the inputted calculation into 3 variables.
        try:
            global first_number
            global operation
            global second_number
            first_number, operation, second_number = command.split()
        except ValueError:
            print("Unknown operation.")
    # Check what operation was entered and output the correct calculation.
    if operation == "+":
        print("{} + {} = {:.2} ".format(first_number, second_number, add_numbers()))
    elif operation == "-":
        print("{} - {} = {:.2} ".format(first_number, second_number, subtract_numbers()))
    elif operation == "*":
        print("{} * {} = {:.2} ".format(first_number, second_number, multiply_numbers()))
    elif operation == "/":
        print("{} / {} = {:.2} ".format(first_number, second_number, divide_numbers()))
    elif operation == "%":
        print("{} % {} = {:.2} ".format(first_number, second_number, remaining_numbers()))

# Adds the numbers together.
def add_numbers():
    return float(first_number) + float(second_number)

# Subtract the numbers.
def subtract_numbers():
    return float(first_number) - float(second_number)

# Multiply the numbers.
def multiply_numbers():
    return float(first_number) * float(second_number)

# Devide the numbers.
def divide_numbers():
    # Try to divide the numbers and catch any 'divide by zero' exceptions.
    try:
        answer = float(first_number) / float(second_number)
        return answer
    except ZeroDivisionError:
        print("Can't divide by zero.")
        return 0.0

# Get the remainder of the numbers.
def remaining_numbers():
    return float(first_number) % float(second_number)

# Prints out information and available commands to the console.
def show_commands():
    print()
    print("Format your questions in the following way")
    print("[FirstNumber] [Operation] [SecondNumber]")
    print("Example: 5 + 3")
    print()
    print("You can do the following operations:")
    print("Add: +")
    print("Subtract: -")
    print("Multiply: *")
    print("Divide: /")
    print("Modulus: %")

# Loop the main method forever.
while True:
    main()
    print()
