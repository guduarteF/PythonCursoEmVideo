""" Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e
R$ 0.15 por Km rodado"""

km = int(input('Qual a quantidade de km percorridos ?'))
dias = int(input('Quantos dias foi utilizado ? '))
preco = (60 * dias) + (km * 0.15)
print('O total pagar é de {} '.format((preco)))
