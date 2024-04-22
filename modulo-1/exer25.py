

senha = int(input("Digite a senha do usuario"))

secreto = 1234

cont = 1
while secreto != senha:
  cont = cont+1
  senha = int(input("Digite a senha do usuario"))
  if cont ==3 and senha != secreto:
      print("Senha bolqueada")
      break
if senha == secreto:
      print("login efetuado com sucesso")

else:


 ''' faça um codigo para ler  a senha de  um usuario e apos  3 
tentativas erradas, sair do programa informando que a senha esta bloqueada'''