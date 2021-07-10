class Asker:
    def __init__(self,isim,guc,can,dayanlıklılık,hız,kudret):
        self.isim = isim
        self.guc = guc
        self.can = can
        self.dayanıklılık = dayanlıklılık
        self.hız = hız
        self.kudret = kudret

    def __str__(self):
        return(f"Asker Adı: {self.isim}") 

    def Ultimate(self):
        print(f"{self.isim}, Ultimate Hazır!!!") 

    
class Piyade(Asker):
    def __init__(self, isim, guc, can, dayanlıklılık, hız, kudret, kaba_kuvvet):
        super().__init__(isim, guc, can, dayanlıklılık, hız, kudret)
        self.kaba_kuvvet = kaba_kuvvet
        print(f"Piyadenin Adı: {self.isim}, Gücü: {self.guc}, Canı: {self.can}, Dayanıklılığı: {self.dayanıklılık}, Hızı: {self.hız}, Kudret Puanı: {self.kudret}")
        print(f"Ultimate {self.kaba_kuvvet}!")

class Suvari(Asker):
    def __init__(self, isim, guc, can, dayanlıklılık, hız, kudret, kudretli_saldiri):
        super().__init__(isim, guc, can, dayanlıklılık, hız, kudret)
        self.kudretli_saldiri = kudretli_saldiri
        print(f"Suvarinin Adı: {self.isim}, Gücü: {self.guc}, Canı: {self.can}, Dayanıklılığı: {self.dayanıklılık}, Hızı: {self.hız}, Kudret Puanı: {self.kudret}")
        print(f"Ultimate {self.kudretli_saldiri}!")

class Okcu(Asker):
    def __init__(self, isim, guc, can, dayanlıklılık, hız, kudret,zehirli_ok):
        super().__init__(isim, guc, can, dayanlıklılık, hız, kudret)
        self.zehirli_ok = zehirli_ok
        print(f"Okcunun Adı: {self.isim}, Gücü: {self.guc}, Canı: {self.can}, Dayanıklılığı: {self.dayanıklılık}, Hızı: {self.hız}, Kudret Puanı: {self.kudret}")
        print(f"Ultimate {self.zehirli_ok}!")

class Gozcu(Asker):
    def __init__(self, isim, guc, can, dayanlıklılık, hız, kudret, kılık_degistirme):
        super().__init__(isim, guc, can, dayanlıklılık, hız, kudret)
        self.kılık_degistirme = kılık_degistirme
        print(f"Gozcunun Adı: {self.isim}, Gücü: {self.guc}, Canı: {self.can}, Dayanıklılığı: {self.dayanıklılık}, Hızı: {self.hız}, Kudret Puanı: {self.kudret}")
        print(f"Ultimate {self.kılık_degistirme}!")

class Bombaci(Asker):
    def __init__(self, isim, guc, can, dayanlıklılık, hız, kudret,dinamit):
        super().__init__(isim, guc, can, dayanlıklılık, hız, kudret)
        self.dinamit = dinamit
        print(f"Bombacının Adı: {self.isim}, Gücü: {self.guc}, Canı: {self.can}, Dayanıklılığı: {self.dayanıklılık}, Hızı: {self.hız}, Kudret Puanı: {self.kudret}")
        print(f"Ultimate {self.dinamit}!")



Soldier1 = Asker("Asker",120,120,130,150,20)
#Piyade = Piyade("Kudretli Kral",150,220,100,150,50,'Aktif')
#Suvari = Suvari("Atlı Süvari",130,200,120,300,50,'Aktif')
#Okcu =  Okcu("Kraliçe Okçu",110,160,80,120,50,'Aktif')
#Gözcü = Gozcu("İstihbaratçı",30,100,40,400,10,'Aktif')
#Bombacı = Bombaci("Tahrip Ustası",50,150,35,200,20,'Aktif')
#Piyade.Ultimate()
#Soldier1.Ultimate()

