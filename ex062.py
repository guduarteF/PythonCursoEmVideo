""" Melhore o DESAFIO 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser que quer
mostrar 0 termos"""

print('PROGRESSÃO ARITMÉTICA')
primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
resultado = primeirotermo
count = 0
termosAMais = 0
# na correção guanabara usou um while dentro de outro while
# sendo o primeiro while os 10 primeiros termos e o segundo os termos a mais
while count != 10 + termosAMais:
    print('{}>'.format(resultado), end='')
    count += 1
    resultado += razao
    if count == 10 + termosAMais:
        print('Pausa')
        termosAMais += int(input(' Deseja mostrar mais quantos termos ? '))
print('A progressão foi finalizada com {} termos mostrado'.format(count))
print('FIM')
