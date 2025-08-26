import irsim
import time, os, psutil, tracemalloc, copy
import numpy as np
import random
import math, json
from simulation8_motionBFS.utils.goals import obter_objetivos
from simulation8_motionBFS.utils.obstaculeValido import validarPosicao
from simulation8_motionBFS.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from simulation8_motionBFS.utils.no import No, Status
from simulation8_motionBFS.utils.estatistica import Estatistica

from simulation8_motionBFS.utils.arvore import gerarArvore, printarArvore
from simulation8_motionBFS.utils.algBFS import algoritmoBFS
from simulation8_motionBFS.utils.deslocamento import motionRobot

matriz =  gerar_matriz_obstaculos_invertida()
No.matriz = gerarArvore(matriz)
m = No.matriz
goals = obter_objetivos()
No.retirarVizinhosNulos()


# Stage 1 - Algoritmo de Mapeamento do Ambiente com BFS
processoS1 = psutil.Process(os.getpid())
tracemalloc.start()
inicioProcess = time.process_time()
inicioBFS = time.time()
BFS = algoritmoBFS([45,45], m)  
fimBFS = time.time()
timeBFS = fimBFS - inicioBFS
fimProcess = time.process_time()
memoriaS1 = processoS1.memory_info().rss / 1024**2
men_atual, men_pico = tracemalloc.get_traced_memory()
men_atual_s1 = men_atual
men_pico_s1 = men_pico
tracemalloc.stop()

inicio = [45,45]
m = No.resetMatriz(m) # Stage 2 - Busca do Objetivo no Mapa 
# for go in goals:
    
#     # BFS = algoritmoBFS(inicio, m)  
#     m = No.resetMatriz(m) # Stage 2 - Busca do Objetivo no Mapa 
#     tracemalloc.start()

#     nos = motionRobot([go[0],go[1]], copy.deepcopy(BFS), inicio, m)
#     m = No.resetMatriz(m) # Stage 2 - Busca do Objetivo no Mapa 
#     inicio = go

#     print(nos[0].posicao, ' -> ', nos[-1].posicao, ' - ', len(nos), ' passos')
#     print('------------------------------------------------------------')

for go in goals:
    # BFS = algoritmoBFS(inicio, m)  
    m = No.resetMatriz(m) # Stage 2 - Busca do Objetivo no Mapa 
    tracemalloc.start()
    processoS2 = psutil.Process(os.getpid())
    execDFSinicio = time.time()
    execProcessInicio = time.process_time()
    execBFSinicio = time.time()
    nos = motionRobot(go, copy.deepcopy(BFS), inicio, m)
    inicio = go
    execBFSfim = time.time()
    execProcessFim = time.process_time()
    memoriaS2 = processoS2.memory_info().rss / 1024**2
    men_atual, men_pico = tracemalloc.get_traced_memory()
    men_atual_s2 = men_atual
    men_pico_s2 = men_pico

    # Dados
    timeBFS = fimBFS - inicioBFS
    execBFS = execBFSfim - execBFSinicio
    tempoDeCiclo = execBFSfim - inicioBFS
    totalRAM = men_atual_s1 + men_atual_s2

    Estatistica(nos[0], nos[-1], timeBFS, memoriaS1, men_atual_s1, execBFS, men_atual_s2, men_pico_s2, len(nos), tempoDeCiclo, totalRAM)
    #resultado.append(no)

lista_dict = [p.__dict__ for p in Estatistica.resultado]
json_result = json.dumps(lista_dict, ensure_ascii=False, indent=4)

print(json_result)

# print('-----Estatísticas BFS --------------------------------------------')
# print(f'Stage 1 - Algoritmo de Mapeamento com BFS: ')
# print(f'---- Tempo de uso processador {timeBFS} segundos')
# print(f'---- Consumo de Memória RAM: {men_atual_s1 / 1024**2:.5f} em MB')
# print(f'---- Pico de Memória RAM: {men_pico_s1 / 1024**2:.5f} MB')

# print(f'Stage 2 - Busca de Objetivo no Mapa, algoritmo de movimentação: ')
# print(f'---- Tempo de uso do processador na busca de objetivo: {execProcessFim - execProcessInicio:.5f} segundos')
# print(f'---- Consumo de memória RAM: {men_atual_s2 / 1024**2:.5f} em MB')
# print(f'---- Pico de Memória RAM: {men_pico_s2 / 1024**2:.5f} MB')
# print()
# print(f'Dados Consolidados: ')
# print(f'Tempo Total: {tempoDeCiclo} em segundos - 100%')
# print(f'---- Stage 1: {timeBFS / tempoDeCiclo * 100:.5f} %')
# print(f'---- Stage 2: {execBFS / tempoDeCiclo * 100:.5f} %')
# print(f'Memoria RAM: {totalRAM / 1024**2:.2f} MB')
# print(f'--- Stage 1: { float(men_atual_s1) / totalRAM * 100 } % ')
# print(f'--- Stage 2: { float(men_atual_s2) / totalRAM * 100 } %')

# print(f'Número de Nós consultados: ' , len(nos))
# print('____________________________________________________________')



# execBFSfim = time.time()
# execBFS = f'{execBFSfim - execBFSinicio:.5f}'


# print()
# print(f'Tempo de execução do algoritmo BFS: {timeBFS} segundos')
# print(f'Tempo de execução do algoritmo BFS: {execBFS} segundos')
# print(f'Tempo total de ciclo BFS: {execBFSfim - inicioBFS}')
# print(f'Número de passos BFS: ' , contBFS)





# print(f'Tempo de execução do algoritmo BFS: {fimBFS - inicioBFS:.5f} segundos')










# env = irsim.make('/simulation7_bfs/robot_world.yaml')
# controle = False
# collision = 0
# arrived = 0


# env.robot._state[0] = [46]  # Define a posição inicial do robô
# env.robot._state[1] = [3]

# env.robot.set_goal([4,45])  # Define o primeiro objetivo
# caminho = algoritmoBFS([45,45], [4,4])  # Calcula o caminho inicial

# for no in caminho:
#     print(no , '--', m[no[0]][no[1]].equivalente)


# # # Define o primeiro objetivo antes do loop
# Define o primeiro objetivo antes do loop
# while True:
#     env.step()

#     if env.status == "Arrived":
#         if len(goals) > 1:
#              linha = goals[0][0]
#              coluna = goals[0][1]
#              print(goals[0])
           
#              goals.pop(0)
#              obj = goals[0]
#              equivalente = m[goals[0][0]][goals[0][1]].equivalente
#              env.robot.set_goal(equivalente)
#              caminho = algoritmoBFS([linha, coluna], goals[0])
             
#         else:
#             input('Aperte qualquer botão para finalizar')
#             env.end()
#     else:

#         posicao = m[caminho[0][0]][caminho[0][1]].equivalente
#         x = posicao[0]
#         y = posicao[1]
#         env.robot._state[0] = [x]  
#         env.robot._state[1] = [y]
#         caminho.pop(0)
#     env.render(figure_kwargs={'dpi': 100})