""" Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuario digitar a palavra 'FIM', o programa se encerrará.
Obs: use CORES """


# guanabara fez uma lista c , em cada posição é uma cor

def msg(mensagem, cor):
    print(f'\033[30;{cor}m', end='')
    print('~' * (len(mensagem) + 8))
    print(f'    {mensagem}')
    print('~' * (len(mensagem) + 8))
    print('\033[m')


def ajuda(comando):
    msg(f'Acessando o manual do comando {comando}', 44)
    print('\033[40;7m', end='')
    help(comando)
    print('\033[m')


while True:
    msg('SISTEMA DE AJUDA PyHELP', 42)
    funcao = input('Função ou Biblioteca > ')
    if funcao == 'fim':
        msg('ATÉ LOGO', 41)
        break
    ajuda(funcao)
