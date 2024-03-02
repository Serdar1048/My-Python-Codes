
#? Q.1: Write a function named 'list_operations' that takes a list as an argument (in list) and returns
#? a value that is calculated by subtracting the sum of even numbers from the sum of odd numbers in
#? 'in_list'.

def list_operations(list):
    even_sum = 0
    odd_sum = 0 
    for i in list:
        if i%2==0:
            even_sum += i
        else:
            odd_sum += i
    return odd_sum - even_sum
print(list_operations([1,2,3,4,5,6,7]))


#? Q: Define a recursive function h(y) that calculates the product of digits.
#? For instance, what does h(456) return?

def h(y):
    ys = str(y)
    if len(ys) == 1:
        return int(ys)
    product = int(ys[0]) * int(ys[1])
    if len(ys) == 2:
        return product
    else:
        return product * h(ys[2:])

# What does h(789) return?
result = h(789)
print(result)

def g(x):
    xs = str(x)
    if len(xs) == 1:
        return int(xs) ** 2
    n = int(xs[0]) ** 2 + int(xs[1]) ** 2
    if len(xs) == 2:
        return n
    else:
        return n + g(int(xs[2:]))

# What does g(543) return?
result = g(543)
print(result)