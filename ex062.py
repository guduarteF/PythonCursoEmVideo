""" Melhore o DESAFIO 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser que quer
mostrar 0 termos"""

print('PROGRESSÃO ARITMÉTICA')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
resultado = termo
count = 0
termos = 0
while count != 10 + termos:
    resultado += razao
    print('{}>'.format(resultado),end='')
    count += 1
    if count == 10:
        termos = int(input(' Deseja mostrar mais quantos termos ? '))
print('FIM')