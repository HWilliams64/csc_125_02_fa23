my_map = {"one": 1, "two": 2, "three": 3}

# Add a new key-value pair to the map
my_map["four"] = 4

# Add if the key does not exist
my_map.setdefault("four", 44)

#same as above
if "four" not in my_map:
    my_map["four"] = 44

# To get a value
if "five" in my_map:
    print(my_map["five"])
else:
    print("NOT IN MAP")

print(my_map.get("five", "NOT IN MAP"))

# To delete a key-value pair
# if "four" in my_map:
#     del my_map["four"]

removed_item = my_map.pop("four", "NOT IN MAP")

print(removed_item)
print(my_map)
