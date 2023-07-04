""" Desenvolva um programa que leia o primeiro termo e a razão
de uma PA . No final , motre os 10 primeiros termos dessa progressão."""

print('PROGRESSÃO ARITMÉTICA : ')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
#Fórmula do Enésimo termo de uma PA
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    print(c, end='>')
print('ACABOU')

