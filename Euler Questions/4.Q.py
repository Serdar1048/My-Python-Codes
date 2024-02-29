
#todo hangi 3 basamaklı iki sayının çarpımı en büyük polindrom sayıyı verir
def is_polidrom(n):
    # r = str(n)[::-1]
    r = ""
    for i in range(len(str(n))-1,-1,-1):
        r += (str(n)[i])
    
    if str(n) == r:
        return True
    else:
        return False
print(is_polidrom(323))

def multi():
    biggest_number = 0
    for x in range(100,1000):
        for y in range(100,1000):
            multiplaction = x*y
            if is_polidrom(multiplaction) and multiplaction> biggest_number:
                    biggest_number = multiplaction
    return biggest_number, x, y
print(multi())