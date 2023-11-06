my_map = {"a":"apple", "b":"banana", "c":"cherry"}
print("Before:",my_map)
my_map["c"] = "orange"
my_map["d"] = "grape"
print("After:",my_map)

for key in my_map:
    print(key, my_map[key])
print("-"*50)
for key, value in my_map.items():
    print(key, value)
