""" Faça um programa que leia um número qualquer e mostre o seu fatorial"""

#não calcula fatorial de 0

print('Qual o FATORIAL ?')
num = int(input('Digite um número inteiro qualquer:'))
resultado = num
print('{}! = {}'.format(num, num), end='')
while num != 0:
    num -= 1
    print('x{}'.format(num),end='')
    if num != 0:
        resultado = resultado * num

print('={}'.format(resultado))




