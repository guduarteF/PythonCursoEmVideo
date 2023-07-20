""" Crie um programa que leia o nome e duas notas de vários alunos
e guarde tudo em uma lista composta . No final , mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente. """
# ficha[[nome, [nota1, nota2], media]] ficha[[[]]]
ficha = list()
num = 0

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar != 'S':
        break

print('-=' * 15)
print('No.  NOME        MÉDIA')
print('-' * 15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}  ')
print('-' * 15)
while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        break
    print(f'Notas de {ficha[num][0]} são {ficha[num][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
