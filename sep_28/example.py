def add(x=0, y=0, z=1):
    print("x:", x, "y:", y, "z:", z)
    return (x + y) * z

result = add(5, 4, z=-1)
assert result == -9
