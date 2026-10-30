faktoriyel = 1
sayi = int(input("Hesaplamak istediğiniz sayıyı giriniz: "))
    
if sayi == 0:
        print("1")
elif sayi < 0:
        print("Sayı Negatif Olamaz !!")
else:
        for i in range(1, sayi + 1):
            faktoriyel *= i
        print(sayi,"sayısının faktoriyeli:",faktoriyel,"!")