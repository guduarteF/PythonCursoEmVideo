""" Desenvolva um programa que pergunte a distância de uma viagem em
Km . Calcule o preço da passagem , cobrando R$ 0.50 por Km para
viagens de 200 km e R$ 0.45 por viagens mais longas"""

distancia = int(input('Qual foi a distância da viagem em km '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O valor da passagem é {:.2f}'.format(preco))
