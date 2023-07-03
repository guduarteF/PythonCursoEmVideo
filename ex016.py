""" Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção inteira."""

from math import trunc
num = float(input('Digite um número real'))
print('O numero digitado foi {} , e sua porção real é {}'.format(num,trunc(num)))
#trunc = trucate , outra opção é {:.0f} mostrar o numero sem nenhuma casa decimal