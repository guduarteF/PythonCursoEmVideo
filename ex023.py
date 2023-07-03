""" Faça um programa que leia um número de 0 a 9999 e mostre
na tela cada um dos dígitos separadores"""

num = int(input('Digite um número entre 0 e 9999 : '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('O número {} tem : \n unidade : {} \n dezena : {}'.format(num,unidade,dezena))
print('centena : {} \n milhar : {} '.format(centena, milhar))
