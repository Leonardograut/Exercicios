"""Faça um programa para calcular a média de 2 notas e
mostrar essa média e o nome do aluno."""

nome= input('Digite seu nome ')
nota1 = int(input(" Digite a primeira nota do aluno: "))
nota2 = int(input(" Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2


print(f'A média do aluno {nome} é {media}')