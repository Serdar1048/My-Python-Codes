# 1-1000 arasındak fibonacci sayılarını bul 1-1-2-3-5-8-13-21-34...

a=1
b=1
c=0
print(a)
print(b)

while c <1000: 
    print(b)
    c=a+b
    a=b
    b=c
