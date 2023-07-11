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

""" aqui foi feito uma gambiarra da minha parte , eu setei o valor menor = 999 
 pois assim qualquer valor comparado a ele vai ser o menor 
 mas não é o ideal fazer essa gambiarra , caso o usuário digite algo maior que 999.
 Na resolução o Guanabara na primeira linha do while usou um if pra fazer com que o 
 primeiro valor digitado receba o maior e o menor, tornando assim , uma melhor prática"""

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
print('Você digitou {} números '.format(count))
print('A média entre todos os valores é {:.1f}'.format(media))
print('O maior valor digitado foi: {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))

