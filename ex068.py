""" Faça um programa que jogue par ou ímpar com o computador. O jogo só
 será interrompido quando o jogador PERDER.
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

print('-' * 60)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-' * 60)

resultado = 'VENCEU'
vezes = 0
while True:
    if resultado == 'VENCEU':
        aleatorio = randint(0, 10)
        valor = int(input('Digite um valor: '))
        escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()
        soma = aleatorio + valor

        if escolha == 'P':
            escolha = 'PAR'
        else:
            escolha = 'ÍMPAR'

        if soma % 2 == 0:
            condicao = 'PAR'
        else:
            condicao = 'ÍMPAR'

        if escolha == condicao:
            resultado = 'VENCEU'
            vezes += 1
        else:
            resultado = 'PERDEU'

        print('-' * 60)
        print(f'Você jogou {valor} e o computador {aleatorio}. Total de {soma} = DEU {condicao}')
        print('-' * 60)
        print(f'VOCÊ {resultado}')
        if resultado == 'VENCEU':
            print('Vamos jogar novamente...')
            print('=-'*30)
    else:
        break
print('-' * 60)
print(f'GAME OVER! Você venceu {vezes}')
