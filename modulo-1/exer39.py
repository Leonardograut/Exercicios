
hora_inicio = int(input("Digite a hora de início do jogo : "))
hora_fim = int(input("Digite a hora de fim do jogo : "))
if hora_fim >= hora_inicio:
    duracao = hora_fim - hora_inicio
else:
   duracao = 24 + hora_fim - hora_inicio
print(f"A duração do jogo é de {duracao} horas.")

"""
escreva um algoritmo para ler a hora  de inicio e a hora de fim de um jogo de xadrez considere apenas horas inteiras 
sem minutos e calcule a duracao do jogo em horas sabendo que o tempo maximo de duracao do jhogo e 24 horas
e que o jogo pode inicar em um dia e terminar no dia seguinte
"""
