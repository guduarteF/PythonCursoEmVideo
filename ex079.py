""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista.
Caso o número ja exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem drescente"""
valores = list()
continuar = 'S'
while True:
    if 'S' in continuar:
        n = (int(input('Digite um valor ')))
        if n in valores:
            print('Valor duplicado! Não vou adicionar')
        else:
            valores.append(n)
            print('Valor adicionado com sucesso...')
        continuar = str(input('Quer continuar [S/N]')).strip().upper()
    else:
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')