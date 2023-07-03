""" Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo."""

r1 = int(input('Qual o comprimento da primeira reta '))
r2 = int(input('Qual o comprimento da segunda reta '))
r3 = int(input('Qual o comprimento da terceira reta '))

# Definir qual são os menores lados comparando-os
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('PODE FORMAR UM TRIANGULO')
else:
    print('NÃO PODE FORMAR UM TRIANGULO')
 