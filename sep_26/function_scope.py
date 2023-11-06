x = 1

def change_x():
    global x
    x = x+9
    print("Inside the function: ", x)

for _ in range(10):
    print("Before function call: ", x)
    change_x()
    print("After function call: ", x)
