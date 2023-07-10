""" Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma sequência de Fibonacci."""

print('SEQUÊNCIA DE FIBONACCI')
n = int(input('Quantos elementos da sequência deseja mostrar? '))
count = 0
numAtual = 1
numAnterior = 0
print('{}>{}>'.format(0, numAtual), end='')
while count != (n-2):
    seguinte = numAnterior + numAtual
    print('{}>'.format(seguinte), end='')
    numAnterior = numAtual
    numAtual = seguinte
    count += 1
print('FIM')
