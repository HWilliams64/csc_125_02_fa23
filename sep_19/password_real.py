import hashlib
salt="admin"
unhashed_password = "password"
hashed_password = hashlib.sha256((salt+unhashed_password).encode()).hexdigest()

print("Before:", unhashed_password)
print("After:", hashed_password)