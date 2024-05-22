

from classes import *

p1=Pessoa('Leonardo',70,28)
p1.comer('Coxinha')
p1.falar()
p1.dormir()


p2 = Conta(2222,'Leonardo','Corrente')
p2.ativarConta()
p2.ativarConta()
p2.depositar(222)
p2.sacar(200)

p3 = Retangulo()
p3.calcularArea(10,10)
p3.calcularPerimetro(10,5)


jogo = JogoJokenpo()
jogo.jogar()


p4 = Ingresso(100)
p4.imprimeValor()

p5 = Vip(50)
p5.valor_total()
print(f"Valor total do ingresso VIP: R$ {p5.valor_total():.2f}")
