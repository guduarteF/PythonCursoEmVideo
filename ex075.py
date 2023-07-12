""" Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
No final mostre:
a) Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares."""

novecount = trespos = valorespares = 0
tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))

print(f'Você digitou os valores {tupla}')
# guanabara utilizou o var.count(9) pra saber a quantidade de números 9 na tupla
# e o var.index(3) + 1 para saber a posição do 3 na tupla
# eliminando assim a estrutura for e a condição if .

for c in range(0, len(tupla)):
    if tupla[c] == 9:
        novecount += 1
    if tupla[c] == 3:
        trespos = c

print(f'O valor 9 apareceu {novecount} vezes')
if trespos == 0 :
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {trespos + 1}ª posição')

print('Os valores pares digitados foram: ',end='')
for c in range(0,len(tupla)):
    if tupla[c] % 2 == 0:
        print(tupla[c],end=' ')

