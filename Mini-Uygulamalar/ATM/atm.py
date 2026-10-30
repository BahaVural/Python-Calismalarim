bakiye = 10000
cikis = "q"

while True:
    print("""
    1-PARA ÇEKME
    2-PARA YATIRMA
    3-BAKİYE SORGULAMA
    """)
    islem = input("YAPMAK İSTEDİĞİNİZ İŞLEMİ GİRİNİZ(Çıkmak için q giriniz):")  

    if islem == "1":
        tutar = int(input("HESABINIZDAN NE KADAR ÇEKMEK İSTİYORSUNUZ:"))
        if tutar > bakiye:
            print("HESABINIZDA BU KADAR PARA YOK!!")
        else:
            bakiye -= tutar
            print("İŞLEM BAŞARILI!!!")
            print("Güncel bakiyeniz:", bakiye)
    elif islem == "2":
        tutar = int(input("HESABINIZA NE KADAR YATIRMAK İSTİYORSUNUZ:"))
        bakiye += tutar
        print("İŞLEM BAŞARILI!!!")
        print("Güncel bakiyeniz:", bakiye)
    elif islem == "3":
        print("HESABINIZDAKİ GÜNCEL BAKİYE:", bakiye)
    elif islem == "q":
        print("KARTINIZ GERİ VERİLİYOR...")
        break
    else:
        print("Geçersiz işlem.")
