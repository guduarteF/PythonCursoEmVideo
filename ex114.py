""" Crie um código em Python que teste se o site Pudim está acessível pelo computador
usado."""

import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br')
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
except:
    print('\033[31mO site Pudim não está acessível no momento!\033[m')


