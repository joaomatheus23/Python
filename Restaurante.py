print("Ola Boa Noite")
Pratos = ['Feijoada', 'Parmegiana', 'Strogonoff']
PrecoPratos = [30,40,35]
print("Escolha um prato: ")
for i in range (0,3):
  print("Prato " + str(i) + ": ", Pratos[i] , "R$" + str(PrecoPratos[i]))
PratoEscolhido = int(input("Escolha o prato : "))
ValorPrato = PrecoPratos[PratoEscolhido]
print(Pratos[PratoEscolhido])

Bebidas = ['Coca-Cola', 'Guarana', 'Fanta Laranja']
PrecoBebidas = [5,5,5,]
print("Escolha uma bebida: ")
for i in range(0,3):
  print("Bebida " + str(i) + ": ", Bebidas[i] , "R$" + str(PrecoBebidas[i]))
BebidaEscolhida = int(input("Escolha sua bebida: "))
ValorBebida = PrecoBebidas[BebidaEscolhida]
print(Bebidas[BebidaEscolhida])

Sobremesas = ['Brigadeiro', 'Beijinho', 'Pudim']
PrecoSobremesa = [10,12,15]
print("Escolha sua sobremesa")
for i in range(0,3):
  print("Sobremesa " + str(i) + ": ", Sobremesas[i] , "R$" + str(PrecoSobremesa[i]))
SobremesaEscolhida = int(input("Escolha sua sobremesa: "))
ValorSobremesa = PrecoSobremesa[SobremesaEscolhida]
print(Sobremesas[SobremesaEscolhida])

ValorTotal = ValorPrato + ValorBebida + ValorSobremesa
print("Sua conta ficou: R$", ValorTotal)
