idade = int(input('Digite sua idade'))
anoAtual = 2024
mesAtual = 4

if anoAtual >= mesAtual:
    anoNascimento = (anoAtual - idade)-1
else:
    anoNascimento = anoAtual -idade

print('o ano de nascimento e',anoNascimento)