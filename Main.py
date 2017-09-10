first_number = ""
operation = ""
second_number = ""

def main():
    print("CMDCalc Alpha.")
    print("Type 'help' for a list of commands.")
    print("Type 'quit' to quit.")
    command = input("Enter a calculation: ")

    if command.lower() == "help":
        show_commands()
    elif command.lower() == "quit":
        exit()
    else:
        try:
            global first_number
            global operation
            global second_number
            first_number, operation, second_number = command.split()
        except ValueError:
            print("Unknown operation.")

    if operation == "+":
        print("{} + {} = {} ".format(first_number, second_number, add_numbers()))
    elif operation == "-":
        print("{} - {} = {} ".format(first_number, second_number, subtract_numbers()))
    elif operation == "*":
        print("{} * {} = {} ".format(first_number, second_number, multiply_numbers()))
    elif operation == "/":
        print("{} / {} = {:.2} ".format(first_number, second_number, divide_numbers()))
    elif operation == "%":
        print("{} % {} = {} ".format(first_number, second_number, remaining_numbers()))

def add_numbers():
    return int(first_number) + int(second_number)

def subtract_numbers():
    return int(first_number) - int(second_number)

def multiply_numbers():
    return int(first_number) * int(second_number)

def divide_numbers():
    return int(first_number) / int(second_number)

def remaining_numbers():
    return int(first_number) % int(second_number)

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

while True:
    main()
    print()