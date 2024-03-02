
#? Q.2: Write a recursion named (converter) that converts a given decimal number (decimal) to a
#? corresponding binary value (e.g., 9 =>1001).

def converter(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return converter(n//2) + str(n%2)
print(converter(9))














