from art import logo


def add(n1: float, n2: float) -> float:
    return n1 + n2


def subtraction(n1: float, n2: float) -> float:
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    return n1 / n2


operations = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if option == "y":
            num1 = answer
        elif option == "n":
            should_continue = False
            calculator()
        else:
            return


calculator()
