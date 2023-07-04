""" Crie um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda não atinjiram a maioridade e quantas
ja são maiores """

from datetime import date
anoAtual = date.today().year
qtd_Maiores = 0
qtd_Menores = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento de uma pessoa :'))
    idade = anoAtual - nascimento
    if idade >= 21:
        qtd_Maiores += 1
    else:
        qtd_Menores += 1
print('Das 7 pessoas , {} são maiores de idade e {} são menores'.format(qtd_Maiores,qtd_Menores))
