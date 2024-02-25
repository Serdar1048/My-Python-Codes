
import random

class dusman:
    def __init__(self, isim="Dusman", kalan_can=500, saldiri_gucu=10, mermi_sayisi=5):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim + " saldırıyor.")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi) + " mermi harcandı")
        self.mermi_sayisi -= harcanan_mermi
        
        return(harcanan_mermi, self.saldiri_gucu)
    
    def saldiriya_ugra(self,harcanan_mermi, saldiri_gucu):
        print("vuruldum")
        self.kalan_can -= (harcanan_mermi * saldiri_gucu)

    def mermi_bitti_mi(self):
        if self.mermi_sayisi<=0: #mermi bitti
            print(self.isim + " Konuşuyor: mermim bitti")
            return True
        else:
            return False
        
    def hayatta_mi(self):
        if self.kalan_can<=0:
            print("ölüyorummmmm...")

    def print(self):
        print("basılıyor....")
        print("isim:", self.isim, " kalan can:", self.kalan_can, " saldırı gücü:", self.saldiri_gucu, " mermi sayısı:",self.mermi_sayisi)

dusmanlar = []
i=0
while i<10:
    rastgele_can = random.randrange(100,200)
    rastgele_saldiri_gucu = random.randrange(10,20)
    rastgele_mermi = random.randrange(20,30)
    yeni_dusman =  dusman("dusman " + str(i+1) , rastgele_can, rastgele_saldiri_gucu,rastgele_mermi)
    dusmanlar.append(yeni_dusman)
    i+=1

i=0
while i<3:
    random_dusman1 = dusmanlar[0] #saldırcak
    random_dusman2 = dusmanlar[1] #savuncak
    random_dusman1.print()
    random_dusman2.print()
    donen_deger = random_dusman1.saldir() # (15,5)

    random_dusman2.saldiriya_ugra(donen_deger[0],donen_deger[1])
    random_dusman2.hayatta_mi()
    random_dusman1.mermi_bitti_mi()
    
    print("round bitti")
    i+=1
