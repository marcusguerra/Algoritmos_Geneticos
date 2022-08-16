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

# [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]
def imprime_calendario(calendario):
  voo_id = -1
  preco_total = 0
  for i in range(len(calendario) // 2):
    nome = pessoas[i][0]
    origem = pessoas[i][1]
    voo_id += 1
    voo_ida = voos[(origem, destino)][calendario[voo_id]]
    preco_total += voo_ida[2]
    voo_id += 1
    voo_volta = voos[(destino, origem)][calendario[voo_id]]
    preco_total += voo_volta[2]
    print('%10s%10s %5s-%5s U$%3s %5s-%5s U$%3s' % (nome, origem, voo_ida[0], voo_ida[1], voo_ida[2],
                                                    voo_volta[0], voo_volta[1], voo_volta[2]))
  print('Preço total: ', preco_total)

def get_minutos(hora):
  t = time.strptime(hora, '%H:%M')
  minutos = t[3] * 60 + t[4]
  return minutos