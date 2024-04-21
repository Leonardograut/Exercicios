"""Escreva um algoritmo que leia o número de litros 
vendidos e o tipo de combustível (codificado da 
seguinte forma: E-etanol, G-gasolina), calcule e 
imprima o valor a ser pago pelo cliente 
sabendo-se que o preço do litro da gasolina é R$ 
5,80 e o preço do litro do etanol é R$ 4,90."""


numLitros = float(input('Digite a quantidade de litros'))
tipoCombustivel= (input('Digite o tipo de combustivel '))

precoG = 5.80 * numLitros
precoE = 4.90 * numLitros

if tipoCombustivel == "e" or  tipoCombustivel == "E":
    print("Etanol",precoE)
elif tipoCombustivel == "g" or tipoCombustivel == "G":
    print("Galosina",precoG)
else:
    print('nehum dos  dois')