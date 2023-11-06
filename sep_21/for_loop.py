my_str = input("Please enter a string: ")
# index = 0
# length = len(my_str)

# while index < length:
#     print(index, "-", my_str[index])
#     index += 1

for banana, apple in enumerate(my_str):
    print(banana, "=", apple)
