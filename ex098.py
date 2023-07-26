""" Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros:
Inicio, Fim e Passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10 , de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

from time import sleep


def contagemp(inicio, fim, passo):
    contagem = inicio
    print(f' Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo *= (-1)
    print(f'{contagem} ', end='')
    for inicio in range(inicio, fim, passo):
        if inicio > fim:
            contagem -= (passo * -1)

            sleep(.5)
            print(f'{contagem} ', end='')
        elif fim > inicio:
            contagem += passo
            sleep(.5)
            print(f'{contagem} ', end='')
    print('FIM!')
    print('-=' * 20)


print('-=' * 20)
contagemp(1, 10, 1)
contagemp(10, 0, 2)
print('Agora é sua vez de personalizar a contagem !')
init = int(input('Inicio: '))
end = int(input('Fim: '))
step = int(input('Passo: '))
if step == 0 or step == -1:
    step = 1
contagemp(init, end, step)
