""" First version of the calculator, only supports default operators and has hard coded input
"""

import os
import operator
import time

def clear() -> None:
    os.system('cls')

operators: dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '**': operator.pow,
    '%': operator.mod,
}


def main() -> None:
    while True:

        number1: str = input("Enter first number: ")
        function: str = input("Enter operator (+,-,/,//,%,*,**): ")
        number2: str = input("Enter second number: ")

        if function not in operators.keys():
            print("Invalid operator")
            time.sleep(1)
            clear()
            continue
        try:
            number1: int = int(number1)
            number2: int = int(number2)

            print(f"result: {operators[function](number1, number2)}")
            break

        except ValueError:
            print("Invalid number/s")
            time.sleep(1)
            clear()
            continue

if __name__ == "__main__":
    main()
