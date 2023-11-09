"/home/developer/Documents/code/csc_125_02_fa23/nov_09/write_file_example.py"

# Absolute path - a path that starts with system root directory and it starts
# with /

# Relative path - a path that is located relative to where you are working. It starts
# with the directory or file name NOT /

# ~ - a user's home directory

# r - read from the file
# w - write to the file (WARNING this delete the content that already exists
# before saving new information)
# a - append to the file

file_object = open("a/b/c", "a+")
file_object.write("New information3!")
# print(text)
