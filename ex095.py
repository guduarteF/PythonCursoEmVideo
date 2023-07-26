""" Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de cada jogador."""

dados = dict()
gols = list()
jogadores = list()
somagols = 0
while True:
    dados["nome"] = str(input('Nome do Jogador: '))
    qtdPartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for num in range(0, qtdPartidas):
        gols.append(int(input(f'Quantos gols na partida {num}? ')))
    dados["gols"] = gols[:]
    for c in gols:
        somagols += c
    dados["total"] = somagols
    jogadores.append(dados.copy())
    gols.clear()
    somagols = 0
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if 'N' in continuar:
        break
print('-=' * 15)
print('cod nome        gols       total')
print('-' * 35)
for num in range(0, len(jogadores)):
    print(f'{num} ', end='')
    for keys, values in jogadores[num].items():
        print(f'{values}      ', end='')
    print()
