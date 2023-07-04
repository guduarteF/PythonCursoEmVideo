""" Refaça o DESAFIO 009 , mostrando a tabuada de um número que
o usuário escolher , só que agora utilizando laço for"""

print('TABUADA !')
num = int(input('Digite o número que deseja saber a tabuada : '))
for c in range(1,11):
    print('{} X {} = {}'.format(num,c,(num * c)))
