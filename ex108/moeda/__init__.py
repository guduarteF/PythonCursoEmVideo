def metade(num):
    result = num / 2
    return result


def dobro(num):
    result = num * 2
    return result


def aumentar(num, porcem):
    result = num + ((num * porcem) / 100)
    return result


def diminuir(num, porcem):
    result = num - ((num * porcem) / 100)
    return result


def moeda(num):
    formato = f'R${num:.2f}'
    return formato
