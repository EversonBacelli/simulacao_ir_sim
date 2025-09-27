import time, os, psutil, tracemalloc, copy
import numpy as np
import random
import math, json
from sim_12_lab1_BFS.utils.goals import obter_objetivos
from sim_12_lab1_BFS.utils.obstaculeValido import validarPosicao
from sim_12_lab1_BFS.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from sim_12_lab1_BFS.utils.no import No, Status
from sim_12_lab1_BFS.utils.estatistica import Estatistica
from sim_12_lab1_BFS.utils.arvore import gerarArvore, printarArvore
from sim_12_lab1_BFS.utils.algBFS import algoritmoBFS
from sim_12_lab1_BFS.utils.deslocamento import motionRobot
from sim_12_lab1_BFS.utils.matriz_lab import gerarMatrizLab


matriz = gerarMatrizLab()


cont = 0
No.matriz = gerarArvore(matriz)
m = No.matriz

for linha in m:
     for no in linha:
        if no is not None:
            print(f'NO: {no.posicao} - VIZINHOS: {no.vizinhos}')

print(cont)
     



# goals = obter_objetivos()
# No.retirarVizinhosNulos()


# inicio = [45,45]
# # Stage 1 - Algoritmo de Mapeamento do Ambiente com BFS
# processoS1 = psutil.Process(os.getpid())
# tracemalloc.start()
# inicioProcess = time.process_time()
# inicioBFS = time.time()
# BFS = algoritmoBFS(inicio, m)  
# fimBFS = time.time()
# timeBFS = fimBFS - inicioBFS
# fimProcess = time.process_time()
# memoriaS1 = processoS1.memory_info().rss / 1024**2
# men_atual, men_pico = tracemalloc.get_traced_memory()
# men_atual_s1 = men_atual
# men_pico_s1 = men_pico
# tracemalloc.stop()


# m = No.resetMatriz(m) # Stage 2 - Busca do Objetivo no Mapa 

# for go in goals:
#      # BFS = algoritmoBFS(inicio, m)  
#      m = No.resetMatriz(m) # Stage 2 - Busca do Objetivo no Mapa 
#      tracemalloc.start()
#      processoS2 = psutil.Process(os.getpid())
#      execDFSinicio = time.time()
#      execProcessInicio = time.process_time()
#      execBFSinicio = time.time()
#      nos = motionRobot(go, copy.deepcopy(BFS), inicio, m)
#      inicio = go
#      execBFSfim = time.time()
#      execProcessFim = time.process_time()
#      memoriaS2 = processoS2.memory_info().rss / 1024**2
#      men_atual, men_pico = tracemalloc.get_traced_memory()
#      men_atual_s2 = men_atual
#      men_pico_s2 = men_pico

#      # Dados
#      timeBFS = fimBFS - inicioBFS
#      execBFS = execBFSfim - execBFSinicio
#      tempoDeCiclo = execBFSfim - inicioBFS
#      totalRAM = men_atual_s1 + men_atual_s2

#      Estatistica(nos[0], nos[-1], timeBFS, memoriaS1, men_atual_s1, execBFS, men_atual_s2, men_pico_s2, len(nos), tempoDeCiclo, totalRAM)
#      #resultado.append(no)

# input('Aperte qualquer coisa para finalizar')
# lista_dict = [p.__dict__ for p in Estatistica.resultado]
# json_result = json.dumps(lista_dict, ensure_ascii=False, indent=4)
# print(json_result)



