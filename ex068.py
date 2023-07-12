""" Faça um programa que jogue par ou ímpar com o computador. O jogo só
 será interrompido quando o jogador PERDER.
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

print('-' * 60)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-' * 60)
vezes = 0
while True:
        aleatorio = randint(0, 10)
        valor = int(input('Digite um valor: '))
        escolha = ' '
        soma = aleatorio + valor
        """ OBS !! -while PI not in escolha = o 'PI' respectivamente tem que estar na string escolha
                   -while escolha not in PI = retorna true os inputs(I,P,PI)"""
        while escolha not in 'PI':
            escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()
        print(f'Você jogou {valor} e o computador {aleatorio}. Total de {soma}', end='')
        print(' DEU PAR' if soma % 2 == 0 else ' DEU IMPAR')
        if escolha == 'P':
            if soma % 2 == 0:
                print('VOCE VENCEU')
                vezes += 1
            else:
                print('VOCE PERDEU')
                break
        if escolha == 'I':
            if soma % 2 == 1:
                print('VOCE VENCEU')
                vezes += 1
            else:
                print('VOCE PERDEU')
                break

        print('Vamos jogar novamente...')
print('=-' * 30)
print(f'GAME OVER! Você venceu {vezes}')
