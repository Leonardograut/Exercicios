
import requests
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="aulafinal"
)

nome = input("Nome: ")
cep = input('Digite seu cep: ')
consulta = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
endereco = consulta.json()

cep1 = endereco['cep']
logradouro = endereco['logradouro']
bairro = endereco['bairro']
localidade = endereco['localidade']
uf = endereco['uf']

cursor = banco.cursor()
sql = "INSERT INTO Endereco(nome, cep, logradouro, bairro, localidade, uf) VALUES (%s, %s, %s, %s, %s, %s)"
data = (nome, cep1, logradouro, bairro, localidade, uf)
cursor.execute(sql, data)

banco.commit()
cursor.close()
banco.close()






