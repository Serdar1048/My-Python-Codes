def arttir(x):
    return x*1.2

personel=["ali","veli","can","canan","kemal"]
maas =[1000,2000,3000,4000,5000]

yeniMaas = list(map(arttir,maas))
sonuc = list(zip(personel,yeniMaas))
# print(sonuc)
# print(yeniMaas)

for i,k in sonuc:
    print("{} isimli personel zamlı maaşı : {}".format(i,k))
