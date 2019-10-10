import random

array = []
vetorPar = []
vetorImpar = []

for i in range(19):
  count = random.randint(0,10)
  array.append(count)
  if count % 2 == 0:
    vetorPar.append(count)
  else:
    vetorImpar.append(count)


print(array)
print(vetorPar)
print(vetorImpar)