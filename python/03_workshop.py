class matematik():
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def topla(self):
        return self.sayi1 + self.sayi2
    def cıkar(self):
        return self.sayi1 - self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2
    
matematik1 = matematik(2,78)


print("toplam = " + str(matematik1.topla()) )

class Person():
    def __init__(self,firstNAme,lastName,Age ):
        self.firstName = firstNAme
        self.lastName = lastName
        self.Age =Age

dosya = open("bilgiler.txt", "a", encoding="utf-8"  )

dosya.write(" \n ")
dosya.write("AHMET RIZA OFLAZ")

dosya.close()