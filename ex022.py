nome = str(input('Digite seu nome completo ')).strip()
print('Seu nome com todas as letras MAIÚSCULAS : {} '.format(nome.upper()))
print('Seu nome com todas as letras minúsculas : {} '.format(nome.lower()))
nomesemespaco = ''.join(nome.split())
print('Seu nome tem {} letras'.format(len(nomesemespaco)))
primeiroNome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(primeiroNome[0])))


