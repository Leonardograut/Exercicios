"""Ler o nome de 2 times e o número de gols 
marcados na partida (para cada time). 
Escrever o nome do vencedor. Caso não 
haja vencedor deverá ser impressa a 
palavra EMPATE"""


santacruz= (input('Digite a primeiro time'))
time1 = int(input('Digite a quantidade de gols time'))

sport =(input('Digite o seugndo time'))
time2 = int(input('Digite o segundo time'))

if time1 > time2:
    print("time 1 vencedor","com quantidades de  gols : ",time1, santacruz)
elif time1 == time2:
    print("time empatados",time1,time2)

elif time2 >time1:
    print("time 2 vencedor","com quantidades de  gols : ",time2 ,sport)

else:

    print("ninguem ganhou nem perdeu")