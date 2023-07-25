""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente
,além da idade, com quantos anos a pessoa vai se aposentar.
Obs. Sabendo que a pessoa aposenta depois de 35 anos de colaboração"""
import datetime

Carteira = dict()
Carteira["nome"] = str(input('Nome: '))
Ano = int(input('Ano de Nascimento: '))
Carteira["idade"] = (datetime.date.today().year - Ano)
Carteira["ctps"] = int(input("Cateira de trabalho (0 não tem): "))
print('-=' * 15)
if Carteira["ctps"] == 0:
    for k, v in Carteira.items():
        print(f'{k} tem o valor {v}')
else:
    Carteira["contratação"] = int(input("Ano de contratação: "))
    Carteira["salario"] = float(input("Salário: R$ "))
    Carteira["aposentadoria"] = Carteira["idade"] + (Carteira["contratação"] + 35 - datetime.date.today().year)
    print('-=' * 15)
    for k, v in Carteira.items():
        print(f'{k} tem o valor {v}')
