""" Crie um programa que tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a calcular e o outro chamado
show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial."""

# não consegui pensar numa solução sem gambiarra pra não mostrar o '='
# quando o show é false
# e também não mostrar o último x apos o valor 1


def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um numero n.
    """

    f = 1
    for x in range(num, 0, -1):
        f *= x
        if show:
            print(f'{x} x ', end='')
    print('= ', end='')
    return f


print(fatorial(5, show=False))
help(fatorial)
