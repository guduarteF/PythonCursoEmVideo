""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada , o programa
deverá perguntar se o usuário quer ou não continuar no final , mostre :
a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos """

continuar = 'S'
mais18 = qtdMulheresMenos20 = qtdHomens = 0
# outra opção é while 'S' in continuar
while continuar == 'S':
    print('-' * 60)
    print('CADASTRE UMA PESSOA')
    print('-' * 60)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

    if idade > 18:
        mais18 += 1
    if sexo == 'F' and idade < 20:
        qtdMulheresMenos20 += 1
    if sexo == 'M':
        qtdHomens += 1

print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {qtdHomens} homens cadastrados')
print(f'E temos {qtdMulheresMenos20} mulheres com menos de 20 anos')
