def mukemmelsayi(sayi):
    boltoplam = 0
    for i in range(1,sayi):
        if sayi % i == 0:
            boltoplam+= i
    if boltoplam == sayi:
        print(sayi,"Mükemmel Sayıdır. Bölenlerin Toplamı",boltoplam)
    else:
        print(sayi,"Mükemmel Sayı Değildir")    



mukemmelsayi(12)