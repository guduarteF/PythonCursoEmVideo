""" Faça um programa que ajuda um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre
1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint
from time import sleep

print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
jogos = list()
verificacao = True
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print(f' -=-=-= SORTEANDO {qtd} JOGOS -==-=-')
for i in range(1, qtd+1):
    verificacao = True
    print(f'Jogo {i}: ', end='')
    for num in range(0, 6):
        jogos.append(randint(0, 60))

    # Para verificar se todos os numeros são diferentes entre sí
    # Um for dentro do outro pra todos os números serem comparados
    # De uma posição x para todas as posições y
    # While para garantir que o número alterado não seja igual a outro numero na lista

# Guanabara durante o append dos numeros na lista usou um if
    """ if num not in lista: append"""
    while verificacao:
        verificacao = False
        for x in range(0, 6):
            for y in range(0, 6):
                if x != y:
                    if jogos[x] == jogos[y]:
                        jogos.pop(x)
                        jogos.insert(x, randint(0, 60))
                        verificacao = True
                        break

    print(jogos)
    jogos.clear()
    sleep(.5)
print('-=' * 5 + ' <  BOA SORTE!  > ' + '-=' * 5)
