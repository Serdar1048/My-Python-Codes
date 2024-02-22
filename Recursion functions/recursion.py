
#todo Write a recursive Python function named merge that will merge two sorted lists of integers and return 
#todo the merged sorted list. For example:
def merge(l1,l2):
    if len(l1) == 0 :
        return l2
    elif len(l2) == 0:
        return l1
    else:
        if l1[0] < l2[0]:
            return [l1[0]] + merge(l1[1:] , l2)
        else:
            return [l2[0]] + merge(l1,l2[1:])
        

# print(merge([1, 4, 7, 11, 14], [2, 3, 6, 11, 13, 17]))
#* result: [1, 2, 3, 4, 6, 7, 11, 11, 13, 14, 17]
print(merge([3, 7, 9, 11],[1, 5, 7, 12, 13, 19]))

#todo reverse string
def reverser(str):
    if len(str) == 0:
        return ""
    else:
        return str[-1] + reverser(str[:-1])
print(reverser("summer"))

#todo Bir küme, liste olarak veriliyor. Bu fonksiyon, listenin tüm alt kümelerinin liste olarak bulunduğu listeyi döndürmelidir.
def eleman_ekleyici(eleman, liste_listesi): # liste icindeki her listeye elemani ekler
    if liste_listesi == []:
        return []
    else:
        return [liste_listesi[0] + [eleman]] + eleman_ekleyici(eleman, liste_listesi[1:])

def altKumeler(liste):
    if liste == []:
        return [[]]
    else:
        return  altKumeler(liste[:-1]) + eleman_ekleyici(liste[-1] , altKumeler(liste[:-1]))

print(altKumeler(["a","b","c"]))
# >>> [[], ['a'], ['a', 'b'], ['a', 'b', 'c'], ['a', 'c'], ['b'], ['b', 'c'], ['c']]

#todo Bir listenin içinde listeler olsun. Her bir iç listeye belirli bir elemanı ekler
def eleman_ekleyici(eleman, liste):
    if liste == []:
        return []
    else:
        return [[liste[0]] + [eleman]] + eleman_ekleyici(eleman, liste[1:])


print(eleman_ekleyici("1234", [[1],[2],[3,4,5]]))
# >>> [[1, '1234'], [2, '1234'], [3, 4, 5, '1234']]

#todo Listede belirli bir elemanın tekrar sayısını döner (count)
def tekrar(liste , n):
    if liste == []:
        return 0
    if liste[0] == n:
        return 1 + tekrar(liste[1:], n)
    else:
        return 0 + tekrar(liste[1:], n)

print(tekrar([1,2,3,4,5,'1',1,'1'],1))

#todo Listedeki sayıları toplar. Eğer listenin içinde iç içe listeler varsa her bir listenin içindeki sayıları da toplar.
def liste_toplayici(liste):
    if liste == []:
        return 0
    else:
        if type(liste[0]) != list:
            return  liste[0] + liste_toplayici(liste[1:])
        else:
            return liste_toplayici(liste[0]) + liste_toplayici(liste[1:])
        
print(liste_toplayici([1,1,[1,1,[1,1,[1,1,[1,1,[1,1,[1,1]]]]]]]))

#todo iç içe listeleri terse çevir *******
def reverser(l):
    if l == []:
        return []
    else:
        if type(l[-1]) == list:
            return [reverser(l[-1])] + reverser(l[:-1])
        else:
            return [l[-1]] + reverser(l[:-1])
        
print(reverser([1,2,[6,5,[7,8]],11,12,11,[13],[14]]))

def ic_ice_list_tersdondur(liste):
    if liste == []:
        return []
    else:
        if type(liste[-1]) == list:
            return ([ic_ice_list_tersdondur(liste[-1])]
                   + ic_ice_list_tersdondur(liste[:-1]))
        else:
            return [liste[-1]] + ic_ice_list_tersdondur(liste[:-1])
# Ornek:
print(ic_ice_list_tersdondur([1,2,[6,5,[7,8]],11,12,11,[13],[14]]))
# >>> [[14], [13], 11, 12, 11, [[8, 7], 5, 6], 2, 1]

#! Tanımladığımız fibonacci fonksiyonunun n. terimini değil de n tane terimini liste halinde döndüren versiyonu
def fibo(n,onceki=1,simdiki=1):
    if n<=1:
        return [onceki]
    else:
        return [onceki] + fibo(n-1,simdiki,onceki+simdiki)

print(fibo(14))

