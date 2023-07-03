""" Elabore um programa que calcule o valor a ser pago por um produto
, cosiderando o seu preço normal e condição de pagamento :

-á vista dinheiro / cheque : 10% de desconto
-em até 3x no cartão : preço normal
-3x ou mais no cartão : 20% de juros"""

valor_do_produto = float(input('Qual o valor do produto ? '))
print('Escolha a forma de pagamento : ')
print(' [ 1 ] A vista no dinheiro ou cheque ')
print(' [ 2 ] Em até 3x no cartão ')
print(' [ 3 ] Parcelado em 4x ou mais')
opcao = str(input('DIGITE A OPÇÃO :').strip())

print('Seguindo esta opção de pagamento o valor a ser pago é de : ')
if opcao == '1':
    desconto = valor_do_produto * 0.10
    valorfinal = valor_do_produto - desconto
    print('\033[1;32m R$ {:.2f} \033[m'.format(valorfinal))
elif opcao == '2':
    print('R$ {:.2f}'.format(valor_do_produto))
elif opcao == '3':
    juros = valor_do_produto * 0.20
    valorfinal = valor_do_produto + juros
    print('\033[1;31m R$ {:.2f} \033[m'.format(valorfinal))
else:
    print('ERROR TENTE NOVAMENTE')

