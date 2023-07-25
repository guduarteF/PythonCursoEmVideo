""" Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média"""

grupo = list()
pessoa = dict()
mulheres = list()
pessoa = dict()

while True:
    pessoa["nome"] = str(input('Nome: ')).strip()
    pessoa["sexo"] = str(input('Sexo: [M/F] ')).strip().upper()
    pessoa["idade"] = int(input('Idade: '))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(pessoa)
