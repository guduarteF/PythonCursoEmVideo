""" Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 numeros e vai colocá-los dentro da lista e a
segunda vai mostrar a soma entre todos os valores PARES sorteados pela função anterior"""

from random import randint

numeros = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for cada in numeros:
        print(f'{cada} ', end='')
    print('PRONTO!')


def somapar():
    soma = 0
    for each in numeros:
        if each % 2 == 0:
            soma += each
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
somapar()
