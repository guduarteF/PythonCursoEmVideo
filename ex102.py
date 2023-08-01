""" Crie um programa que tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a calcular e o outro chamado
show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial."""

def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um numero n.
    """

    f = 1
    for x in range(num, 0, -1):
        if show:
            print(x, end='')
            if x > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= x
    return f


print(fatorial(5, show = True))
help(fatorial)
