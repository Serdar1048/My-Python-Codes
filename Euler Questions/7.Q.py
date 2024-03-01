
#todo 10.001. asal sayı kaçtır

def is_prime(n):
    prime = True
    if n==1:
        prime = False
    for i in range(2,int((n**0.5))+1):
        if n%i==0:
            prime = False
            break
    return prime
print(is_prime(29))

def nth_prime():
    counter = 0
    n = 1
    while True:
        if is_prime(n):
            counter += 1
        if counter == 10001:
            break
        n += 1
    return n
print(nth_prime())