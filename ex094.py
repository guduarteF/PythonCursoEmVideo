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
media = somaidades = 0
acima_da_media = list()


while True:
    pessoa["nome"] = str(input('Nome: ')).strip()
    pessoa["sexo"] = str(input('Sexo: [M/F] ')).strip().upper()
    pessoa["idade"] = int(input('Idade: '))
    if pessoa["sexo"] == 'F':
        mulheres.append(pessoa.copy())
    grupo.append(pessoa.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
for num in range(0, len(grupo)):
    somaidades += grupo[num]["idade"]
media = somaidades / len(grupo)
print('-=' * 15)
print(f'- O grupo tem {len(grupo)} pessoas')
print(f'- A média de idade é de {media} anos')
print('- As mulheres cadastradas foram: ', end='')
for cada in mulheres:
    print(cada["nome"], end=', ')
print('Lista das pessoas que estão acima da média: ')
for each in grupo:
    if each["idade"] > media:
        acima_da_media.append(each.copy())
for c in acima_da_media:
    print(c)



