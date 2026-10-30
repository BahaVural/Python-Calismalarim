a = int(input("Birinci Sayıyı Giriniz:"))
b = int(input("İkinci Sayıyı Giriniz:"))
c = int(input("Üçüncü Sayıyı Giriniz:"))

if a <= b and a <= c:
    a = a
elif b <= a and b <= c:
    a,b=b,a
else:
    a,b,c =c,b,a
print(a,"<",b,"<",c)
