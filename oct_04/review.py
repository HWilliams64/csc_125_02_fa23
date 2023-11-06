
def subtract(x = 5, y = 7):
    result = x - y
    print(f"{x} - {y} = {result}")
    return result

print(subtract(y=0, x=10))
print("="*10)
print(subtract(y=10, x=0))
print("="*10)
print(subtract(10, 0))
