""" Desenvolva um programa que leia o primeiro termo e a razão
de uma PA . No final , motre os 10 primeiros termos dessa progressão."""

print('PROGRESSÃO ARITMÉTICA : ')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(termo, razao * 10, razao):
    print(c)

