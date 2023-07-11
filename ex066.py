""" Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles
( desconsiderando a flag )"""

num = soma = count = 0
print('LEITURA E SOMA DE VÁRIOS NÚMEROS')
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Foram digitados {count} número(s) e sua soma é {soma}')
