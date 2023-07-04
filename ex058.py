""" Melhore o desafio 028 onde o computador vai "pensar" em um número
entre 0 e 10 . Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
from time import sleep

palpite = 0
aleatorio = randint(0, 10)

print('=-' * 30)
print('TENTE ADIVINHAR O NÚMERO EM QUE ESTOU PENSANDO ENTRE 0 E 10')
print('=-' * 30)
print('PENSANDO.', end='')
sleep(.5)
print('.', end='')
sleep(.5)
print('.')
print('EM QUAL NÚMERO EU PENSEI ? [0-10]')
num = int(input('Digite um número : '))

while num != aleatorio:
    palpite += 1
    num = int(input('Você errou ! Tente outro número : '))
print('VOCÊ FINALMENTE ACERTOU ! Precisou de {} palpites '.format(palpite))
