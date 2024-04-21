"""Faça um código que receba as 3 notas de um aluno e
verifique se ele está aprovado ou reprovado.
Considere que a média para aprovação é 7,0 caso sua média
seja menor que 7,0 e maior que 4,00 fica  em recuperacao"""

num1 = float(input('Digite a primeiro nota'))
num2 = float(input('Digite a segundo nota'))
num3 = float(input('Digite a terceira nota'))

media = (num1+num2+num3)/3

if media >=7:
    print("aluno aprovado com media:",media)

elif media >=4:
    print("aluno em recuperacao",media)
else:
    print("Aluno Reprovado com media ",media)