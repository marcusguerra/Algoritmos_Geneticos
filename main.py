#flights.txt
#coluna 1- aeoroporto de saida
#coluna 2- aeroporto de chegada
#coluna 3- horario saida
#coluna 4- horario chegada
#coluna 5- preço
import time
import random
import math
import sys

pessoas = [('Lisbon', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Brussels', 'BRU'),
           ('London', 'LHR')]
#locais de saida e as siglas dos aeroportos

destino = 'FCO'

voos = {}
for linha in open('flights.txt'):
    origem, destino, partida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((partida, chegada, int(preco)))
print(voos['FCO', 'LIS'])