grocery_list = ["beans", "rice", "avocado",
                "bread", "tomatoes", "apple", "apple", "apple"]

grocery_list_2 = ("chicken", "milk", "eggs", "meat", "rice")

grocery_list.extend(grocery_list_2)

to_remove = input("Type the name of the item you want to remove: ")
while to_remove in grocery_list:
    grocery_list.remove(to_remove)

print(grocery_list)
