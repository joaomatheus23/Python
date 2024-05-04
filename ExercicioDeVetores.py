Vetor1 = [0]*10
Vetor2 = [0]*10
Vetor3 = [0]*10

for i in range(0,10):
  Vetor1[i] = int(input("Digite o " + str(i) + " Valor: "))

for i in range(0,10):
  Vetor2[i] = int(input("Digite o " + str(i) + " Valor "))

for i in range(0,10):
  Vetor3[i] = Vetor1[i] + Vetor2[i]
  print(str(i) + " Valor ", Vetor3[i])
