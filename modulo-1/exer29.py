
soma = 0
for x in range(2):
  num = float(input("digite um numero"))
  soma = soma +num

media = soma/2

if media >= 7:
   print('aprovado com ',media)
elif media >=4:
    print('Recuperacao',media)
else:
    print("Reprovado",media)



