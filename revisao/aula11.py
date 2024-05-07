"""As maçãs custam R$ 1,30 cada se forem 
compradas menos de uma dúzia, e R$ 1,00 
se forem
 compradas pelo menos 12. Escreva um 
programa que leia o número de maçãs 
compradas, calcule e
 escreva o custo total da compra"""


macas = int(input("Quantas maças voce deseja"))
 
valor = macas 

if macas < 12:
    valor = macas * 1.30

print(f" Voce comprou {macas} maças. Pague R$ {valor}")