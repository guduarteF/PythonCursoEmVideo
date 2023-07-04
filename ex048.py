""" Faça um programa que calcule a soma entre todos os números
ímpares que são mútiplos de três e que se encontram no intervalo de
1 até 500."""

soma = 0
print('Soma de todos os números ímpares múltiplos de 3 entre 1 e 500 : ')
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
print('A soma é : {}'.format(soma))



