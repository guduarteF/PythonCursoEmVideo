""" Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será a
 base de conversão """

num = int(input('Digite um número inteiro qualquer '))
print('Escolha para qual base você deseja converter este número')
print('[ 1 ] Para \033[4m BINÁRIO \033[m')
print('[ 2 ] Para \033[4m OCTAL \033[m')
print('[ 3 ] Para \033[4m HEXADECIMAL \033[m')
escolha = str(input('\033[1M DIGITE ... : \033[m').strip())

if escolha == '1':
    print('O número {} convertido para BINÁRIO é \033[7m {} \033[m'.format(num, bin(num) [2:]))
elif escolha == '2':
    print('O número {} convertido para OCTAL é \033[7m {} \033[m '.format(num, oct(num) [2:]))
elif escolha == '3':
    print('O número {} convertido para HEXADECIMAL é \033[7m {} \033[m'.format(num, hex(num) [2:]))
