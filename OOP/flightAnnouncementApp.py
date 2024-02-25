
#! flight announcement application
class Ucus:
    havayolu = "THY"
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def anons_yap(self):
        print(f"{self.kod} sefer sayılı {self.kalkis}-{self.varis} uçağımız {self.sure} dakikalık ucus seferi {self.kapasite} kişilik yolcu kapasitesiyle {self.yolcu} kişi ile uçuşa hazırdır. ")
        return "{} sefer sayılı {}-{} uçuşumuz {} dakika sürecektir.".format(self.kod, 
        self.kalkis, 
        self.varis, 
        self.sure)

ucus2 = Ucus("TK123", "IST", "ANK", 60, 300, 50)
ucus3 = Ucus("TK223", "BOD", "ANT", 40, 250, 250)
print(ucus3.anons_yap())
# ucus1 = Ucus()
# print(ucus3.havayolu)
# print(ucus2.havayolu)
