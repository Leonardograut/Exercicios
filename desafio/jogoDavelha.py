"""from desafio.jogoDavelha import verifica_vitoria


def exibir_tabuleiro():
    # Inicializa o tabuleiro do jogo da velha com zeros
    jogo = inicializar_tabuleiro()

    # Preenche o tabuleiro com números de 1 a 9
    count = 1
    for i in range(3):
        for j in range(3):
            jogo[i][j] = count
            count += 1

    # Exibe o tabuleiro de forma organizada
    print("==============")
    print("Jogo da Velha")
    print("+------+-------+")
    for i in range(3):
        for j in range(3):
            print("|", end=" ")
            print(f"{jogo[i][j]:<2}", end=" ")
        print("|")
        print("+------+-------+")


def inicializar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]


def verifica_vitoria(vetor_da_velha,simbolo):
    resultado = False
    # Linha
    if(vetor_da_velha[0] == simbolo and vetor_da_velha[1] == simbolo and vetor_da_velha[2] == simbolo):
        resultado = True
    elif(vetor_da_velha[3] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[5] == simbolo):
        resultado = True
    elif(vetor_da_velha[6] == simbolo and vetor_da_velha[7] == simbolo and vetor_da_velha[8] == simbolo):
        resultado = True
    # Coluna
    elif(vetor_da_velha[0] == simbolo and vetor_da_velha[3] == simbolo and vetor_da_velha[6] == simbolo):
        resultado = True
    elif(vetor_da_velha[1] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[7] == simbolo):
        resultado = True
    elif(vetor_da_velha[2] == simbolo and vetor_da_velha[5] == simbolo and vetor_da_velha[8] == simbolo):
        resultado = True
    # Vertical
    elif(vetor_da_velha[0] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[8] == simbolo):
        resultado = True
    elif(vetor_da_velha[6] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[2] == simbolo):
        resultado = True
    return resultado


def verifica_vitoria(vetor_da_velha):
     resultado = True
     for i in vetor_da_velha:
        if(i != "X" and i != "O"):
            resultado = False
     return resultado


jogador = 1
jogador_numero_1 = 0
jogador_numero_2 = 0

while(True):
    if (jogador == 1):
        jogador_numero_1 = input('Digite uma posiçao de  1 a 9')"""
         


import random


def imprime_grid(grid):
	print ("O status do grid é\n")

	for indice in range(len(grid)):
		print (grid[indice], end=" ")
		if indice == 2 or indice == 5 or indice == 8:
			print ("")

def verifica_grid(grid, jogador):
	
	# testando linhas
	if grid[0] == jogador and grid[1] == jogador and grid[2] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if grid[3] == jogador and grid[4] == jogador and grid[5] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if grid[6] == jogador and grid[7] == jogador and grid[8] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2

	# testando colunas
	if grid[0] == jogador and grid[3] == jogador and grid[6] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if grid[1] == jogador and grid[4] == jogador and grid[7] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if grid[2] == jogador and grid[5] == jogador and grid[8] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	
	#testando diagonais
	if grid[0] == jogador and grid[4] == jogador and grid[8] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2
	if grid[2] == jogador and grid[4] == jogador and grid[6] == jogador:
		if jogador == "X":
			return 1
		else:
			return 2

	return 0


quantidade_escolhas = 0	

grid = ["_"] * 9

while True:

	escolha = int(input("Qual é a sua escolha "))

	while grid[escolha-1] != "_":
		print ("Sua escolha foi inválida! Veja como está o grid")
		imprime_grid(grid)
		escolha = int(input("Qual é a sua escolha "))

	grid[escolha-1] = "X"
	quantidade_escolhas += 1

	vencedor = verifica_grid(grid,"X")

	if vencedor != 0:
		break

	if quantidade_escolhas == 9:
		break

	imprime_grid(grid)

	escolha_computador = random.randint(1,9)
	while grid[escolha_computador-1] != "_":
		escolha_computador = random.randint(1,9)

	grid[escolha_computador-1] = "O"
	quantidade_escolhas += 1

	vencedor = verifica_grid(grid,"O")
	if vencedor != 0:
		break
	imprime_grid(grid)

if vencedor == 1:
	print ("parabéns, você ganhou")
elif vencedor == 2:
	print ("Você perdeu, o computador ganhou")
else:
	print ("Deu velha, ninguém venceu, foi empate!")

imprime_grid(grid)