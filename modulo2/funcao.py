def cadastro():
    nomes = ["", "", "", "", ""]
    senhas = ["", "", "", "", ""]
    for x in range(5):
      nomes[x] = input('Digite o nome do usuário: ')
      senhas[x] = input('Digite a senha: ')


def imprime_nome(nome):
   print(f"Nome:{nome}")

   imprime_nome("leonardo")
   imprime_nome("maria")
   imprime_nome("jose")
   nome = input("Digite um nome")
   imprime_nome(nome)


def somar(*numeros):
    soma=0
    for x in range(len(numeros)):
      soma +=numeros[x]
    print(soma)


def processar_texto(texto):
    cont=0
    for x in range(len(texto)):
      if texto[x] != ".,!":
        cont=cont+1
    for z in range(len(texto)):
       if texto[z]== ".,!":
        cont = cont-1
    return texto

def tratarTexto(texto):
    cont = 0
    for x in range(len(texto)-1,-1,-1):
        print(texto[x],end="")
        if texto[x]!= " " and texto[x] != "." and texto[x] != ",":
            cont = cont + 1
    print(f"\n{cont}")
    print(texto[::-1])


"""faça uma funcao que recebe uma lista como
 argumento e crie uma nova lista , somente com numeros unicos
 exemplo   a=[1,2,2,3,4,3,4,5,6,7,6,8,7,10"""



def lista(*nova):
    nova_lista =[]
    for x in range(len(nova)):
      if nova[x]!= x:
          nova_lista.append(nova[x])
    print(nova_lista)

def duplicados(*lista):
    nova = set(lista)
    print(f"Lista Recebida{lista}")
    print(f"A Lista sem repeticao{nova}")

def duplicados2(*lista):
    listaNova=[]
    for x in lista:
        if lista[x] not in  listaNova:
            listaNova.append(x)
    print(listaNova)

def numeroPrimo(num):
  num=0
  for x in range(2,num-1):
        if num/num == 0:
           print(num, 'não é primo')
        else:
           print(num, 'é primo')

def test_primo(n):
    if (n ==1):
        return n,"Nao e primo"
    elif(n==2):
        return n,"E primo"

    else:
        for x in range(2,n):
            if(n% x == 0):
                return n , "Nao e primo"

        return n, "E primo"



"""n = int(input("digite um numero"))"""
def piramide(n):
    for x in range(1, n + 1):
        for j in range(1, x + 1):
            print(x , end=" ")

        print()




def piramide2(n):

    for x in range(1, n+1):
        for j in range(1, x + 1):
            print(j, end=" ")

        print()



def vogais(texto):
   cont = 0
   for x in range(len(texto)):
       if texto[x] == "a" or  texto[x] =="e" or texto[x] =="i" or texto[x] == "o" or texto[x] == "u":
           cont = cont + 1

       print(cont)

texto = "o rato roeu a roupa do rei de roma"
vogais(texto)