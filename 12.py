quantidade = int(input("Digite o número desejado:"))

def funcao2(quantidade):
  for x in range(0,quantidade,1):
    if x == 0:
      print("*")
    elif x < quantidade-1:
      print("*" + " " * (x-1) +"*")
    else:
      print("*" * (x+1))
  print("\n")
print(funcao2(quantidade))