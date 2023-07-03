""" Faça um programa que leia o ano de nascimento de um jovem e informe ,
de acordo com sua idade :

- Se ele ainda vai se alista ao serviço militar
- Se é a hora de se alistar
- Se ja passou do tempo de alistamento

Seu programa deverá mostrar o tempo que falta ou que passou do prazo"""

from _datetime import date
ano_De_Nacimento = int(input('Qual é o seu ano de nascimento ? '))
ano_Atual = date.today().year
idade = ano_Atual - ano_De_Nacimento

if idade < 18:
    print('Ainda falta {} ano(s) para se alistar no serviço militar'.format((18 - idade)))
elif idade > 18:
    print('Ja passou do prazo de se alistar')
else:
    print('Está na hora de se alistar ! ')
