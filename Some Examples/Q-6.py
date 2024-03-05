

#? Q: Write a recursive function similar to the given function f(x) that calculates the sum of digits.
#? For example, what does g(9876) return?

def g(x):
    xs = str(x)
    if len(xs) == 1:
        return int(xs)
    n = int(xs[0]) + int(xs[1])
    if len(xs) == 2:
        return n
    else:
        return n + g(xs[2:])

# What does g(54321) return?
result = g(12345)
print(result)