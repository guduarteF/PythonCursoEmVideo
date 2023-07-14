""" Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
 No final , mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""
#guanabara usou uma lista fazia
# guanabara usou 24 linhas , eu resolvi em 13
valores = [0,0,0,0,0]
# também usou 3 estruturas de iteração , mas o primeiro for dele foi 'for c in range(0,5)
for pos, valor in enumerate(valores):
    valores[pos] = int(input(f'Digite um valor para a Posição {pos}: '))
print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ',end='')
for pos, valor in enumerate(valores):
    if valores[pos] == max(valores):
        print(f'{pos}... ',end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ',end='')
for pos, valor in enumerate(valores):
    if valores[pos] == min(valores):
        print(f'{pos}... ',end='')
