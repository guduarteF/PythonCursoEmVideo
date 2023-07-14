""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção ( sem usar o sort()).
No final, mostre a lista ordenada na tela. """
# Desafio que tive maior dificuldade até então no curso
valores = []
#Minha resolução
val = int(input('Digite um valor: '))
valores.append(val)
print('Valor adicionado no final da lista...')
# na resolução do guanabara ele também usa 2 estruturas de repetição
# a primeira foi idêntica a minha , e da um append se for o primeiro elemento ou se for o maior
# a segunda foi um while :
""" while pos < len(list):
        if n <= lista[pos]:
            lista.insert(pos, n)
            break """
# ele não verfica se o valor está entre o minimo e o maximo.
#  somente se ele é menor do que cada elemento de um a um das pos 0 até a pos final

for num in range(0, 4):
    val = int(input('Digite um valor: '))
    for pos, valor in enumerate(valores):
        if val > max(valores):
            valores.append(val)
            print('Adicionado ao final da lista...')
            break
        elif val < min(valores):
            valores.insert(0, val)
            print('Adicionado na posição 0 da lista')
            break
        elif min(valores) < val < max(valores):
            if val > valores[pos]:
                if val < valores[pos + 1]:
                    valores.insert(pos + 1, val)
                    print(f'Adicionado na posição {pos + 1} da lista')
                    break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
