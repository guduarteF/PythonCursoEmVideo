""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso , mostre a listagem números gerados e também indique o menor e o maior valor que estão na tupla"""
from random import randint
aleatorio = (randint(0, 10),randint(0, 10),
             randint(0, 10), randint(0, 10), randint(0, 10))
maior = 0
menor = aleatorio[0]
print(f'Os valores sorteados foram: {aleatorio}')
for c in range(0, 5):
    # guanabara mostra um método max(variavel) que retorna o maior valor dentro da tupla
    # assim como min(variavel) retorna o menor valor dentro dela
    if aleatorio[c] < menor:
        menor = aleatorio[c]
    if aleatorio[c] > maior:
        maior = aleatorio[c]
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')