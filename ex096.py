""" Faça um programa que tenha uma função chamada Área(), que receba as dimensões de um
terreno retângular ( largura e comprimento ) e mostre a área do terreno."""

print('Controle de Terrenos')
print('-' * 15)


def Area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a} m²')


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
Area(largura, comprimento)
