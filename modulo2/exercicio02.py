def piramide(n):
    for x in range(1,n+1):
        for j in range(1,x+1):
            print(j, end=" ")
    
    print(n)



def vogais(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont = cont + 1
    print(cont)
texto = "o rato roeu a roupa do rei de roma"
vogais(texto)

def sistema():
    opcao = -5
    nomes = ["","","","",""]
    senhas = [5]
    cont = 0

    while opcao != 3:
        opcao =int(input("1 para cadastrar\n"
                        "2 para login\n"
                        "3 para sair\n"
                        "Escolha sua opção: "))

        if opcao == 1:
            for x in range(5):
                nomes[x]= input("Digite o nome do usuario: ")
                senhas[x]= int(input(f"Digite a senha de {nomes[x]}: "))
                if nomes == nomes[x]:
                 print("Usuario ja cadastrado!")    


        elif opcao == 2:
            login = input("Digite o usuario: ")
            senha = input("Digite a senha: ")
            for y in range(5):
                if login == nomes[y]:
                    if senha == senhas[y]:
                        print("Login realizado com sucesso!")
                    else:
                        print("senha incorreta!")
                else:
                    cont = cont + 1
            if cont == 5:
                print("Usuario não existe!")


def estoque( quantidade, preco):
    total= preco * quantidade
    return total


def somar(n1,n2):
    return n1+n2

def subtrair(n1,n2):
    n1-=n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    return n1/n2

def resto(n1,n2):
    return n1%n2   


