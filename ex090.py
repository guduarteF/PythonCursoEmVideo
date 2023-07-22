""" Faça um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno["Média"] > 6:
    aluno["Situação"] = 'Aprovado'
else:
    aluno["Situação"] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

