
#todo 4 milyondan küçük çift fibo sayılarının toplamı

def fibonacci():
    fibo = [1,1]
    total = 0
    while fibo[-1] + fibo[-2] < 4000000:
        fibo.append(fibo[-1] + fibo[-2])
    for i in fibo:
        if i%2==0:
            total += i
    print(total)
fibonacci()
