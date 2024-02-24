
kare = lambda x : x**2
 
küp = lambda y : y**3

toplam = lambda x,y : x+y

genel_toplam = lambda *args : sum(args)
print(genel_toplam(1,2,3))

print((lambda x,y,z : x*y+z)(3,5,6))

print((lambda *args : sum(args)//len(args))(2,3,4,5,6,7,8))

#!--------------------------

liste = [("a",12),("c",2),("b",23),("e",98),("d",313)]
liste.sort(key = lambda x:x[1])
print(liste)

#!--------------------------

liste2 =[{"isim" : "a" ,"soyad":"b" , "yas" : 12},{"isim" : "d" ,"soyad":"a" , "yas" : 120},{"isim" : "c" ,"soyad":"e" , "yas" : 19}]

liste2.sort(key=lambda x: x["soyad"])
print(liste2)

#!--------------------------

isim_soyisim = ["a b","c a","e f","g h"]
isim_soyisim.sort(key = lambda x:x.split()[-1].lower())
print(isim_soyisim)

#!--------------------------

denklem = lambda x: x*2
print(denklem(2))