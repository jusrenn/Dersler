sepet = ["elma", "armut", "cilek", "kivi"]

print(type(sepet))
print(sepet[0])
# elma = sepet[0]
# print(elma)

sepet.append("karpuz")
print(sepet)

sepet.remove("armut")
print(sepet)

print(len(sepet))
print(sepet[0:2])
print(sepet[1:3])
print(sepet[2:])
print(sepet[::-1])

if "elma" in sepet:
    print("Var")
else:
    print("yok")