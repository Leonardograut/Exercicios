"""escreva um codigo que pertmita a leitura das notasde um turma  de 5 alunos e guarde um vetor, calcular 
   a media da turma e  cantar quantos alunos obtiveram nota acima desta  media caculada e escrever a media  da turma  e o resultado da contagem
"""

notas = [0,0,0,0,0]
s = 0
cont =0

for x in range(5):
    notas[x] = float(input(' Digite a nota do aluno : '))
for z in range(5):
    s = s + notas[z]
media = s /5

for y in range(5):
    if notas[y] > media:
        cont = cont +1
print(' A media da sala foi',media,'e',cont,'alunos foram aprovados')        