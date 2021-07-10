class Krallık:
    def __init__(self,nufus,duvar_hp,uretim,kaynaklar,askerler):
        self.nufus = nufus
        self.uretim = uretim
        self.kaynaklar = kaynaklar
        self.askerler = askerler
        self.duvar_hp = duvar_hp
    
    def __str__(self):
        return f"Köyün nüfusu: {self.nufus}, Saatlik Kaynak Üretimi: {self.uretim}, Depolar {self.kaynaklar} kaynak ile dolu. Askerler Savaşa Hazır: {self.askerler}  Duvar sağlığı {self.duvar_hp}!"
       
               
    def DuvarSaglik(self):         
        if self.duvar_hp > 75:
            print(f"Duvar Sağlığı :{self.duvar_hp}. Duvarlarımız sağlam görünüyor!")
        else:
            print(f"Duvar sağlığı :{self.duvar_hp}. Duvarlarmızın onarıma ihtiyacı var!")
    
    def Kaynaklar(self):
        if self.kaynaklar <= 10000 and self.kaynaklar >= 7500:
            print(f"Kaynaklarımız : {self.kaynaklar} seviyesinde ve depolarımızın ağzına kadar dolu")

        elif self.kaynaklar <= 7500 and self.kaynaklar >= 6000:
            print(f"Kaynaklarımız: {self.kaynaklar} seviyesinde ve depolarımız dolu görünüyor")
        
        else:
            print(f"Kaynaklarımız: {self.kaynaklar} seviyesinde.Üretimi arttırmamız gerekiyor. Depolar boşalmak üzere")
            
    def KöyünGenelDurumu(self):
        print(f"Köyün nüfusu: {self.nufus}, Saatlik Kaynak Üretimi: {self.uretim}, Depolar {self.kaynaklar} kaynak ile dolu. Askerler Savaşa Hazır: {self.askerler}  Duvar sağlığı {self.duvar_hp}! ")    
        

T1 = Krallık(1200,70,1500,6000,1200)



T1.DuvarSaglik()
T1.Kaynaklar()
T1.KöyünGenelDurumu()