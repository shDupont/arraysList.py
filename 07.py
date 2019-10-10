import random
import numpy

vetor = []
soma = 0
mult = 0
count = random.randint(0,10)

for i in range(5):
  vetor.append(count)
soma = sum(vetor)
mult = numpy.prod(vetor)


print(vetor)
print(soma)
print(mult)