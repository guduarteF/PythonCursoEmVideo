""" Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final , mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000
c) Qual é o nome do produto mais barato"""

print('-'*60)
print('FAÇA COMPRAS NA LOJA')
print('-'*60)
continuar = 'S'
total = maisdemil = precomaisbarato = count = 0
nomemaisbarato = ''
while 'S' in continuar:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if count == 0:
        #outra opcao é fazer uma lista produto = [nome,valor] ao invés de 2 var
        precomaisbarato = preco
        nomemaisbarato = nome
        count += 1
    if preco < precomaisbarato:
        precomaisbarato = preco
        nomemaisbarato = nome
    if preco > 1000:
        maisdemil += 1
    total += preco
print('--------------- FIM DO PROGRAMA -----------------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisdemil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemaisbarato} que custa R${precomaisbarato:.2f}')
