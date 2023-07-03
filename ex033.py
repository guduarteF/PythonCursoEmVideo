""" Faça um programa que leia três número e mostre qual é
o maior e qual é o menor """

num1 = int(input('Digite o primeiro número : '))
num2 = int(input('Digite o segundo número : '))
num3 = int(input('Digite o terceiro número : '))
# ---Calculando o menor valor -----------
menor = num1
# Assumindo que o valor é o menor faz eu eliminar um if
# e se eles não for o menor ou maior as proximas condições substituem esse valor
if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3
# ---Calculando o maior valor -----------
maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3
# ------------- resultado
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))