def kayit():
    kayit = open("rehber.txt","a",encoding="utf-8")
    ad = input("Adınızı giriniz:")
    soyad = input("Soyadınızı giriniz:")
    telefon = input("Telefon Numaranızı Giriniz")
    kayit.write(ad+soyad+str(telefon)+"\n")
    kayit.close()
def goster():
    goster = open("rehber.txt","r",encoding="utf-8")
    for satir in goster:
        print(satir.strip())

    
while True:
    print("""1-Kayıt Gir 
             2-Kayıt Gör
             3-Farklı bir tuşa basın
          """)
    islem = input("Yapmak İstediğiniz İşlemi Seçin")
    if islem == "1":
        kayit()
    elif islem =="2":
        goster()
    else:
        print("Programdan çıkılıyor")
        break