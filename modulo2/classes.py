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









