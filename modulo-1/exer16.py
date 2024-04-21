"""Dados os valores de horários abaixo, decifre a lógica e faça 
um código para executar.
 entrada01 3:45
 entrada02 14:20
saída 6:05"""


hora01 = int(input('Digite a hora1:'))
min1 = int(input("Digite os minutos1: "))
hora02 = int(input('Digite o segundo valor'))
min2 = int(input("Digite os minutos2"))
if hora01 >12:
    hora01 = hora01 -12
if hora02 > 12:
    hora02 = hora02 - 12
hora = hora01 + hora02

minuto = min1 + min2

if minuto >=60:
    minuto = minuto -60
    hora = hora +1


print(f" {hora} : {minuto} ")