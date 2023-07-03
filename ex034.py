""" Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00 , calcule um aumento de 10%
Para os inferiores ou iguais , o aumento é de 15%"""

salario = float(input('Qual o salário de um funcionário ? '))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novosalario = salario + aumento
print('O seu novo salário é de {:.2f} reais'.format(novosalario))
