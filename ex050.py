""" Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar , desconside-o"""

print('SOMA DE NÚMEROS PARES : ')
soma = 0
for c in range(1,7):
    num = int(input('Digite um número inteiro :'))
    if num % 2 == 0:
        print('A soma entre {} e {}'.format(num, soma),end = '')
        soma += num
        print(' é {}'.format(soma))
    else:
        print('O número {} é impar , portanto não será somado'.format(num))
