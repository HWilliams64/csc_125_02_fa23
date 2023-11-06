import hashlib

db = {
    "michael9":{
        "first_name":"Michael",
        "last_name":"Gilligan",
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    },
    "nobel": {
        "first_name": "Nobel",
        "last_name": "T",
        "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
    }
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username not in db:
    print("User not found")

password_hash = hashlib.sha256(password.encode()).hexdigest()

if db[username]["password"] == password_hash:
    print("Login successful")
else:
    print("Login failed")
