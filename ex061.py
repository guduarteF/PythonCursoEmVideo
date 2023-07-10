""" Refaça o DESAFIO 051 , lendo o primeiro termo e a razão de uma PA
, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

print('PROGRESSÃO ARITMÉTICA')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
count = 0
resultado = termo

while count < 10:
    print('{}>'.format(resultado), end='')
    count += 1
    resultado = resultado + razao
print('FIM')
