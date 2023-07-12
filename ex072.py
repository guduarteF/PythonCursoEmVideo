""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão
, de zero até vinte
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

extenso_0a20 = ('zero', 'um', 'dois', 'três', 'quatro',
                'cinco', 'seis', 'sete', 'oito', 'nove',
                'dez', 'onze', 'doze', 'treze', 'catorze',
                'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= numero <= 20:
        break
    else:
        print('Tente Novamente. ',end='')
        numero = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso_0a20[numero]}')
