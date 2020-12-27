ad = str (input("adınız:"))
soyad =str(input("soyadınız:"))
yas = int (input("yasınız:"))
dtarih = int (input("doğum tarihiniz (yıl):"))
all = [ad,soyad,yas,dtarih]
print(all)
if yas < 18 :
    print("dışarı çıkamazsınız çok tehlikeli.")
else:
    print("sokağa çıkabilirsiniz.")