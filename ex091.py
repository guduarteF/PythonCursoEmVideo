""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from time import sleep
from random import randint
# Guanabara utilizou uma biblioteca -> from operator import itemgetter
# no sorted , em key = itemgetter(1) , posição (1) pois é os valores, (0) seria a chave
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
             'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(.5)
print('Ranking dos jogadores: ')
# O problema do sorted em dicionários é que eles possuem um valor para as chaves e um para valores
# Oque não ocorre nas listas pois só tem os valores diretamente
# Não ensinado em aula , pra fazer a lista ficar em ordem no método sorted():
# Para retornar somente esses valores do dicionário , duas opções:
# O lambda x: x[1] tem a mesma função do itemgetter(1) .


jogadores_em_ordem = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
# para converter o resultado gerado pelo método que retorna list/tupla , novamente para dicionário:
jogadores_em_ordem_lista = dict(jogadores_em_ordem)
num = 0
for k, v in jogadores_em_ordem_lista.items():
    num += 1
    print(f'{num}º lugar: {k} com {v}')
