def create_user():
    sayac = 0
    username = input("Kullanıcı Adınızı Oluşturunuz :")
    print("Giriş Yap")
    while sayac < 3:
        while True:
            usr = input("Kullanıcı Adı :")
            if usr == username :
                print("Merhaba", usr)
                sayac += 3
                break
            if usr != username:
                print("Kullanıcı adı hatalı...")
                sayac += 1
                break
create_user()
dersler =input("almak istediğiniz dersleri yazınız:")
a_ders=list (dersler)
bosluk_sayac=0
for i in a_ders:
    if i == " ":
        bosluk_sayac += 1
       #print("boşluk adedi",bosluk_sayac)
         # adet=print(bosluk_sayac+1)
        adet = bosluk_sayac+1
        print(dersler)
if adet <=5 and adet >3 :
    print(dersler)
elif adet < 3:
    print("sınıfta başarısız oldunuz")
    

def notlar():
        while True:
            arasınav = int(input("arasınav notunuzu girin:"))
            final = int (input("finaş notunu girin:"))
            proje = int (input("proje notunu gir:"))
            ort = (arasınav*0.3)+(final*0.5)+(proje*0.2)
            if (ort>90):
                print ("AA",ort)
                break
            elif (ort> 70 and ort <=90):
                print ("BB",ort)
                break
            elif (ort> 50 and ort <=70):
                print ("CC",ort)
                break
            elif (ort> 30 and ort <=50):
                print ("DD",ort)
                break
            else:
                print("DD",ort)
                break
    

notlar()