# if - block of code that is executed based of a bool

# if <Expression> :
#    code
# - <Expression> must equal true for the code to be executed
# - colon at the end (:) means next line must indented for ownership
#
# `==` this is value equality
# `is` identity equality

string_1 = "hello" * 10000
string_2 = "hello" * 10000

print(f"String 1 ID = {hex(id(string_1))}")
print(f"String 2 ID = {hex(id(string_2))}")

if string_1 == string_2:
    print("The strings have the same value")
else:
    print("The strings have different values")

if string_1 is string_2:
    print("The strings have the same identity")
else:
    print("The strings have different identities")
