""" Crie um programa que simule o funcionamento de um caixa eletrônico.
No início , pergunte ao usuário qual será o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
obs . CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$50,R$20,R$10 E R$1."""
print('=' * 60)
print('BANCO DA SUA CIDADE')
print('=' * 60)

valor = int(input('Qual o valor que você quer sacar?'))
de50 = valor // 50
restante = valor - (de50*50)
de20 = restante // 20
restante = restante - (de20*20)
de10 = restante // 10
restante = restante - (de10*10)
de1 = restante

print(f'Total de {de50:.0f} cédulas de R$50')
print(f'Total de {de20:.0f} cédulas de R$20')
print(f'Total de {de10:.0f} cédulas de R$10')
print(f'Total de {de1:.0f} cédulas de R$1')

print('=' * 60)
print('VOLTE SEMPRE AO BANCO XYZ ! Tenha um bom dia!')
