"""Faça um algoritmo que receba 2 notas
 e calcule a media  aritmetica  e depois  calcule se ele foi aprovado  , reprovado ou se esta  em recuperaçao ,  
"""
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o primeiro numero: "))

media = (numero1 + numero2) / 2

if media >=7:
    print(f"Aprovado com media {media}")
elif media >=4:
    print(f"Recuperacao com media {media}")
else:       
    print(f"Reprovado com media {media}")    




