"""Ler uma variável de número inteiro e mostrar a
tabuada desse número."""

numero = int(input("Digite um numero inteiro"))
             
for x in range(1, 11):
 print("A tabuada de", numero, "Vezes " , x, "é:",
numero*x," \n ")