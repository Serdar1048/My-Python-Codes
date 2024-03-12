# n=int(input("enter"))
# # 1000 tane asal sayı bulan program
# for i in range(2,n):
#     if n%i == 0:
#         print("asal değildir")
#         break

# else:
#     print("asaldır")
    
 
while True:
    n=int(input("Sayıyı Girin : "))
    if n > 1:
    
        for i in range(2,n):
            if (n % i) == 0:
                print(n," Asal Sayı Değildir.")
                break
        else:
            print(n," Asal Sayıdır.")
    
    else:
        print(n," Asal Sayı Değildir.")




