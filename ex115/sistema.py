""" Crie um pequeno modularizado que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

from time import sleep
from ex115.lib.interface import *
# * importa tudo


opcao = 0
while True:
    exibir('MENU PRINCIPAL')
    cor('1 -', 33, True)
    cor('Ver pessoas cadastradas', 34, False)
    cor('2 -', 33, True)
    cor('Cadastrar nova Pessoa', 34, False)
    cor('3 -', 33, True)
    cor('Sair do Sistema', 34, False)
    print('-' * 45)
    try:
        opcao = int(input('\033[33m Sua opção: \033[m'))
        if opcao == 3:
            exibir('Saindo do sistema... Até logo !')
            break
        elif opcao == 2:
            exibir('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            print(f'Novo registro de {nome} adicionado')
            with open('pessoas.txt', 'a') as arquivo:
                texto = f'{nome:<30} {idade:>3} anos'
                arquivo.write(texto + '\n')
            sleep(1)
        elif opcao == 1:
            exibir('PESSOAS CADASTRADAS')
            with open('pessoas.txt', 'r') as arquivo:
                for linha in arquivo:
                    linha = linha.rstrip()
                    print(linha)
            sleep(1)
        else:
            cor('ERRO! Digite uma opção válida!', 31)
    except:
        cor('ERRO! Digite uma opção válida!', 31)
