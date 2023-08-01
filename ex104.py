""" Crie um programa que tenha a função leiaInt(), que vai funcionar
de forma semelhante á função input() do python, só que fazendo a
validação
para aceitar apenas valor númerico.
Ex: n = leiaInt('Digite um n') """

# eu utilizo a mesma lógica do exercício anterior
# guanabara resolve com o uso do is.numeric() novamente.
def leiaint(txt):

    while True:
        print(txt, end='')
        digitou = input()
        for x in range(0, len(digitou)):
            if digitou[x] in '0123456789':
                if digitou[len(digitou) - 1] in '0123456789':
                    return int(digitou)

            else:
                print('\033[31m Erro! Digite um número inteiro válido. \033[m')
                break


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
