"""crie um array tamanho 5 e preencher com os nomes dos
 5alunos informados pelo usuario com pyhton e imprimir  todas as posicao de cada"""


nome = ['','','','','']

for x in range (5):
    nome[x] = (input('Digite o seu nome '))
for z in range (5):
    print('Nome :',nome[z],'na posiçao',z)