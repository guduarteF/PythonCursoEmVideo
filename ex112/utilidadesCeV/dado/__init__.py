from ex112.utilidadesCeV import moeda


def leiaDinheiro(msg='Digite o preço: R$'):
    preco = input(msg)
    ok = False
    while not ok:
        if not preco.isnumeric():
            if '.' in preco:
                ok = True
                return float(preco)
            elif ',' in preco:
                preconovo = preco.replace(',', '.')
                ok = True
                return float(preconovo)
            if not ok:
                print(f'\033[31m ERRO: "{preco}" é um preço inválido \033[m')
                preco = input(msg)
        else:
            return float(preco)
            break
