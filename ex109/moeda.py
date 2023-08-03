def metade(preco=0, formato=False):
    result = preco / 2
    if formato:
        return moeda(result)
    else:
        return result


def dobro(preco=0, formato=False):
    result = preco * 2
    return result if formato is False else moeda(result)


def aumentar(preco=0, porcem=0, formato=False):
    result = preco + ((preco * porcem) / 100)
    return result if not formato else moeda(result)


def diminuir(preco=0, porcem=0, formato=False):
    result = preco - ((preco * porcem) / 100)
    if formato:
        return moeda(result)
    else:
        return result


def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
