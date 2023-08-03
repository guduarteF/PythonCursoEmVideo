def metade(preco=0):
    result = preco / 2
    return result


def dobro(preco=0):
    result = preco * 2
    return result


def aumentar(preco=0, porcem=0):
    result = preco + ((preco * porcem) / 100)
    return result


def diminuir(preco=0, porcem=0):
    result = preco - ((preco * porcem) / 100)
    return result


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
