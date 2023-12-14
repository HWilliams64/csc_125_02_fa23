def number_input(prompt="Please enter a number: "):
    number_str = input(prompt)
    try:
        return float(number_str.strip())
    except ValueError:
        return number_input("Invalid input. Please try again: ")


def op_input(prompt="Please enter a operation: ", default_operations="+-*/**|"):
    operation = input(prompt)
    operation = operation.strip()

    if operation.isdigit():
        raise TypeError(f"Numbers are not accepted as operations.")

    # + - * /
    if operation in default_operations:
        return operation
    else:
        raise ValueError(f"Unknown operation `{operation}`.")

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y

calc_dict = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

while True:
    num1 = number_input()

    try:
        op1 = op_input()
    except (ValueError, TypeError) as e:
        print(f"Invalid input. {e}")
        continue

    num2 = number_input()

    try:
        func = calc_dict[op1]
        result = func(num1, num2)
        print(f"{num1} {op1} {num2} = {result}")
    except ArithmeticError as e:
        print(f"Unable to calculate: {num1} {op1} {num2} because {e}.")
    except KeyError as e:
        print(f"Operation `{op1}` is not supported.")
    except Exception as e:
        print(f"Something went wrong! {e}")
        
