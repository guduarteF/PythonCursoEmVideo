""" Crie um programa que leia o nome e duas notas de vários alunos
e guarde tudo em uma lista composta . No final , mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente. """

# ALUNOS  [ '[ FULANO, [5.5, 8.0], media ]',  [[BELTRANO], [7.9, 4.5], [media]] ]
alunos = list()
dados = list()
notas = list()
num = 0
while True:
    nome = input('Nome: ')
    notas.insert(0, float(input('Nota 1: ')))
    notas.insert(1, float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2
    dados.append((nome, notas[:], media))
    alunos.append(dados[:])
    notas.clear()
    dados.clear()
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar != 'S':
        break

print('-=' * 15)
print('No.  NOME        MÉDIA')
print('-' * 15)
for num in range(0, len(alunos)):
    print(f'{num}  {alunos[num][0][0]}  {alunos[num][0][2]}  ')
print('-' * 15)
while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        break
    print(f'Notas de {alunos[num][0][0]} são {alunos[num][0][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
