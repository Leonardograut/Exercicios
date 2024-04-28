"""Escreva um algoritmo para ler o 
número total de eleitores de um 
município, o número de votos brancos, 
nulos e válidos. Calcular e escrever o 
percentual que cada um representa em 
relação ao total de eleitores.
"""


eleitores= int(input('Digite o numero de eleitores:'))
validos =0
nulo = 0
brancos = 0


for x in range  (eleitores):
    voto = int(input('Vote:[1]-Maria , [2]-Jose, [3]-Lampiao, [4]-Nulo'))
    if voto ==1  or voto == 2 or voto == 3:
        validos = validos + 1

    elif voto == 4:
          nulo = nulo + 1
    else:
         brancos = brancos + 1 

porcentagemV = (validos/eleitores)*100 
porcentagemN = (nulo/eleitores)*100   
porcentagemB = (brancos/eleitores)*100   


print('Porcentagem de votos validos',porcentagemV)
print('Porcentagem de votos nulos',porcentagemN)
print('Porcentagem de votos brancos',porcentagemB)
