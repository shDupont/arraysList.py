quantidade = int(input("Digite o número desejado:"))

def funcao4(linhas):
  for linha in range(0,linhas+1,1):
    for preencher in range(1,linha+1,1):
      if preencher!=linha:
        print(preencher, ",", end=" ") 
      else:
        print(preencher)
print(funcao4(quantidade))