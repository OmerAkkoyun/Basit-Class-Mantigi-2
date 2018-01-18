class Bilgisayar():
    def __init__(self,pcdurum="kapalı",pcram="8GB",pcislemci="i7_4700MQ",pcekrankart="Nvidia GTX 765M"):
        self.pcdurum=pcdurum
        self.pcram=pcram
        self.pcislemci=pcislemci
        self.pcekrankart=pcekrankart

    def __str__(self):
        print("""
        Sistem Özelikleri
        
        Pc Durumu= {}
        
        PC Ram = {}
        
        PC İşlemci = {}
        
        Pc Ekran Kartı = {}
        
        
        """.format(self.pcdurum,self.pcram,self.pcislemci,self.pcekrankart))
pc=Bilgisayar()

print(pc)
