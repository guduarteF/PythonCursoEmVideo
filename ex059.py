""" Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep
print('OPERAÇÔES ENTRE DOIS NÚMEROS')
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('-=' * 20)
    print('Oque deseja fazer com esses dois valores?')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior entre eles')
    print('[4] Escolher novos números')
    print('[5] Sair')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        resultado = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1, num2, resultado))
    elif opcao == 2:
        resultado = num1 * num2
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, resultado))
    elif opcao == 3:
        if num1 > num2:
            print('O maior número entre {} e {} é {}'.format(num1, num2, num1))
        elif num2 > num1:
            print('O maior número entre {} e {} é {}'.format(num1, num2, num2))
        else:
            print('Não há maior , os dois são iguais.')
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número'))
    elif opcao != 5:
        print('Número digitado inválido , insira outro valor de (1-5)')
    sleep(1.5)
print('FIM DO PROGRAMA')
