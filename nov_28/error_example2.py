
try:
    def a(x, y):
        print(f"a({x}, {y})")
        try:
            return x / y
        except ZeroDivisionError:
            #print("ZeroDivisionError was handled")
            return 0

    def b(x, y):
        return a(x, y)

    def c(x, y):
        r = b(x, y)
        return r

    def d(x, y):
        return c(x, y)
    
    d(1, 0)
except SyntaxError:
    print("SyntaxError was handled")
