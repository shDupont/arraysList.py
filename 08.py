idades = []
alturas = []
alturas_inv = []
idades_inv = []

for i in range(5):
  idades.append(int(input("Digite sua idade: ")))
  alturas.append(float(input("Digite sua altura: ")))

alturas_inv = alturas[::-1]
idades_inv = idades[::-1]


print(idades)
print(alturas)
print(idades_inv)
print(alturas_inv)