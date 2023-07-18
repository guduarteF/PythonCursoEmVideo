""" Aprimore o desafio anterior , mostrando no final:
A ) A soma de todos os valores pares digitados.
B ) A soma dos valores da terceira coluna.
C ) O maior valor da segunda linha. """

matriz = [[], [], []]
pares = list()
terceira_colum = list()
maior_segunda_linha = soma_pares = soma_terceira_coluna = 0
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f'Digite um valor para [{x}, {y}]: '))
        matriz[x].append(num)
print('-=' * 15)

for a in range(0, 3):
    for b in range(0, 3):
        print(f'[  {matriz[a][b]}  ] ', end='')
        if matriz[a][b] % 2 == 0:
            pares.append(matriz[a][b])
        if b == 2:
            terceira_colum.append(matriz[a][b])
        if a == 1:
            if matriz[a][b] > maior_segunda_linha:
                maior_segunda_linha = matriz[a][b]
    print('\n')
print('-=' * 15)
for c in pares:
    soma_pares += c
for d in terceira_colum:
    soma_terceira_coluna += d
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')





