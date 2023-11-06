grocery_list = ("chicken", "milk", "eggs", "meat", "rice", 1, 3.14,  True, ("hello", "world"))


def print_tuple(grocery_list):
    # print("Grocery List Length: ", len(grocery_list))

    # index = 0
    # while True:
    #     print("Pick up", grocery_list[index])
    #     index += 1

    #     if index >= len(grocery_list):
    #         break

    for item in grocery_list:
        print("Pick up", item)


def contains(grocery_list, item):
    if item in grocery_list:
        print(f"{item} is in the list")
    else:
        print(f"{item} is not in the list")


#contains(grocery_list, ("hello", "world"))
print_tuple(grocery_list)
