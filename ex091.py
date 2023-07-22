""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from time import sleep
from random import randint
jogadores = {'jogador1': randint(0, 6), 'jogador2': randint(0, 6),
             'jogador3': randint(0, 6), 'jogador4': randint(0, 6)}
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(.5)
print('Ranking dos jogadores: ')
# Não ensinado em aula , pra fazer a lista ficar em ordem no método sorted():
jogadores_em_ordem = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
# para converter o resultado gerado pelo método que retorna list/tupla , novamente para dicionário:
jogadores_em_ordem_lista = dict(jogadores_em_ordem)
num = 0
for k, v in jogadores_em_ordem_lista.items():
    num += 1
    print(f'{num}º lugar: {k} com {v}')
