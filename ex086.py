""" Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos
pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

matriz = [[], [], []]
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f'Digite um valor para [{x}, {y}]: '))
        matriz[x].append(num)
print('-=' * 15)

for a in range(0, 3):
    for b in range(0, 3):
        print(f'[  {matriz[a][b]:^5}  ] ', end='')
    print()
