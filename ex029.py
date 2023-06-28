velocidade = int(input('Qual foi a velocidade do carro em km/h? '))
if velocidade > 80 :
    print('VOCÊ EXCEDEU O LIMITE DE VELOCIDADE !')
    multa = velocidade - 80
    custo = multa * 7
    print('Você terá de pagar uma multa de {:.2f} reais '.format(custo))
