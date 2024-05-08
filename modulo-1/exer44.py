"""faça um codigo para ler  5 nomes de usuarios e suas respectivas senhas e ,
   e armazenar cada lista em um array diferente, apos completar a digitacao imprimir,
   nome, senha, e posicao dos dados no array,alterar o sistema anterior e faça um sitemaa
    de login pedindo a senha do usuario e  mostrando seu nome  e mensagem, o login efetuado com sucesso
"""


usuario=['','','','','']
senha = [0,0,0,0,0]

for x in range(5):
    usuario[x] = (input('Digite o seu nome '))
    senha[x] = (input('Digite a sua senha '))
for i in range(5):
    print('Nome :',usuario[i],'na posiçao',i)
    print('Senha :',senha[i],'na posiçao',i) 

    if usuario == usuario and senha == senha :
        
        print('Login efetuado com sucesso')
        print('-------------------------')
        print('seja bem vindo ',usuario)
   

      
       