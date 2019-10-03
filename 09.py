import random
a = []

resultado = 0
quadrado = 0
soma = 0
for i in range(10):
  count = random.randint(0,10)
  print(count)
  a.append(count)
  quadrado = count * count
  soma += quadrado
print(soma)