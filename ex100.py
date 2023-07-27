""" Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 numeros e vai colocá-los dentro da lista e a
segunda vai mostrar a soma entre todos os valores PARES sorteados pela função anterior"""

from random import randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        # O Flush é usado para garantir que o print ocorra no tempo certo
        # usado juntamente com o sleep
        print(f'{n} ', end='', flush=True)
        sleep(.3)
    print('PRONTO!')


def somapar():
    soma = 0
    for each in numeros:
        if each % 2 == 0:
            soma += each
    print(f'Somando os valores pares de {numeros}, temos {soma}')

numeros = list()
sorteia(numeros)
somapar()


