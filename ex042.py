""" Refaça o DESAFIO 035 dos TRIÂNGULOS [Calcule o comprimento de 3 retas e verifique se é possível
formar um triangulo] acrescentando o recurso de mostrar que tipo de triângulo
será formado
- EQUILATERO: todos os lados iguais
-ISÓSCELES: dois lados iguais
-ESCALENO: todos os lados diferentes"""

print('-' * 65)
print('PROGRAMA PARA ANALISAR A CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO:')
print('-' * 65)
r1 = float(input('Qual o comprimento da reta 1 : '))
r2 = float(input('reta 2 : '))
r3 = float(input('reta 3 : '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32m É possível formar um TRIÂNGULO com as 3 retas \033[m')
    print('O TIPO de TRIÂNGULO formado é : ')
    if r1 == r2 == r3:
        print('\033[7m EQUILÁTERO \033[m , todos os lados iguais')
    elif r1 != r2 != r3 != r1:
        print('\033[7m ESCALENO, \033[m todos os lados diferentes')
    else:
        print('\033[7m ISÓSCELES \033[m , dois lados iguais ')
else:
    print('\033[1;31m NÃO é possível formar um TRIÂNGULO com as 3 retas \033[m ')
