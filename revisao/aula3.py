"""Crie um código que leia a idade de 
uma pessoa e diga em qual ano ela 
nasceu e 
coloque uma condiçao para  saber  se ele fez aniversario ou nao
"""
idade = int(input(' digite a sua idade '))
anoAtual = 2024

niver = input('Ja fez a aniversario ?')

if niver == 's' or niver == "S":
    anoAniversario = anoAtual - idade
    print(anoAniversario)
else:
    anoAniversario = anoAtual - idade -1   
    print(anoAniversario) 