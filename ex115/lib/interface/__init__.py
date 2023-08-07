def exibir(txt):
    print('-' * 45)
    print(f'{txt:^45}')
    print('-' * 45)


def cor(txt, num, continua=False):
    print(f'\033[{num}m {txt} \033[m') if continua is False else print(f'\033[{num}m {txt} \033[m', end='')


# Guanabara criou um função pra criar o menu, enumerando ele apartir de uma lista e retornando a resposta
# também criou uma função pra ler , criar arquivo e cadastrar pessoas