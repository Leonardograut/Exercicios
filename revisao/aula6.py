"""Ler um valor e escrever a mensagem É MAIOR 
QUE 10! se o valor lido for maior que 10, caso 
contrário escrever NÃO É MAIOR QUE 10!
"""


valor= int(input('digite um numero'))

if valor >10:
    print('é maior que 10')
elif valor == 10:
    print('valor e igual a 10')
else:
    print('e menor que 10')