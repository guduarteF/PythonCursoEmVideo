""" Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: O nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente."""

# O valor inteiro não pode receber 'VAZIO' '' .... Como faço ?
# no caso do string tem outra forma sem ser por if var == '' ... ?


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


def leiaint(txt):
    while True:
        print(txt, end='')
        digitou = input()
        for x in range(0, len(digitou)):
            if digitou[x] in '0123456789':
                if digitou[len(digitou) - 1] in '0123456789':
                    break

            else:
                digitou = 0
                break

        if digitou == '':
            digitou = 0
        return int(digitou)
        break


print('-' * 30)
nome = str(input('Nome do Jogador: ')).strip()
gols = leiaint('Número de Gols: ')
if nome == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
