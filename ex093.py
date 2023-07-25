""" Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final , tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato."""
dados = dict()
gols = list()
somagols = 0
dados["nome"] = str(input('Nome do Jogador: '))
qtdPartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for num in range(0, qtdPartidas):
    gols.append(int(input(f'Quantos gols na partida {num}? ')))
dados["gols"] = gols[:]
for c in gols:
    somagols += c
dados["total"] = somagols
print('-=' * 15)
print(dados)
print('-=' * 15)
for key, value in dados.items():
    print(f'O campo {key} tem o valor {value}')
print('-=' * 15)
print(f'O jogador {dados["nome"]} jogou {qtdPartidas}.')
for partidas, gols in enumerate(gols):
    print(f'=> Na partida {partidas} fez {gols}')
print(f'Foi um total de {somagols} gols')

