# V2 brings improved performance, readability and improved functionality. Stay tuned for further improvements!



import os
import operator
import time
import typing

def number_input_cleanup(*args: str) -> typing.Optional[tuple[float, ...]]:
    try:
        return tuple(float(arg) for arg in args)
    except ValueError:
        return None

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

operators: dict[str, typing.Callable] = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '**': operator.pow,
    '%': operator.mod,
}

def get_user_input(prompt: str) -> str:
    return input(prompt).strip().lower()

def main() -> None:
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
        break

if __name__ == "__main__":
    main()
