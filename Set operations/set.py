
#* tekrar eden elemanların bir tanesini yazar. --> listeden farkı
#! set oluşturma yöntemleri
A = {1,2,3}
B = {3,4,5}
C = A.difference(B)

print(A) #todo {1,2,3}
print(B) #todo {3,4,5}
print(C) #todo {1,2}  type--> set

#! set(" ") --> bir tane argüman alır ve bu argüman int olamaz
kume1 = {"ben bir metinim, bir string ifadeyim"}
print(kume1) #todo {'ben bir metinim, bir string ifadeyim'}

kume2 = set("ben bir metinim, bir string ifadeyim") #todo {'s', 'g', 'y', 'e', 'n', 'r', 'd', 'a', ' ', 't', 'm', 'b', 'f', 'i', ','}
print(kume2)

kume3 = set([1,2,6,7,8,9,0,0,2,6])
print(kume3) #todo {0, 1, 2, 6, 7, 8, 9} --> sıralı veriyor

#! kesişim .intersection(" ") methodu
print(A.intersection(B)) #todo {3} -- A kesişim B

#! fark .difference(" ") methodu
print(A.difference(B)) #todo {1,2} -- A fark B

#! birleşim .union(" ") methodu
print(A.union(B)) #todo {1,2,3,4,5} -- A birleşim B 
print(A) #todo {1, 2, 3} 

#! birleşim .update(" ") methodu --> birleştirdikten sonra bunu kümeye atar.
A.update(B)
print(A) #todo {1, 2, 3, 4, 5}

#! for döngüsü ile tek tek yazdırma
for  i in C:
    print(i)

#! ekleme .add(" ") methodu
C.add("elma")
print(C)

#! çıkarma .discard(" ") methodu
C.discard(1)
print(C)

#! temizleme .clear() methodu
C.clear()
print(C)

#! eleman silme .pop() methodu
print(A.pop()) #todo sildiği elemanı yazdırır --> 1
print(A) #todo {2, 3}

#! 1 == True ve 0 == False
D = {1 , True , False , 0} #todo ilk yazılanı alıyor
print(D) #todo {False,1}