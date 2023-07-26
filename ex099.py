""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é maior"""

from time import sleep


def qual_o_maior(* lst):
    maior = 0
    print(f'Analisando os valores passados...')
    sleep(1)
    for each in lst:
        if each > maior:
            maior = each
        print(f'{each} ', end='')
        sleep(.2)
    print(f'Foram informados {len(lst)} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print('-=' * 17)


print('-=' * 17)
qual_o_maior(2, 9, 4, 5, 7, 1)
qual_o_maior(4, 7, 0)
qual_o_maior(1, 2)
qual_o_maior(6)
qual_o_maior()
