nomeDaCidade = str(input('Digite o nome de uma cidade : ')).strip()
nomeSeparado = nomeDaCidade.split()
print('A cidade que você digitou {} , começa com SANTO ? {}'.format(nomeDaCidade,'SANTO' in nomeSeparado[0].upper()))