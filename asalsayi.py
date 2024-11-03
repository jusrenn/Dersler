"""
Asalsayi bulan program yazin.
"""
sayi = int(input("Lutfen bir sayi girin: "))

i = 2
while i < sayi:
    if sayi % i == 0:
        print(f"{sayi}, {i} bolunuyor. Bu yuzden bir asalsayi degildir")
        break
    i += 1
    if i == sayi:
        print(f"{sayi} bir asal sayidir!")