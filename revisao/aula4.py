"""Crie um algoritmo que receba 3 
números e informe qual o maior entre 
eles"""

resposta = 's'

while resposta =='s' or resposta =='S':

  n1 = int(input(" Digite o primeiro nuemero "))
  n2 = int(input(" Digite o segundo nuemero "))
  n3 = int(input(" Digite 3 terceiro nuemero "))

  if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior")

  elif n2 >n1 and n2>n3:
    print(f"{n2} é o maior")
  else:
    print(f"{n3} é o maior")    


  resposta = str(input("Você deseja tentar novamente ?"))       
 