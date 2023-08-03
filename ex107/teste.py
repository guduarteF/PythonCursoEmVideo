""" Crie um módulo chamado moeda.py que tenha as funções
incorporadas aumentar(), dimunir(), dobro() e metade().
Faça também um programa que importe esse módulo e use
algumas dessas funções. """

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(p, 13)}')

""" Adapte o código do desafio 107, criando uma função
adicional chamada moeda() que consiga mostrar os valores como
um valor monetário formatado"""



