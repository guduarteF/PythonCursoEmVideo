""" Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto"""

preco = float(input('Qual o preço do produto?'))
novopreco = preco - preco * 0.05
print('O preço com desconto é : {}'.format(novopreco))