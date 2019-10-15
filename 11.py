quantidade = int(input("Digite o número desejado:"))

def funcao(quantidade):
  for x in range(0,quantidade,1):
    print("*" * (x+1))
  print("\n")
print(funcao(quantidade))
    