#todo listenin en küçük ve en büyük elemanını bul
l=[2,3,2,1,11,-321,321312]
def big(l):
    if len(l)==1:
        return l[0]
    if l[0] > l[1]:
        return big([l[0]] + l[2:])
    else:
        return big(l[1:])
   
def small(l):
    if len(l)==1:
        return l[0]
    if l[0]>l[1]:
        return small(l[1:])
    else:
        return small([l[0]] + l[2:])

print(small(l))

#todo reverser
def reverse_list(l):
    new_l = []

    if len(l)==0:
        return []
    else:
        new_l = reverse_list(l[1:]) + [l[0]]   #[l[-1]] + reverse_list(l[:-1])
    return new_l

print(reverse_list([1,2,3,4,5]))

#todo total digit 
def total_digit(n):
    total = 0
    if n==0:
        return 0
    else:
        total = total_digit(n//10) + n%10 
    
    if total > 9:
        return total_digit(total)
    else:
        return total
print(total_digit(17854212))

#todo fibonacci with dict
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
dict={}
for i in range(10):
    dict[i] = fibonacci(i)
print(dict)

#! ebob
def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)

print(gcd(12,15))

#todo Hanoi Kuleleri 
def move (fr,to):
    print("diski hareket ettir: " + str(fr) + "-->" + str(to) )


def playHanoi(n, baslangic, bitis, gecici ):
    if n==1:
        move(baslangic,bitis)
    else:
        playHanoi(n-1,baslangic,gecici,bitis)
        playHanoi(1,baslangic,bitis,gecici)
        playHanoi(n-1,gecici,bitis,baslangic)


playHanoi(2, "A", "B", "C" )

#todo fibonacci
# ? yol:1
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
# 0 1 1 2 3 5 8 13
for i in range(10):
    print(fibonacci(i))

#? yol:2
def fib(n):
    if n<=1:
        return n
    t = fib(n-1)+fib(n-2)
    return t
for i in range(10):
    print(fib(i))


#todo listedeki elemanları toplama
#? yol:1
def sum_list(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_list(list[1:])
print(sum_list([1,2,3,4,5]))

#? yol:2
def sum_list2(list):
    if len(list)==0:
        return 0
    else:
        first_el = list.pop(0)
        return first_el + sum_list(list)
print(sum_list([1,2,3,4,5]))

#? yol:3 --> listeye dokunmadan
def sum_list(list, count = 0):
    if count == len(list):
        return 0
    else:
        add_el = list[count]
        count += 1
        return add_el + sum_list(list,count)

print(sum_list([1,2,3,4,5]))

#todo output ????? **** (bilgisayar kavramları youtube)
def f(n):
    if n>1:
        f(n-1)
    print(n)
n = 3
f(n)

#todo factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#todo reverse
def reverser(list):
    r = []
    for x in list:
        r = [x] + r
    return r
print(reverser([1,2,3,4,5]))

def reverser(list):
    if len(list)==0:
        return []
    else:
        return [list[-1]] + reverser(list[:-1])
print(reverser([1,2,3,4,5]))

def reverser(list):
    if len(list)>0:
        return [list[-1]] + reverser(list[:-1])
    else:
        return[]
print(reverser([1,2,3,4,5]))

#todo reverse yapma yolu
def reverse (list):
    new_list=[]
    for i in range(len(list)):
        last_eleman = list.pop(-1)
        new_list.append(last_eleman)
    return new_list
print(reverse([1,2,3,4,5]))

#todo basamakları toplama
def sum_digit(n):
    if n > 0:
        return n%10 + sum_digit(n//10)
    else:
        return 0
print(sum_digit(0))

#todo basamak toplamı tek sayı olana kadar topluyor ***
def sum_digit(n):
    if n >= 10:
        x = n%10 + sum_digit(n//10)
        if x>=10:
            return x%10 + sum_digit(x//10)
        else: 
            return x
    else:
        return n
print(sum_digit(566))

#todo kelimeden bir harf çıkartarak yaz
def write(w):
    if len(w)>0:
        print(w)
        # write(w[1:]) #? baştan çıkartıyor
        write(w[:-1]) #? sondan çıkartıyor
write("araba")

#todo output
def x(a):
    print("hello")
    if a<3:
        a+=1
        x(a)
    print("world")

(x(1))

#todo belirli değer aralığındaki(first,last) 5'in katı olan sayıları topla ---> dene bidaha  (Gençay Yıldız youtube)
def sum_number(first,last):
    if first%5 == 0:
        return first + sum_number(first+1,last)
    if first<last:
        return sum_number(first+1,last)
    return 0

print(sum_number(10,20))