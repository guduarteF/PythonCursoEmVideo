""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status de acordo com a tabela abaixo :

- Abaixo de 18.5 : ABAIXO DO PESO
- Entre 18.5 e 25 : PESO IDEAL
- 25 ATÉ 30 : SOBREPESO
-30 ATÉ 40 : OBESIDADE
-ACIMA DE 40 : OBESIDADE MÓRBIDA """

print('-=-' * 30)
print('PROGRAMA PARA CALCULAR O ÍNDICE DE MASSA CORPORAL')
print('-=-' * 30)

peso = float(input('Digite o peso de uma pessoa : '))
altura = float(input('Digite a altura dessa pessoa : '))

IMC = peso / (altura ** 2)

print('Seu IMC é {:.2f} e você está : '.format(IMC))

if IMC < 18.5:
    print('\033[1;34m ABAIXO DO PESO \033[m')
elif 18.5 <= IMC <= 24.9:
    print('\033[1;32m PESO IDEAL \033[m')
elif 25 <= IMC <= 29.9:
    print('\033[1;33m SOBREPESO \033[m')
elif 30 <= IMC <= 40:
    print('\033[1;31m OBESIDADE \033[m')
else:
    print('\033[7;31m OBESIDADE MÓRBIDA \033[m')


