
# Handle different exceptions using a try-except block with multiple except clauses.
# The program should take a list and an index as input, and handle various possible errors.
try:
    my_list = [1, 2, 3, 4, 5]
    index = int(input("Enter an index: "))
    
    try:
        result = my_list[index]
        print("Element at index", index, ":", result)
    
    except IndexError:
        print("Error: Index out of range.")
    
    except ValueError:
        print("Error: Invalid index. Please enter a valid integer.")
    
    except Exception as e:
        print("Error:", e)

except Exception as e:
    print("E", e)

#?-------------------------------------------------------------------

sayi1 = input("SAYI1: ")
sayi2 = input("SAYI2: ")

try:
    print("asdasd")
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print(sayi1/sayi2)
except (ValueError,ZeroDivisionError):
    print("hatalı giriş")

#?-------------------------------------------------------------------

try: #!Burada bir hata olursa EXCEPT çalışır. Hata yoksa(except çalışmazsa) ELSE çalışır. FINALLY hep çalışır.
    a = 5
    b = 7
    # if b == 7:
    #     raise ZeroDivisionError
    c = a/b
    x = 8
    d = x
    isim = "Ali"
    karakter = isim[2]
#except sıralaması önemli

except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except IndexError:
    print("ali karaktersix")
except Exception:
    print("bilinmeyen hata oluştu")

else:
    print("try da hata yok. else çalışıyor")

finally:
    print("finally hep çalışıyor")

# ?-------------------------------------------------------------------

# try:
#     dosya = open("yazılımbilimi.txt" , "r")
# except IOError:
#     print("Dosya bulunamadı")

# finally:
#     dosya.close()

#?-------------------------------------------------------------------

try:
    i = int(input("Sayı gir: "))
    print(i)
except Exception:
    i = 0
    print(i)

#?-------------------------------------------------------------------

def tam_sayiya_cevir_dongu():

    while True:
        girdi = input("ondalık sayı gir: ")
        status = ''
        try:
            status = "başarılı"
            girdi = float(girdi)
            print(round(girdi))
            break
        except:
            status = "başarısız"
            print("hatalı giriş")
            pass
        finally:
            print("tam sayıya çevirme {}".format(status))
        

tam_sayiya_cevir_dongu()

#?-------------------------------------------------------------------

try:
    [5] + "a"
except TypeError:
    print("yanlış")

#?raise--------------------------------------------------------------

num1 = 0
if num1 == 0:
    raise Exception("Değer 0 olamaz..")
if num1 == 0:
    raise ZeroDivisionError("Değer 0 olamaz..")

num1 = "asd"
if not type(num1) is int:
    raise ValueError("bir sayısal değer giriniz")

num = (input("sd")) #!value error alırız
print(int(num))

#?-------------------------------------------------------------------

while True:
    sayi = input("bir sayı gir")
    
    try:
        sayi = float(sayi)
        print(sayi)
    except ValueError:
        print("hatal")
        pass

# ?SyntaxError: default 'except:' must be last--------
# try:
#     f = open("a.txt" , "w")
#     a = 5
#     b = 0
#     c = a/b
#     f.write(str(c))

# except:
#     print("1.except")

# except IOError:
#     print("cant open file")    

# except ZeroDivisionError:
#     print("not divede 0 ")
