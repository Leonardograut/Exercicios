
nota1 = int(input("Digite a nota1 do usuario"))
nota2 = int(input("Digite a nota2 do usuario"))

while nota1 > 10 or nota1 < 0:
    nota1 = int(input("Digite a nota2 do usuario"))
while nota2 > 10 or nota2 < 0:
    nota2 = int(input("Digite a nota2 do usuario"))
media = (nota1 + nota2) / 2
print(media)


'''escreva um codigo para ler as notas de  1 a  2 , avaliaçoes de um aluno calcule
 e imprima a media desse aluno, so devem ser aceitos valores validos, durante a leitura,(0 a 10) para cada nota.'''
