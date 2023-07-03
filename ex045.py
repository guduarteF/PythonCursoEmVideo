""" Crie um programa que faça o computador jogaar JOKENPô com você """
from time import sleep
from random import randint
print('-x-' * 10)
print('VAMOS JOGAR JOKENPÔ')
print('x-x' * 10)

vermelho = '\033[1;31m'
verde = '\033[1;32m'
itens = ['Pedra', 'Papel', 'Tesoura']
print('ESCOLHA ENTRE : ')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
escolha = int(input('Digite sua escolha : ').strip())
aleatorio = randint(0, 2)

print('-' * 30)
print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('PO')
print('-' * 30)

print('Computador jogou : {} '.format(itens[aleatorio]))
print('Jogador jogou : {} '.format(itens[escolha]))

print('-' * 30)

if escolha == aleatorio:
    print('EMPATE , JOGAR NOVAMENTE')
elif escolha == 0:
    if aleatorio == 1:
        print('{} VOCÊ PERDEU ! PEDRA PERDE PRA PAPEL'.format(vermelho))
    elif aleatorio == 2:
        print('{} VOCÊ VENCEU ! PEDRA GANHA DE TESOURA'.format(verde))
elif escolha == 1:
    if aleatorio == 0:
        print('{} VOCÊ VENCEU ! PAPEL GANHA DE PEDRA'.format(verde))
    elif aleatorio == 2:
        print('{} VOCÊ PERDEU ! PAPEL PERDE PRA TESOURA'.format(vermelho))
elif escolha == 2:
    if aleatorio == 0:
        print('{} VOCÊ PERDEU ! TESOURA PERDE PRA PEDRA'.format(vermelho))
    elif aleatorio == 1:
        print('{} VOCÊ VENCEU ! TESOURA GANHA DE PAPEL'.format(verde))

else:
    print('{} ERROR , TENTE NOVAMENTE'.format(vermelho))








