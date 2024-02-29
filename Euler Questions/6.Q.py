
#todo ilk 100 doğal sayının toplamının karesinden karelerinin toplamını çıkart

def total():
    sum = 0
    for i in range(1,101):
        sum += i
    return sum*sum

def square_total():
    sum = 0
    for i in range(1,101):
        sum += (i*i)
    return sum
result = total() - square_total()
print(result)