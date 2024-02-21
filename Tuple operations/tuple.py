
#?liste ye benzer ama farkı değiştirilemez olması (readonly) bu yüzden listeden daha hızlıdır. 
#! IMMUTABLE

#! tuple oluşturma yöntemleri
meyve_tuple = ("elma" , "armut" , "kayısı" , "karpuz" , "kayısı" , 2 , [4 , 6] , (8 , 10 , 12))

sayilar = 1,2,3,4
print(type(sayilar)) #todo (1, 2, 3, 4)  --  type---> tuple

#! tek elemanlı tuple da sıkıntı var. Elemanın yanında virgül varsa TUPLE'dır
tuple_deger1 = "Ali"
print(tuple_deger1) #todo Ali
print(type(tuple_deger1)) #todo str

tuple_deger1 = ("Ali")
print(tuple_deger1) #todo Ali
print(type(tuple_deger1)) #todo str

tuple_deger2 = "Ali",
print(tuple_deger2) #todo ('Ali',)
print(type(tuple_deger2)) #todo tuple

print(type(meyve_tuple[5:6])) #todo (2,)  --  type---> tuple

#! yazdırma
print(meyve_tuple)
print(meyve_tuple[5:6]) #todo (2,)
print(meyve_tuple[2]) #todo kayısı
print(meyve_tuple[-2][0]) #todo 4
print(meyve_tuple[4:7]) #todo ('kayısı', 2, [4, 6])

#! tuple'ın içindeki LİSTE elemanını güncelleştirebiliriz
meyve_tuple[-2][0] = 5
print(meyve_tuple)

meyve_tuple[-2].append(9)
print(meyve_tuple)

#! TUPLE DEĞİŞTİRİLEMEZ
# meyve_tuple[1] = "kivi" #todo 'tuple' değiştirilemez ----> TypeError 

#! iki tuple'ı toplayabiliriz
sayi1 = 1,2,3,4
sayi2 = 5,6,7,8
sayilar = sayi1 + sayi2
print(sayilar) #todo (1,2,3,4,5,6,7,8)

#! len(" ") methodu
print(len(meyve_tuple)) #todo 8

#! .count(" ") methodu
print(meyve_tuple.count("kayısı")) #todo 2
print(meyve_tuple.count("kavun")) #todo 0

#! .index(" ") methodu
print(meyve_tuple.index("karpuz")) #todo 3 -- ilk gördüğü karpuzun indexini verir.
# print(meyve_tuple.index("kavun")) #todo ValueError

#! del methodu ----> değiştirilemez olduğu için eleman silemeyiz ama bütün tuple'ı silebiliriz.
# del meyve_tuple[2] #todo TypeError
# del meyve_tuple
# print(meyve_tuple) #todo NameError  undefined gelir

#! tuple'da değer değiştirme (bunu liste'de de yapabiliriz)
x = 2
y = 3
(x,y) = (y,x)
x,y = y,x
print("X",x," Y",y)

#! while döngüsü ile elemanları tek tek yazdırma

a = 0
while a<len(meyve_tuple):
    print(meyve_tuple[a])
    a+=1

#! tuple halinde menu tutma
menu =(
    ("Zinjor Burger",18),
    ( "Plasma Tacosi", 15),
    ( "Kozmik Kebap" ,30),
    ( "Robotik Rulo", 14),
    ("Lazer Limonata",4),
    ("Galaktik RoketBurger" ,25),
    ( "Karbonlu Macaron" ,20),
    ( "Güneş Patlaması Pizza" ,30),
    ( "Kozmik Kıymalı Köfte", 35),
    ( "Yıldız Tozu Sufle",25),
    ( "Galaktik Izgara Tavuk", 40),
    ( "Gezegen Gevreği" ,15),
    ( "Astro Smoothie", 20),
    ( "Galaktik Dondurma", 30),
    ( "SIVI Meteorit Şurubu" ,10)
)

a = 0
while a < len(menu):
    print(menu[a][1] , menu[a][0])
    a+=1