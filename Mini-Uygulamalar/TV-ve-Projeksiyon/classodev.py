class Televizyon:
    def __init__(self):
        self.acik = False
        self.ses_seviyesi = 50
        self.kanallar = ["TRT", "Show", "Fox", "Kanal D", "Star"]
        self.aktif_kanal = 0
    
    def ac(self):
        if not self.acik:
            self.acik = True
            print("TV açıldı")
        else:
            print("TV zaten açık")
    
    def kapat(self):
        if self.acik:
            self.acik = False
            print("TV kapatıldı")
        else:
            print("TV zaten kapalı")
    
    def ses_ayari(self):
        if self.acik:
            try:
                ses = int(input("Ses seviyesi (0-100): "))
                if 0 <= ses <= 100:
                    self.ses_seviyesi = ses
                    print("Ses ayarlandı")
                else:
                    print("Geçersiz ses seviyesi")
            except:
                print("Sayı girmelisiniz")
        else:
            print("Cihaz kapalıyken ses ayarı yapılamaz")
    
    def kanal_ekle(self):
        if self.acik:
            kanal = input("Yeni kanal adı: ")
            self.kanallar.append(kanal)
            print("Kanal eklendi")
        else:
            print("Cihaz kapalıyken kanal eklenemez")
    
    def kanal_degistir(self):
        if self.acik:
            print("Mevcut kanallar:")
            for kanal in self.kanallar:
                print(kanal)
            
            kanal = input("Geçmek istediğiniz kanal: ")
            if kanal in self.kanallar:
                self.aktif_kanal = self.kanallar.index(kanal)
                print("Kanal değiştirildi")
            else:
                print("Kanal bulunamadı")
        else:
            print("Cihaz kapalıyken kanal değiştirilemez")
    
    def bilgileri_goster(self):
        print("""
        Cihaz Bilgileri:
        
        Durum: {}
        
        Ses Seviyesi: {}
        
        Aktif Kanal: {}
        
        Kanallar: {}
        """).format(
            "Açık" if self.acik else "Kapalı",
            self.ses_seviyesi,
            self.kanallar[self.aktif_kanal],
            ", ".join(self.kanallar)
        )
    def tv_kumanda():
        tv = Televizyon()
    
        while True:
            print("\nTV KUMANDASI")
            print("1. Aç")
            print("2. Kapat")
            print("3. Ses Ayarı")
            print("4. Kanal Ekle")
            print("5. Kanal Değiştir")
            print("6. Bilgileri Göster")
            print("q. Çıkış")
            
            secim = input("Seçiminiz: ")
            
            if secim == "1":
                tv.ac()
            elif secim == "2":
                tv.kapat()
            elif secim == "3":
                tv.ses_ayari()
            elif secim == "4":
                tv.kanal_ekle()
            elif secim == "5":
                tv.kanal_degistir()
            elif secim == "6":
                tv.bilgileri_goster()
            elif secim == "q":
                print("TV kumandası kapatılıyor")
                break
            else:
                print("Geçersiz seçim")

class Projeksiyon(Televizyon):
    def __init__(self):
        super().__init__()
        self.goruntu_kaynaklari = ["HDMI", "USB", "VGA"]
        self.aktif_kaynak = 0
        self.parlaklik = 50
    
    def kaynak_degistir(self):
        if self.acik:
            print("Görüntü kaynakları:")
            for kaynak in self.goruntu_kaynaklari:
                print(kaynak)
            
            kaynak = input("Geçmek istediğiniz kaynak: ")
            if kaynak in self.goruntu_kaynaklari:
                self.aktif_kaynak = self.goruntu_kaynaklari.index(kaynak)
                print("Görüntü kaynağı değiştirildi")
            else:
                print("Geçersiz kaynak")
        else:
            print("Cihaz kapalıyken kaynak değiştirilemez")
    
    def parlaklik_ayari(self):
        if self.acik:
            try:
                parlaklik = int(input("Parlaklık seviyesi (0-100): "))
                if 0 <= parlaklik <= 100:
                    self.parlaklik = parlaklik
                    print("Parlaklık ayarlandı")
                else:
                    print("Geçersiz parlaklık seviyesi")
            except:
                print("Sayı girmelisiniz")
        else:
            print("Cihaz kapalıyken parlaklık ayarı yapılamaz")
    
    def bilgileri_goster(self):
        print("""
        Projeksiyon Bilgileri:
        
        Durum: {}
        
        Ses Seviyesi: {}
        
        Aktif Kanal: {}
        
        Kanallar: {}
        
        Görüntü Kaynağı: {}
        
        Parlaklık: {}
        """.format(
            "Açık" if self.acik else "Kapalı",
            self.ses_seviyesi,
            self.kanallar[self.aktif_kanal],
            ", ".join(self.kanallar),
            self.goruntu_kaynaklari[self.aktif_kaynak],
            self.parlaklik)
        )



def projeksiyon_kumanda():
    projeksiyon = Projeksiyon()
    
    while True:
        print("\nPROJEKSİYON KUMANDASI")
        print("1. Aç")
        print("2. Kapat")
        print("3. Ses Ayarı")
        print("4. Kaynak Değiştir")
        print("5. Parlaklık Ayarı")
        print("6. Bilgileri Göster")
        print("q. Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            projeksiyon.ac()
        elif secim == "2":
            projeksiyon.kapat()
        elif secim == "3":
            projeksiyon.ses_ayari()
        elif secim == "4":
            projeksiyon.kaynak_degistir()
        elif secim == "5":
            projeksiyon.parlaklik_ayari()
        elif secim == "6":
            projeksiyon.bilgileri_goster()
        elif secim == "q":
            print("çıkılıyor...")
            break
        else:
            print("Geçersiz seçim")

# Ana program
while True:
    print("\nANA MENÜ")
    print("1. TV Kumandası")
    print("2. Projeksiyon Kumandası")
    print("q. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        Televizyon.tv_kumanda()
    elif secim == "2":
        projeksiyon_kumanda()
    elif secim == "q":
        print("Program sonlandırılıyor")
        break
    else:
        print("Geçersiz seçim")