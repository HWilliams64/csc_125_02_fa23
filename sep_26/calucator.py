def input_a_number(attempts):
    limit = 3
    if attempts == limit:
        return 0

    number = input("Enter a number: ")
    if number.isdigit():
        return int(number)
    else:
        print(f"Please enter a valid number you have {limit - attempts-1} left")
        return input_a_number(attempts+1)

x = input_a_number(0)
y = input_a_number(0)
print(f"{x} + {y} = {x+y}")