""" Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário . O programa será interrompido quando o
número solicitado for negativo."""

print('DESCUBRA A TABUADA!')
num = count = resultado = i = 0
while True:
    print('-' * 30)
    num = int(input('Quer saber a tabuada de qual valor ? '))
    print('-' * 30)

    if num < 0:
        print('PROGRAMA ENCERRADO ! Volte sempre')
        break

        # guanabara utilizou um [for] pra fazer a tabuada
        # muito mais performático pois resolve o problema em 2 linhas
        # ja feito em exercícios anteriores de for loop. Ex:.

    """  for c in range(1, 11):
         print(f'{num} x {c} = {num * c}') """

    while True:
        if i < 10:
            count += 1
            i += 1
            resultado = num * count
            print(f'{num} x {count} = {resultado}')
        else:
            i = count = 0
            break

print('-'*30)
