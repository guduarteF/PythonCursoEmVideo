""" Faça um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o último nome separadamente"""

nome = str(input('Digite seu nome completo : ')).strip()
nomeSeparado = nome.split()
print('Seu primeiro nome é : {} '.format(nomeSeparado[0]))
print('Seu ultimo nome é : {} '.format(nomeSeparado[len(nomeSeparado)-1]))