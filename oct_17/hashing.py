my_set = {1, 2, 3, "a", "b", "c", "d",}
my_set.update("abcdef")
for item in my_set:
    print(item)
###########################################################################
grocery = ["milk", "eggs", "bread", "milk", "cheese", "bread", "milk"]
grocery_set = set(grocery)
grocery = list(grocery_set)
print(grocery)