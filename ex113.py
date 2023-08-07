""" Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade de um número
de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaInt():
    while True:
        try:
            num = int(input('Digite um Inteiro: '))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return num
            break


def leiaFloat():
    while True:
        try:
            num = float(input('Digite um Real: '))
        except:
            print('\033[31mERRO: por favor, digite um número real válido\033[m')
        else:
            return num
            break


print(f'O valor inteiro digitado foi {leiaInt()} e o real foi {leiaFloat()}')