num =0
while num !=3 :
 num = int(input('Digite 1 para area do triangulo e  2 para Area do Quadrado e Digite 3 para  sair do sistema'))
 if num == 1:
  base = int(input('Insira o valor do triangulo'))
  altura = int(input("Insira o valor da altura:"))
  triangulo = (base*altura)/2
  print("o valor  do triangulo ",triangulo)

 elif num == 2:
  base = int(input('Insira o valor do quadrado'))
  quadrado = base **2
  print("area do quadrado",quadrado)

 elif num > 3:
   print("Opcao invalida")


"""faça um codigo que receba o valor da base e da aultra 
de um triangulo e calcule a sua area usando a formula A =(basexAltura)/2


"""