def print_initial_msg():
    print("💻💻💻💻💻 Welcome to Calculator2030! 💻💻💻💻💻")


def show_operators():
    print("+")
    print("-")
    print("*")
    print("/")


def summation(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def pick_operation():
    valid_operations = ["+", "-", "/", "*"]
    show_operators()
    while True:
        operation = input("Pick an operation: ")
        if operation in valid_operations:
            return operation
        else:
            print("Please, enter a valid operation")


def calculate_result(num1, num2, operator):
    if operator == "+":
        return summation(num1, num2)
    elif operator == "-":
        return subtraction(num1, num2)
    elif operator == "*":
        return multiplication(num1, num2)
    elif operator == "/":
        return division(num1, num2)


def print_result(result, num1, num2, operator):
    print(f"The result of {num1} {operator} {num2} is {result}")


# global
keep_calculating = True


def main():
    global keep_calculating
    first_number = float(input("What is the first number? "))
    while keep_calculating:
        operation = pick_operation()
        second_number = float(input("What is the second number? "))
        result = calculate_result(first_number, second_number, operation)
        print_result(result, first_number, second_number, operation)
        user_final_choice = input(
            f"Type 'yes' to keep calculating with {result}, type 'no' to start a new calculation and type 'exit' to exit the program: ")
        print(user_final_choice)
        # processing final choice
        if user_final_choice.lower() == "exit":
            print("\n\nThank you for using Calculator 2030!!")
            keep_calculating = False
        elif user_final_choice.lower() == "no":
            main()
        elif user_final_choice.lower() == "yes":
            first_number = result
        else:
            print("Please, entera valid choice")
            main()


main()
