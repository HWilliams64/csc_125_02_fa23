value_1 = input("Type a number: ")
value_2 = input("Type a number: ")

print(f"value 1 is int: {value_1.isdigit()}")
print(f"value 2 is int: {value_2.isdigit()}")

if value_1.isdigit():
    number_1 = int(value_1)
else:
    number_1 = 0

if value_2.isdigit():
    number_2 = int(value_2)
else:
    number_2 = 0

print(f"{number_1} + {number_2} = {number_1 + number_2}")