# isim = input("Isim: ")
# print(isim)

# sayi1 = input("Bir sayi girin: ")
# sayi2 = input("Bir sayi daha girin: ")

# print(int(sayi1) + int(sayi2))

sayi1 = int(input("Bir sayi girin: "))
sayi2 = int(input("Bir sayi daha girin: "))

islem = input("Hangi dört islemi gerceklestirmek istiyorsun (+, -, /, *): ")

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "/":
    sonuc = sayi1 / sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
else:
    print("gecersiz karakter girildi!")

try:
    print("Sonuc: " + str(sonuc))
except:
    print("Bir hata olustu!")


