import os

print("Current directory is: " + os.getcwd()) # This gets our current working directory
print("Current directory parent: " + os.path.dirname(os.getcwd())) # this gets the parent directory of our current working directory
print("Current directory name: " + os.path.basename(os.getcwd())) # this gets the name current working directory

# grocery_list = ["apple", "banana", "cherry"]
# grocery_list_pretty = "=".join(grocery_list)
# print(grocery_list_pretty)

directories = ["/", "home", "developer", "Documents", "code"]
full_path = os.path.join(*directories)
print(f"Full path is: {full_path}")

print("Does this exist:", os.path.exists(full_path))
print("Is this a directory:", os.path.isdir(full_path))
print("Is this a file:", os.path.isfile(full_path))
