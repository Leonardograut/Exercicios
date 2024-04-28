"""Crie um algoritmo que leia um 
número e diga se ele é par ou ímpar
"""

n1 = int(input(" Digite o primeiro nuemero "))

if n1 % 2 == 0:
    print(f"{n1}O numero é par")
else:
    print(f"{n1}O numero é impar")