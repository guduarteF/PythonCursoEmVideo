""" Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos Dólares ela pode comprar"""

dinheiro = float(input('Quanto dinheiro você tem na carteira ?'))
dolar = 3.27
conversao = dinheiro/dolar
print('Com {} você consegue comprar {:.2f} dólares'.format(dinheiro,conversao))
