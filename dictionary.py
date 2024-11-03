# Anahtar ve deger
# Key value

person = {
    "name" : "Yusuf",
    "lastname" : "Renkoglu",
    "age" : 40
    }

print(type(person))
print(person)
print(f"{person['name']} {person['lastname']}")

# Dictionary'den eleman cikartmak
person.pop("name")
print(person)

person["human"] = "Evet"
print(person)
