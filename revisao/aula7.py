"""Faça um algoritmo que leia a idade de 
uma pessoa expressa em anos, meses e dias 
e escreva a idade dessa pessoa expressa 
apenas em dias. Considerar ano com 365 
dias e mês com 30 dias.
"""



anos= int(input('digite o ano que vc nasceu'))
meses= int(input('digite o mes que voce nasceu'))
dias= int(input('digite o dia que vc nasceu'))

diasVividos = anos*365+meses*30+dias
print(diasVividos)