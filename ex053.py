""" Crie um programa que leia uma frase
qualquer e diga se ela é palíndromo,desconsiderando
os espaços"""

print('DETECTOR DE PALÍNDROMO :')
print('(palavras que lidas de trás pra frente são iguais)')
print('(desconsiderando acentos e espaços)')
print('-=' * 10)
frase = str(input('Escreva uma frase :')).strip().upper()
fraseJunta = ''.join(frase.split())
fraseInvertida = ''

for c in range(len(fraseJunta)-1, -1, -1):
    fraseInvertida += fraseJunta[c]

print('FRASE NORMAL = {} '.format(fraseJunta))
print('FRASE DE TRÁS PRA FRENTE = {}'.format(fraseInvertida))
if fraseJunta == fraseInvertida:
    print('\033[1;32m PALÍNDROMO DETECTADO !\033[m')
else :
    print('\033[1;31m NÃO EXISTE PALÍNDROMO \033[m')
