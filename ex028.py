""" Escreva um programa que faça o computador 'PENSAR' em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador . O programa deverá escrever
na tela se o usuário venceu ou perdeu """

import random
from time import sleep

num = random.randrange(0,6) #randint , também funciona

advinhar = int(input('Tente adivinhar em qual número eu pensei de 0 a 5: '))
print('PROCESSANDO . . .')
sleep(2)
print('VENCEU ! Você acertou o número' if num == advinhar else 'PERDEU , O número que eu pensei foi {}'.format(num))
