class Pessoa():
  def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo=False,dormindo=False,falando =False):
   self.nome=nomeAluno
   self.peso=pesoAluno
   self.idade=idadeAluno
   self.comendo = comendo
   self.dormindo =dormindo
   self.falando = falando


  def comer(self,alimento):
    print(f'{self.nome} foi comer {alimento}')
    self.comendo=True
   
  def andar(self):
      print(f'{self.nome} andou')
      self.comendo=True

  def dormir(self):
      if self.comendo:
          print(f"{self.nome} nao pode dormir por que ele esta comendo")
      else:
            print(f'{self.nome} foi dormir')
            self.dormindo = True
            self.falando = False

  def falar(self):
      self.falando =True
      if self.comendo == True:
          print(f"{self.nome} nao pode falar por que ele esta comendo ")
   

  def parardeComer(self):
      print(f'{self.nome}parou de comer')
      self.comendo = False

  def parardeFalar(self):
      print(f'{self.nome}parou de falar')
      self.falando = False

  def parardeDormir(self):
      print(f'{self.nome} parou de dormir e  acordou')


class Conta():
    def __init__(self, numero_conta, nome_cliente, tipo_conta):
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.saldo = 0
        self.status = False

    def depositar(self,valor):
     self.saldo +=valor
     print(f"Depósito de {valor:.2f} realizado com sucesso! Saldo atual:{self.saldo}")

    def sacar(self,valor):
      if self.saldo >= valor:
         self.saldo -=valor
         print(f"Saque realizado com sucesso ")
      else:
        print(f"Saldo insuficiente")


    def verificarSaldo(self):
        if self.status == True :
            print("Conta ativada com sucesso")
        else:
            print("Saldo da  conta deve estar zerado para ativar a conta")


    def ativarConta(self):
       if self.saldo == 0  and not self.status:
          self.status = True
          print('Conta ativada com sucesso')
       elif self.saldo !=0:
            print('Saldo da conta  deve ta zerado para ativar a conta')
       else:
            print('Conta ja esta ativada')

    def desativarConta(self):
       if self.saldo == 0:
          self.status = False
          print("Conta desativada com sucesso")



class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0


class Retangulo(Forma):
    def __init__(self):
       super().__init__()
    
    def calcularArea(self,base,altura):
        self.area = base * altura
        print(f"A Area é {self.area}")


    def calcularPerimetro(self,base,altura):
        self.perimetro = 2*(base+altura)
        print(f"O Perimetro é {self.perimetro}")




class Triangulo(Forma):
    def __init__(self, area, perimetro):
        super().__init__(area,perimetro)

    def calcularArea(self,base,altura):
        self.area = base * altura
        print(f"A Area é {self.area}")


    def calcularPerimetro(self,base,altura):
        self.perimetro = 2*(base+altura)
        print(f"O Perimetro é {self.perimetro}")



class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.escolha = None

    def obter_escolha(self):
        print(f"{self.nome}, escolha uma opção:")
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        self.escolha = int(input("Digite a opção desejada (ou 0 para sair): "))
        if self.escolha not in [0, 1, 2, 3]:
            print("Opção inválida, tente novamente.")
            self.obter_escolha()

    def exibir_escolha(self):
        if self.escolha == 1:
            print(f"{self.nome} escolheu Pedra")
        elif self.escolha == 2:
            print(f"{self.nome} escolheu Papel")
        elif self.escolha == 3:
            print(f"{self.nome} escolheu Tesoura")


class JogoJokenpo:
    def __init__(self):
        self.jogador = Jogador("Jogador")
        self.computador = Jogador("Computador")

    def determinar_vencedor(self):
        if (self.jogador.escolha == 1 and self.computador.escolha == 3) or \
           (self.jogador.escolha == 2 and self.computador.escolha == 1) or \
           (self.jogador.escolha == 3 and self.computador.escolha == 2):
            print("Jogador Venceu!")
        elif self.jogador.escolha == self.computador.escolha:
            print("Empate!")
        else:
            print("Computador Venceu!")

    def jogar(self):
       while True:
        self.jogador.obter_escolha()
        if self.jogador.escolha == 0:
            print("Saindo do jogo.")
            return

        self.jogador.exibir_escolha()

        self.computador.obter_escolha()
        if self.computador.escolha == 0:
            print("Saindo do jogo.")
            return

        self.computador.exibir_escolha()
        self.determinar_vencedor()
        print("")





