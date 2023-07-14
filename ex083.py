""" Crie um programa onde o usuário digite uma expressão qualquer que usa parênteses.
Seu aplicativo deverá analisar se a expressâo passada está com os parênteses abertos e fechados
na ordem correta."""
cadaelemento = list()
expressao = (str(input('Digite a expressão: ')))
abreparenteses_count = fechaparenteses_count = 0

# guanabara usou outra forma do for -> for var in expressao
# passa em cada elemento da string mesmo não sendo uma lista
# criou uma lista só para os parênteses
# adiciona um parentese aberto sempre que existir
# remove um parentese aberto sempre que achar um parentese fechando
# se a lista estiver fazia é porque a qtd de parenteses abrindo = parenteses fechando
# expressão válida nesse caso , se não , expressão inválida

#Minha resolução
print(expressao)
for num in range(0, len(expressao)):
    cadaelemento.append(expressao[num])
for pos, valor in enumerate(cadaelemento):
    if cadaelemento[pos] == '(':
        abreparenteses_count += 1
    elif cadaelemento[pos] == ')':
        fechaparenteses_count += 1
if abreparenteses_count == fechaparenteses_count:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
