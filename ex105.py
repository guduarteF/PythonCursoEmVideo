""" Faça um programa que tenha uma função
notas() que pode receber várias notas de alunos e vai retornar um dicionário com
as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional) : 7 > Boa / 5 < Razoável < 7  / Ruim < 5"""


def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param num: uma ou mais notas dos alunos ( aceita várias )
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    menor = num[0]
    maior = soma = 0
    for c in num:
        soma += c
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    media = soma / len(num)
    info = {'total': len(num), 'maior': maior, 'menor': menor, 'média': media}
    if sit is True:
        if media >= 7:
            result = 'Boa'
        elif 5 <= media < 7:
            result = 'Razoável'
        else:
            result = 'Ruim'
        info['situação'] = result
    return info


# Programa principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
help(notas)
