import random
array = []
naipes = ["Ouros","Copas","Espadas","Paus"]

for naipe in range (0,3,1):
  for cartas in range (0,14,1):
    if cartas > 0 and cartas < 11:
      array.extend([[cartas, " de ", naipes[naipe]]])
    elif cartas == 11:
      array.extend([["J de", naipes[naipe]]])
    elif cartas == 12:
      array.extend([["Q de", naipes[naipe]]])
    elif cartas == 13:
      array.extend([["K de", naipes[naipe]]])
    else:
      array.extend([["A de", naipes[naipe]]])
print(array, "\n")
random.shuffle(array)
print(array)