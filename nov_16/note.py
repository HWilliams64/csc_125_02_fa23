def write_file(file_name):
    new_note = input("Enter a new note: ")
    new_note += "\n"

    with open(file_name, "a") as file:  # same as -> file = open(file_name, "a")
        file.write(new_note)

def read_file(file_name):
    with open(file_name, "r") as file:  # same as -> file = open(file_name, "r")
        print("Your current notes:")
        for line in file:
            print(line, end="")



while True:
    file_name = "notes.txt"
    user_input = input("w - new note\nr - read note\nq - quit\n")

    if user_input == "w":
        write_file(file_name)
    elif user_input == "r":
        read_file(file_name)
    else:
        break

    print("-"*80)