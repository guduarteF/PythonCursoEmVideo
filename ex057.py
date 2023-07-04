""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
M ou F . Caso esteja errado , peça a digitação novamente até ter um valor correto"""

sexo = str(input('Qual o sexo da pessoa , Masculino ou Femino [M/F] ?'))

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo digitado INVÁLIDO , Digite novamente : [M/F]')).strip().upper()

print('Sexo correto e computado com sucesso !')
