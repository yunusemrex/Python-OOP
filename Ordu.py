import time


class Ordu:
    def __init__(self,okcu,piyade,suvari,gozcu,bombacı):
        self.okcu = okcu
        self.piyade = piyade
        self.suvari = suvari
        self.gozcu = gozcu 
        self.bombacı = bombacı 

    def İçtima(self):
        print(f"Ordumuz: {self.okcu} Okçu, {self.piyade} Piyade, {self.suvari} Suvari, {self.gozcu} Gozcu, {self.bombacı} Bombacı ile emirlerinize hazırdır.")

    def AskerEgit(self):        
        egitim = input("Eğitmek istediğiniz askeri birlik türünü seçiniz: ")
        Birlik_sayisi = input("Eğitmek istediğiniz birlik sayisini seçiniz: ")

        print(f"Ordumuz: {self.okcu} okçu, {self.piyade} piyade, {self.suvari}, {self.gozcu} gozcu, {self.bombacı} bombacı ile emirlerinize hazırdır.")
        
        if egitim == "piyade":
            self.piyade += int(Birlik_sayisi)
            print(f"{Birlik_sayisi} Piyade eğitildi")

        elif egitim == "suvari":
            self.suvari += int(Birlik_sayisi)
            print(f"{Birlik_sayisi} Suvari eğitildi")

        elif egitim == "okcu":
           self.okcu += int(Birlik_sayisi)
           print(f"{Birlik_sayisi} Okçu eğitildi")
        
        elif egitim == "gozcu":
            self.gozcu += int(Birlik_sayisi)
            print(f"{Birlik_sayisi} Gözcü eğitildi")
        
        else:
            self.bombacı += int(Birlik_sayisi)
            print(f"{Birlik_sayisi} Bombacı eğitildi")

        print(f"Ordumuz: {self.okcu} Okçu, {self.piyade} Piyade, {self.suvari} Suvari, {self.gozcu} Gozcu, {self.bombacı} Bombacı ile emirlerinize hazırdır.")

    def GozcuGonder(self):
        Hedef = input("Hakkında istihbarat toplamak istediğiniz Krallığın kordinatlarını girin!")
        time.sleep(3)
        print("-"*10,"Kumandamın gözcü birlikler hazırlanıyor!")
        time.sleep(3)
        print("*"*10)
        print("-"*10,"Gözcü birlikler yola çıktı!")
        time.sleep(3)
        print("*"*10)
        print("-"*10,"Gözcü birlikler geri döndü!!")
        time.sleep(3)
        print("*"*10)
        print("-"*10,"İstihbarat Raporunu İnceleyebilirsiniz")




A1 = Ordu(120,130,140,150,160)
A1.İçtima()
A1.AskerEgit()
A1.GozcuGonder()



