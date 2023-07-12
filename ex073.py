""" Crie uma tupla preenchida com os 30 primeiros colocados da Tabelo do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense"""

brasileirao = ('Botafogo', 'Flamengo', 'Grêmio', 'Fluminense', 'Palmeiras', 'Bragantino', 'Fortaleza', 'São Paulo', 'Cruzeiro', 'Internacional', 'Athletico-PR', 'Atlético-MG', 'Santos', 'Chapecoense', 'Corinthians', 'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG')
print('-=' * 15)
print('Lista de times do Brasileirão: {}'.format(brasileirao))
print('-=' * 15)
print('Os 5 primeiros colocados são : {}'.format(brasileirao[:5]))
print('-=' * 15)
print('Os 4 últimos são : {}'.format(brasileirao[16:]))
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-=' * 15)
# guanabara usou uma forma melhor de encontrar a posição da chapecoense , usando .index + 1
for pos, time in enumerate(brasileirao):
    if brasileirao[pos] == 'Chapecoense':
        print(f'O Chapecoense está na {pos}ª posição')

