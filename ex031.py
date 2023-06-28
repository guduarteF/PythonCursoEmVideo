distancia = int(input('Qual foi a distância da viagem em km '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O valor da passagem é {:.2f}'.format(preco))
