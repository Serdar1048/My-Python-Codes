
#todo 1000 den küçük 3 e ve 5 e bölünen sayıların toplamı

def check(x):
    if x%3 == 0 or x%5 == 0:
        return True
    else:
        return False
total = 0

for i in range(1,10):
    if check(i):
        total += i
print(total)

