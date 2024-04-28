"""Crie um código que leia um número 
diferente de zero e diga se este número 
é positivo ou negativo , se a pessoa repetir  0 , repita  a pergunta
"""

numero = float(input('digite um numero'))
while numero == 0:

    numero = float(input('digite novamente'))

if numero >0:
    print('numero positivo')
else:
    print('nuemero negativo')    

