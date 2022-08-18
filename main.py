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


# [1,5, 3,1, 7,3, 6,3, 2,4, 5,3]
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

def avaliacao(calendario):
  preco_total = 0
  ultima_chegada = 0
  primeira_partida = 1439

  voo_id = -1
  for i in range(len(calendario) // 2):
    origem = pessoas[i][1]
    voo_id += 1
    voo_ida = voos[(origem, destino)][calendario[voo_id]]
    voo_id += 1
    voo_volta = voos[(destino, origem)][calendario[voo_id]]

    preco_total += voo_ida[2]
    preco_total += voo_volta[2]

    if ultima_chegada < get_minutos(voo_ida[1]):
      ultima_chegada = get_minutos(voo_ida[1])
    if primeira_partida > get_minutos(voo_volta[0]):
      primeira_partida = get_minutos(voo_volta[0])

  espera_total = 0
  voo_id = -1
  for i in range(len(calendario) // 2):
    origem = pessoas[i][1]
    voo_id += 1
    voo_ida = voos[(origem, destino)][calendario[voo_id]]
    voo_id += 1
    voo_volta = voos[(destino, origem)][calendario[voo_id]]

    espera_total += ultima_chegada - get_minutos(voo_ida[1])

    espera_total += get_minutos(voo_volta[0]) - primeira_partida


  return espera_total + preco_total


#12 pois são 6 pessoas no problema original e como é um voo de ida e outro de volta 12
#9 pois são 9 possibilidades de voo no total

alcance = 9
dominio = 12

def gera_invididuoAleatorio():
  calendario = []
  for i in range(dominio):
    calendario.append(random.randint(0, alcance))
  return calendario

def mutacao(passo, individuo):
  gene_mutado = random.randint(0, dominio-1)
  passo = passo * random.randrange(1, -2, -2)
  if(individuo[gene_mutado]+passo <= alcance and individuo[gene_mutado]+passo >= 0):
    individuo[gene_mutado] += passo
    return individuo
  elif(individuo[gene_mutado]+passo > alcance):
    individuo[gene_mutado] = alcance
    return individuo
  else:
    individuo[gene_mutado] = 0
    return individuo


def crossover(individuo1, individuo2):
  gene_max = random.randint(0, alcance)
  return individuo1[0:gene_max] + individuo2[gene_max:]

#tamanho da populacao = quantos individuos terao na amostra inicial
#elitismo = depois da avialiacao inicial, voce pegara os melhores 20% inicais
#numero de gerações = quantas vezes os processos de crossover, mutações, etc serao rodados(qnt mais complexo mais geracoes é bom ter)


def algoritmo_genetico(tamanho_populacao, passo, elitismo, numero_geracoes):
  elitismo = int(math.ceil(elitismo * tamanho_populacao))
  total_individuos = []
  for i in range(tamanho_populacao):
    total_individuos.append(gera_invididuoAleatorio())

  for i in range(numero_geracoes):
    valor_individuos = [(avaliacao(total_individuos), total_individuos) for total_individuos in total_individuos]
    valor_individuos.sort()
    total_individuos = [total_individuos for (custo , total_individuos) in valor_individuos]
    populacao = total_individuos[0:elitismo]


algoritmo_genetico(10, 1, 0.2, 1)