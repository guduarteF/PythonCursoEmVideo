""" Dentro do pacote utilidadesCeV que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que
sejam monetários."""

from ex112.utilidadesCeV import dado
from ex112.utilidadesCeV import moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
