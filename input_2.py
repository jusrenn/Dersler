# ==
# >
# <
# <=
# >=
# or
# and
# ! => Tersini yapar

# sayi1 = int(input("Bir sayi girin: "))
# sayi2 = int(input("Bir sayi daha girin: "))

# if sayi1 < sayi2:
#     print(f"{sayi2}, {sayi1}'den buyuktur.")
# elif sayi1 > sayi2:
#     print(f"{sayi1}, {sayi2}'den buyuktur.")
# else:
#     print(f"{sayi1} ve {sayi2} birbirine esittir.")

hayvan = input("Bir hayvan girin: ")
isim = input("Bir isim girin: ")

if hayvan == "köpek" or isim == "comar":
    print("bu bir köpektir!")
elif hayvan == "kus" and isim == "angut":
    print("beni tanidilar siz kacin!")
else:
    print("Böyle bir hayvan yok")