frase = str(input('Digite um frase : ')).upper().strip()
numerodevezes = frase.count('A')
print('Na sua frase , aparece a letra A {} vezes'.format(frase.count('A')))
print('Esta letra aparece em sua primeira vez na posição {}'.format(frase.find('A')+1))
print('Esta letra aparece em sua última vez na posição {}'.format(frase.rfind('A')+1))

