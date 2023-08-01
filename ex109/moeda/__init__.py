def metade(num, formato=False):
    result = num / 2
    if formato:
        return moeda(result)
    else:
        return result


def dobro(num, formato=False):
    result = num * 2
    if formato:
        return moeda(result)
    else:
        return result


def aumentar(num, porcem, formato=False):
    result = num + ((num * porcem) / 100)
    if formato:
        return moeda(result)
    else:
        return result


def diminuir(num, porcem, formato=False):
    result = num - ((num * porcem) / 100)
    if formato:
        return moeda(result)
    else:
        return result


def moeda(num):
    formato = f'R${num:.2f}'
    return formato
