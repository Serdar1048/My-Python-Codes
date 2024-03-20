n1 = int(input("your firstt number: "))
n2 = int(input("your second number: "))
n3 = int(input("your third number: "))

buyuk = n1

if n2>buyuk:
    buyuk = n2
if n3>buyuk:
    buyuk = n3

print("En büyük sayı ",buyuk)

# if n1>n2 and n1>n3:
#     print(n1 , "büyüktür")
# elif n2>n1 and n2>n3:
#     print(n2,"büyüktür")
# else:
#     print(n3,"büyüktür")
