""" A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria , de acordo com a idade :
- Até 9 anos : Mirim
- Até 14 anos : Infantil
-Até 19 anos : Junior
-Até 25 anos : Sênior """

from datetime import date

anoNascimento = int(input('Qual o ano de nascimento do atleta ? '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print('A CATEGORIA do atleta é : ')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
