from typing import Callable

def add(x: float = 0, y: float = 0) -> float:
    """
    This function adds the two numbers it is given and returns the result.
    """

    # This is returned to the user
    return x + y

def minus(x: float = 0, y: float = 0) -> float:
    """
    This function subtracts the two numbers it is given and returns the result.
    """

    # This is returned to the user
    return x - y

def calc(x:float, y:float, operation:Callable):
    print("x:", x)
    print("y:", y)
    print("operation:", operation)
    return operation(x, y)


result = calc(x=2, y=2, operation=minus)
print("result:", result)
