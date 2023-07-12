""" Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
na sequência.
No final , mostre uma listagem de preços organizando os dados em forma tabular."""

produtos = ('Caneta', 2.50, 'Borracha', 2,
            'Tesoura', 5, 'Caderno', 10.50,
            'Lapiseira', 9, 'Mochila', 59.99)

print('-' * 45)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-' * 45)
for c in range(0,len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}',end='')
    if c % 2 == 1:
        print(f'R${produtos[c]:>7.2f}')








print('-' * 45)

