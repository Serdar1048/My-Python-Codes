
#todo 1 den 20 ye kadar olan tüm sayılara kalansız bölüne en küçük sayı kaçtır

def func():
    n=200
    sayac=0
    while True:
        for i in range(2,20):
            if n%i==0:
                sayac+=1
            else:
                sayac=0
            if sayac == 18:
                return n
        print(n)
        n+=200
print(func())

