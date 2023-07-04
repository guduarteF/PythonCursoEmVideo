""" Crie um programa que mostre na tela todos os números pares
que estão no intervalo entre 1 e 50"""

print('Números pares entre 1 e 50 :')
for c in range(1,51):
    if c%2 == 0:
        print(c)

# uma forma mais perfomática seria fazer o for pular de 2 em 2
# for n in range(2,51,2) . Pois o laço seria executado metade das vezes
# removendo assim o if