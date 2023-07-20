""" Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas masi leves"""


individuo = list()
galera = list()
maior = list()
menor = list()
contador = 0
while True:
    individuo.append(str(input('Nome: ')))
    individuo.append(float(input('Peso: ')))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    galera.append(individuo[:])
    if contador == 0:
        menor.append(galera[0])
        maior.append(galera[0])
        contador += 1
    individuo.clear()
    if continuar != 'S':
        break
# Eu fiz um for pra verificar o menor e maior peso após eles serem cadastrados na lista
# O guanabara ja fez isso dentro do append de cada item da lista no condicional if
for count, pessoa in enumerate(galera):
    if galera[count][1] < menor[0][1]:
        menor.clear()
        menor.append(galera[count])
    elif galera[count][1] == menor[0][1] and galera[count][0] != menor[0][0]:
        menor.append(galera[count])
    if galera[count][1] > maior[0][1]:
        maior.clear()
        maior.append(galera[count])
    elif galera[count][1] == maior[0][1] and galera[count][0] != maior[0][0]:
        maior.append(galera[count])

# O output do guanabara deu o resultado dentro de uma lista ...
# Será que ele fez 4 listas , 2 pra o valor dos maiores e menores e 2 pros nomes dos respectivos?
print('-=' * 15)
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maior[0][1]} Kg. Peso de ', end='')
# como no caso do Guanabara a variável menor e maior não é uma lista
# ele também usa dois 'for' , porém pra verificar se o valor do maior existe na lista
# se existir ele printa o Nome relacionado a aquele peso
for c in range(0, len(maior)):
    print(f'{maior[c][0]} ', end='')
print(f'\n O menor peso foi de {menor[0][1]} Kg. Peso de ', end='')
for c in range(0, len(menor)):
    print(f'{menor[c][0]} ', end='')
