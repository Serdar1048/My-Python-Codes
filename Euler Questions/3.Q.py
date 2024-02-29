
#todo 600851475143 sayısını en büyük asal çarpanı kaçtır

def prime(n):
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            is_prime = False
            break
    return is_prime

def prime_divede(n):
    biggest_prime=1
    for i in range(1,int(n**0.5)+1):
        if prime(i) and n%i==0:
            biggest_prime = i
    print(biggest_prime)
   
prime_divede(600851475143)