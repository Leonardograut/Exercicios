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











