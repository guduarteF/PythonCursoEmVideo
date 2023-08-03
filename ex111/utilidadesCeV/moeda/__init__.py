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


def resumo(preco=0, porcent_aumento=0, porcent_redut=0):
    print('-' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco):>10}')
    print(f'Dobro do preço: {dobro(preco, True):>10}')
    print(f'Metade do preço: {metade(preco, True):>10}')
    print(f'{porcent_aumento}% de aumento: {aumentar(preco,porcent_aumento, True):>10}')
    print(f'{porcent_redut}% de redução: {diminuir(preco, porcent_redut, True):>10}')
