import random

sonuclar = set()
amount = int(input("Please type a number: "))

i = 0
while i < amount:
    while len(sonuclar) < 6:
        sayi = random.randint(1,49)
        sonuclar.add(sayi)

    print(sonuclar)
    sonuclar.clear()
    i += 1