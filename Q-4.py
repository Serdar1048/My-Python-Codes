
#? Q.4: Analyze the code snippet below and write the values of variables x and y next to
#? the print lines.

def f():
    y = 1
    global x
    print(x, y) # x => ___ y => ___

    def g():
        nonlocal y
        y = x + y
        print(x, y) # x => ___ y => ___
        return y / 2
    x = 7
    print(x, y) # x => ___ y => ___
    return g

x = 5
y = 3
print(x, y) # x => ___ y => ___
b = f()
y = b()
print(x, y) # x => ___ y => ___



#!------------------------------------------------------------------------------------------
#? örnek
#? Q: Analyze the code snippet below and write the values of variables a and b next to
#? the print lines.

def outer():
    b = 2
    global a
    print(a, b)                    # a => ___ b => ___

    def inner():
        nonlocal b
        b = a * b
        print(a, b)                # a => ___ b => ___
        return b - 1
    a = 4
    print(a, b)                    # a => ___ b => ___
    return inner

a = 3
b = 5
print(a, b)                        # a => ___ b => ___
c = outer()
b = c()
print(a, b)                        # a => ___ b => ___



def outer():
    a = 3
    b = 2
    print(a, b)  # a => ___ b => ___

    def inner():
        nonlocal a
        b = a + 2
        print(a, b)  # a => ___ b => ___
        return b * 3
    a = 5
    print(a, b)  # a => ___ b => ___
    return inner

a = 1
b = 4
print(a, b)  # a => ___ b => ___
c = outer()
b = c()
print(a, b)  # a => ___ b => ___


def outer():
    y = 3
    global x
    print(x, y)  # x => ___ y => ___

    def inner():
        nonlocal y
        x = y - 1
        print(x, y)  # x => ___ y => ___
        return x + y
    x = 7
    print(x, y)  # x => ___ y => ___
    return inner

x = 5
y = 2
print(x, y)  # x => ___ y => ___
z = outer()
y = z()
print(x, y)  # x => ___ y => ___


#? Q: Analyze the code snippet below and write the values of variables a and b next to
#? the print lines.

def outer():
    b = 2
    global a
    print(a, b)  # a => ___ b => ___

    def inner():
        nonlocal b
        b = a * b
        print(a, b)  # a => ___ b => ___
        return b - 1
    a = 4
    print(a, b)  # a => ___ b => ___
    return inner

a = 3 #4
b = 5
print(a, b)  # a => ___ b => ___
c = outer()
b = c()
print(a, b)  # a => ___ b => ___