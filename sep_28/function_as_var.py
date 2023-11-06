
def number_input(prompt="Please enter a number: "):
    number_str = input(prompt)
    clean_number_str = number_str.strip().replace("-", "", 1).replace(".", "", 1)
    # -3.14    => 314
    if clean_number_str.isdigit():
        return float(number_str.strip())
    else:
        return number_input("Invalid input. Please try again: ")


def op_input(prompt="Please enter a operation: ", default_operations="+-*/"):
    operation = input(prompt)
    operation = operation.strip()
    # + - * /
    if operation in default_operations:
        return operation
    else:
        return op_input("Invalid input. Please try again: ")


number_1 = number_input()
operation = op_input(default_operations="+-")
number_2 = number_input()
print(number_1, operation, number_2)
