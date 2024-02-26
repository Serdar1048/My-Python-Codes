
#!File İşlemleri 

#todo okuma ve başka yere kopyalama
with open("test.txt") as okunacak:
    with open("test2.txt","w") as yazilacak:
        #icerik = okunacak.readlines()
        for satir in okunacak:#icerik
            yazilacak.write(satir)

#todo write
with open("test2.txt","w")as f:
    f.write("Python")

#todo append
with open("test2.txt","a")as f:
    f.write("Python")

#todo eğer dosya büyükse küçük küçük dosyayı okuruz
with open ("test.txt") as f:
    okunacak_miktar = 10
    icerik = f.read(okunacak_miktar)
    while len(icerik)> 0:
        print(icerik,end="")
        icerik = f.read(okunacak_miktar)

with open("test.txt","r") as f:
    icerik = f.read(2)
    print(icerik,end="")
    icerik = f.read(2)
    print(icerik,end="")
    icerik = f.read(2)
    print(icerik,end="")

with open("test.txt","r") as f:
    icerik = f.readline()
    print(icerik,end="")
    pozisyon = f.tell()
    print(pozisyon)
    f.seek(0)
    icerik = f.readline()
    print(icerik,end="")

    for satır in icerik:
        print(satır,end = "-")