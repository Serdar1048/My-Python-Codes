
#todo 2 milyondan küçük bütün asal sayıları toplamı kaçtır

def is_prime(n):
    prime = True
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime = False
            break
    return prime
# print(is_prime(17))

total = 0
i = 2
while True:
    if is_prime(i):
        total+=i
    if i == 2000000:
        break
    i+=1
print(total)

# for i in range(2000000):
#     if is_prime(i):
#         total+=i
# print(total)