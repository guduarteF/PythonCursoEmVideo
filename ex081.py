""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista """
continuar = 'S'
valores = list()
while True:
    if continuar == 'S':
        valor = int(input('Digite um valor '))
        valores.append(valor)
        continuar = input('Quer continuar [S/N]').strip().upper()
    else:
        break
print('=-' * 30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')
