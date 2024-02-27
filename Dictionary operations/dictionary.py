
#! dict oluşturma yöntemleri
kisi = dict(
    isim = "ali" ,
    yas = 20 ,
    cinsiyet = "m" ,
    hobiler = ["Sinema","Konser","Yazılım"],
    lokasyon = {      #todo dict() şeklinde de sözlük içerisinde sözlük oluşturabilirsin.
            "yasadigi_sehir":"Berlin",
            "dogdugu_sehir":"Istanbul"
    }
)

kisi = {
        "isim" : "ali" ,
        "yas" : 20 ,
        "cinsiyet" : "m" ,
        "hobiler" : ["Sinema","Konser","Yazılım"],
        "lokasyon" :{
            "yasadigi_sehir":"Berlin",
            "dogdugu_sehir":"Istanbul"
        }
}

#! yazdırma
print(kisi["isim"])
print(kisi["hobiler"])
print(kisi["yas"])
print(kisi)
print(kisi["lokasyon"])
print(kisi["lokasyon"]["yasadigi_sehir"])

#! sözlük uzunluğu bulma len(" ") methodu
print(len(kisi))

#! güncelleme
kisi["isim"] = "veli"
kisi["hobiler"][0]="a"
print(kisi)

#! birden fazla güncelleme ve yeni alanlar ekleme ----> update( {...} ) methodu
kisi.update({ "isim" : "ahmet" , "yas" : 30 , "id" : 12345 , "hobiler" : ["a" , "b"] })
print(kisi)

#! alan ekleme ve silme ---> del methodu
kisi["id"] = 12345
print(kisi)

# del kisi["id"]
# print(kisi)

# del kisi #todo sözlüğü ortadan kaldırıyor.
# print(kisi) #todo NameError

#! .clear() methodu
# kisi.clear() #todo sözlüğün içini boşaltıyor.
# print(kisi)  #todo ----> {}

#! .pop(" ") methodu ile alan silme
print(kisi.pop("yas")) #todo silinen alanın value'sunu döndürür. ----> 20
print(kisi)

#! .popitem() methodu ile alan silme
print(kisi.popitem()) #todo SON eklenen alanı siler ve silinen alanı döndürür.----> ('hobiler', ['Sinema', 'Konser', 'Yazılım'])
print(kisi)

#! for döngüsü ile yazdırma
for x in kisi: 
    print(x) #todo key'leri yazdırır.

for x in kisi: 
    print(kisi[x]) #todo value'ları yazdırır.

#! .keys() methodu
print(kisi.keys()) #todo key'lerden oluşan bir LİSTE yazdırır.

#! .values() methodu
print(kisi.values()) #todo value'lardan oluşan bir LİSTE yazdırır.

#! .items() methodu
print(kisi.items()) #todo key'lerden ve value'lardan oluşan bir LİSTE yazdırır.

#! for döngüsü ile yazdırma ---> .items() methodu
for k in kisi.items():
    print(k) #todo tupple şeklinde yazdırır.

for k,v in kisi.items():
    print(k,v)

#! olmayan bir alanı görüntülemeye çalıştığımız zaman ----> KeyError
# print(kisi["id"]) #todo KeyError verir. id diye bir key yok.

#! .get(" " , " ") methodu ----> yukarıdaki hatayı çözer
print(kisi.get("id" , "bulunamadı")) #todo None yazdırır. ----> bulunamadı
print(kisi.get("isim" , "bulunamadı")) #todo Value'yu yazdırır. ----> ali

print(kisi.get("lokasyon"))
print(kisi.get("lokasyon").get("dogdugu_sehir"))
#! for döngüsü ile key'leri veya value'ları tek tek yazdırma
for i in kisi.keys():
    print(i)

for j in kisi.values():
    print(j)

#?ÖRNEK
text = """In this exercise, we will delve into the fundamentals of the Perceptron and the 
Backpropagation algorithm, which are foundational concepts in the field of artificial neural 
networks.
These concepts play a crucial role in the development and training of neural networks, 
enabling them to learn and make predictions from data. By the end of this exercise, you will
have a better apply basic concepts of programming such as function conditionals and loops
on a perceptron backpropagation algorithm based On Calculus."""

def counter_word(text):
    dict = {}
    for word in text.lower().split():
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    for k,v in sorted(dict.items()):
        print (k,v)

counter_word(text)  

#! referans olayı vardır
p1 = {
    "name" : "samsung s20",
    "price": 6000
}

p2 = {
    "name" : "samsung s22",
    "price": 8000
}

p1 = p2

p1["price"]= 7000

print(p1)   #! p1'i değiştiriyorum fakat yukarıda bunları eşitleyip aynı referansa 
print(p2)   #! gönderdiğim için p2 de değişiyor.
 
#! .copy() methodu
p1 = {
    "name" : "samsung s20",
    "price": 6000
}

p2 = {
    "name" : "samsung s22",
    "price": 8000
}

p2 = p1.copy()

p1["price"]= 7000

print(p1)
print(p2) 

#! liste içinde dict
p1 = {
    "name" : "samsung s20",
    "price": 6000
}

p2 = {
    "name" : "samsung s22",
    "price": 8000
}

products = [p1 , p2 , {"name" : "samsung s23" , "price": 9000}]

for p in products:
    print(p) 
    print(p["name"])
    print(p.values())

for p in products:
    for key, value in p.items():
        print(key, value)