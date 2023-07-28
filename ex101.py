""" Crie um programa que tenha uma função chamada voto() que vai
receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem voto NEGADO, OPCCIONAL ou OBRIGATÓRIO nas
eleições."""
import datetime


def voto(ano):
    idade = datetime.datetime.today().year - ano
    resultado = ''
    if 18 <= idade < 65:
        resultado = 'VOTO OBRIGATÓRIO'
    elif idade > 16:
        resultado = 'VOTO OPCIONAL'
    elif idade < 16:
        resultado = 'NÃO VOTA'
    print(f'Com {idade} anos: ', end='')
    return resultado


print('-' * 10)
num = (int(input('Em que ano você nasceu? ')))
print(voto(num))
