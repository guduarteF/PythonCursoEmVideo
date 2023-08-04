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


def resumo(preco=0, porcent_aumento=10, porcent_redut=5):
    print('-' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{porcent_aumento}% de aumento: \t{aumentar(preco,porcent_aumento, True)}')
    print(f'{porcent_redut}% de redução: \t{diminuir(preco, porcent_redut, True)}')
