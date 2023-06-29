""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa , o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal ,sabendo que ela não pode exceder 30% do salário ou então o emprétimo será negado"""

valor_Da_Casa = float(input('Qual o valor da casa ?'))
salario = float(input('Qual o salário do comprador'))
anos = int(input('Em quantos anos a casa será paga ?'))
valor_Da_Prestacao = valor_Da_Casa / (anos * 12)
trintaporcento = salario * 0.30

print('O valor da prestação é {:.2f} reais , dividido em {:.0f} meses !'.format(valor_Da_Prestacao, (anos * 12)))

if valor_Da_Prestacao > trintaporcento:
    print('\033[1;31m EMPRÉSTIMO NEGADO \033[m')
else:
    print('\033[1;32mEMPRESTIMO APROVADO')
