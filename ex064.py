""" Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a
 condição de parada. No final , mostre quantos números foram digitados e qual foi
 a soma entre eles. ( desconsiderando o flag)"""

flag = 999
soma = 0
count = 0
num = 0
# digite 999 para parar ? (o usuario vai saber ?)
while num != flag:
    num = int(input('Digite um número inteiro '))
    soma += num
    count += 1
print('Foram digitados {} números'.format(count))
print('A soma entre os números digitados é {}'.format(soma))