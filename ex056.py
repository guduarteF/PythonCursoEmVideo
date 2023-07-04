""" Desenvolva um programa que leia o nome , idade e sexo
de 4 pessoas. No final do programa , mostre :
-A média de idade do grupo
- Qual é o nome do homem mais velho
-Quantas mulher tem menos de 20 anos"""
media = 0
somaIdades = 0
idadeMaisVelho = 0
nome_Mais_Velho = ''
qtd_Mulher_Menores = 0

for c in range(1, 5):
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Qual o sexo (F para Feminino e M para masculino: ').upper()).strip()
    somaIdades += idade
    if idade > idadeMaisVelho and sexo == 'M':
        nome_Mais_Velho = nome
    if sexo == 'F' and idade < 20:
        qtd_Mulher_Menores += 1

print('A média de idade do grupo é {:.0f} anos'.format(somaIdades/4))
print('O nome do homem mais velho é {}'.format(nome_Mais_Velho))
print('{} Mulher(es) tem menos de 20 anos'.format(qtd_Mulher_Menores))
