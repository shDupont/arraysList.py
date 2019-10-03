alunos = ["a","b","c","d","e","f","g","h","i","j"]
alunosSete = 0
medias = []
notas = []
media = 0
for i in range(10):
  for x in range(4):
    notas.append(int(input("Nota: ")))
  media = sum(notas) / 4
  if media >= 7:
    alunosSete += 1
  print(media)
  medias.append(media)
  notas.clear()