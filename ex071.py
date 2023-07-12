""" Crie um programa que simule o funcionamento de um caixa eletrônico.
No início , pergunte ao usuário qual será o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
obs . CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$50,R$20,R$10 E R$1."""
print('=' * 30)
print('{:^30}'.format('BANCO DA SUA CIDADE'))
print('=' * 30)

""" # O desafio foi solucionado , porém sem utilizar a estrutura de repetição WHILE 

valor = int(input('Qual o valor que você quer sacar?'))
de50 = valor // 50
restante = valor - (de50*50)
de20 = restante // 20
restante = restante - (de20*20)
de10 = restante // 10
restante = restante - (de10*10)
de1 = restante

if de50 != 0:
    print(f'Total de {de50:.0f} cédulas de R$50')
if de20 != 0:
    print(f'Total de {de20:.0f} cédulas de R$20')
if de10 != 0:
    print(f'Total de {de10:.0f} cédulas de R$10')
if de1 != 0:
    print(f'Total de {de1:.0f} cédulas de R$1')
"""
# resolução guanabara
valor = int(input('Que valor você quer sacar?R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print('=' * 60)
print('VOLTE SEMPRE AO BANCO XYZ ! Tenha um bom dia!')
