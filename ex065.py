""" Crie um programa que leia vários números inteiros pelo teclado.
No final da execução , mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores."""

media = 0
continuar = 'S'
maior = 0
count = 0
soma = 0
menor = 999

while continuar == 'S':
    num = int(input('Digite outro número inteiro :'))
    count += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = str(input('Deseja continuar ? [S/N]').upper())
media = soma / count
print('A média entre todos os valores é {:.1f}'.format(media))
print('O maior valor digitado foi: {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))
