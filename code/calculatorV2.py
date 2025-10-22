# V2 bring new and improved functionality. Stay tuned for more updates!

#Imports
import os
import operator
import time
import typing

#Function to check input
def number_input_cleanup(*args: str) -> typing.Optional[tuple[float, ...]]:
    """
    Functions is used to turn the input strings into floats ready for calculations.
    :param args: inputs of user, strings
    :return: a tuple of the numbers requested
    """
    try:
        return tuple(float(arg) for arg in args)
    except ValueError:
        return None

#Clear function to clear cmd
def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

#Dict of all supported operators
operators: dict[str, typing.Callable] = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '**': operator.pow,
    '%': operator.mod,
}

#Function to get user input
def get_user_input(prompt: str) -> str:
    return input(prompt).strip().lower()

#Main function
def main() -> None:
    #Main Loop
    while True:

        number1: str = get_user_input("Enter first number: ")
        op: str = get_user_input("Enter operator (+,-,/,//,%,*,**): ")
        number2: str = get_user_input("Enter second number: ")

        function = operators.get(op)
        if not function:
            print("Invalid operator")
            time.sleep(1)
            clear()
            continue
        checked_numbers: tuple[float, ...] = number_input_cleanup(number1, number2)
        if checked_numbers is None:
            print("Invalid input")
            time.sleep(1)
            clear()
            continue

        number1, number2 = checked_numbers

        try:
            result = function(number1, number2)
        except ZeroDivisionError:
            print("Division by zero")
            time.sleep(1)
            clear()
            continue

        print(f"result: {result}")
        time.sleep(3)
        clear()
        choice: str = get_user_input("Do you want to continue? (y/n)\n>>> ")

        if choice == "n":
            clear()
            print("Goodbye")
            break
        if choice == "y":
            clear()
            print("Let's go")
            time.sleep(0.25)
            clear()
            continue
        else:
            clear()
            print("Invalid input, fuck u")
            exit()

#Program start
if __name__ == "__main__":
    main()
