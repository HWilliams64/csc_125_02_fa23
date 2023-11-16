# Modes
# r - read
# w - write (WARNING THIS DELETES EVERYTHING)
# a - append
# a+ - append and read
# r+ - read/write
# w+ - write then read (WARNING THIS DELETES EVERYTHING)

file = open("./example.txt", "r+")
text = file.read()
print("Read 1 ->", text)
print("cursor location:", file.tell(), len(text))
file.write("\nSecond text")
print("cursor location:", file.tell())
file.seek(len(text))
print("---")
print(file.read())
print("---")
