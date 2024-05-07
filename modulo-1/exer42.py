"""preencher um vetor A com 10 numeros, logo em seguida  ler mais um numero e guarda em uma variavel X
  Armazenar em um vetor M o resultado  dde  cada elemento  e A multiplicacao pelo valor X, no final do vetor
"""

vetorA = [0,0,0,0,0,0,0,0,0,0]
vetorB = [0,0,0,0,0,0,0,0,0,0]

for x in range(0,10):
    vetorA[x] = int(input(" Digite um numero "))

X = int(input(" Digite o multiplicador "))

for z in range(10):
    vetorB[z] = vetorA[z]* X

    print(vetorA)
    print(X) 
    print(vetorB)
  
   