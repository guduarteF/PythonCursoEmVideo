salario = float(input('Qual o salário de um funcionário ? '))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novosalario = salario + aumento
print('O seu novo salário é de {:.2f} reais'.format(novosalario))
