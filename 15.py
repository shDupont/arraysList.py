#Programa de eleição:

candidatos = ["1","2","3","4","5","6"]
votos = []
maiorVoto = 0

while True:
  voto = int(input("Digite um número: "))
  if voto not in range(0, 8):
    print('Voto inválido!')
  elif voto == 0:
    break
  else:
    votos.append(voto)

for i in range(1,5):
  print("Candidato: ", i, ": ", votos.count(i), " votos.")


print("Núumero de nulos: ", votos.count(6))
print("Número de brancos: ", votos.count(7))