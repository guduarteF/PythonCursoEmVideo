""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção ( sem usar o sort()).
No final, mostre a lista ordenada na tela. """

# AINDA NÃO SOLUCIONADO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
valores = [7]
# lista[2,3,5,7,9]
val = int(input('Digite um valor: '))
valores.append(val)
print('Valor adicionado no final da lista...')
for num in range(0, 4):
    val = int(input('Digite um valor: '))
    for pos, valor in enumerate(valores):
        if val > max(valores):
            valores.append(val)
            print('Adicionado ao final da lista...')
        elif val < min(valores):
            valores.insert(0, val)
            print('Adicionado na posição 0 da lista')
        elif min(valores) < val < max(valores):
            if val > valores[pos]:
                valores.insert(pos + 1, val)
                print(f'Adicionado na posição {pos + 1} da lista')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')

