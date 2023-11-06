# Step 0
number_of_attempts = 0
# Step 1
users_password = "password"

# Step 1 a
while number_of_attempts < 3:
    # Step 2
    user_input = input("Please enter your password: ")
    # Step 3
    password_match = user_input == users_password
    # Step 4
    if password_match:
        print("You have successfully logged in!")
        break
    # Step 5
    else:
        number_of_attempts += 1
        print(f"Incorrect password! You have {3 - number_of_attempts} attempts left.")
