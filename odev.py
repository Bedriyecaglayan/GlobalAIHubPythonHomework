d1 = input("1.değeri giriniz:")
print(" {} " .format(d1) )
print(type (d1))
d2 = input("2.değeri giriniz:")
print(f' {d2} ')
print(type(d2))
d3 = input("3.değeri giriniz:")
print(" {} ".format(d3) )
print(type(d3))
d4 = input("4.değeri giriniz:")
print(f' {d4} ')
print(type(d4))
d5 = input("5.değeri giriniz:")
print(" {} ".format(d5))
print(type(d5))

# girilen bütün değerleri yazdıran format komutu

print ("girdiğiniz değerler: {} {} {} {} {} ".format(d1,d2,d3,d4,d5))

#girilen tüm değerleri f-string komutu ile yazdırma işlemi

print (f' girdiğiniz değerler {d1,d2,d3,d4,d5} ' )