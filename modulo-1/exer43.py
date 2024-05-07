"""Faça um codigo para ler 5 numeros e armazenar em um vetor. apos a leitura , 
total dos  5 numeros, o codigo deve escrever  esses  5 numeros lidos  na ordem inversa"""


vetor1 = [0,0,0,0,0]
vetor2=[0,0,0,0,0]

for x in range(5):
    vetor1[x] = int(input('Digite um numero '))

for z in range(4,-1,-1):
    print(vetor1[z],end=" ")    