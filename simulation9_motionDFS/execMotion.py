import irsim
import time, os, psutil, tracemalloc, random, math
import numpy as np
import copy, json

from simulation9_motionDFS.utils.goals import obter_objetivos
from simulation9_motionDFS.utils.obstaculeValido import validarPosicao
from simulation9_motionDFS.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from simulation9_motionDFS.utils.no import No, Status
from simulation9_motionDFS.utils.arvore import gerarArvore, printarArvore
from simulation9_motionDFS.utils.main import menorCaminho
from simulation9_motionDFS.utils.algDFS import algoritmoDFS
from simulation9_motionDFS.utils.deslocamento import motionRobot
from simulation9_motionDFS.utils.estatistica import Estatistica

matriz =  gerar_matriz_obstaculos_invertida()
No.matriz = gerarArvore(matriz)
m = No.matriz
goals = obter_objetivos()

No.retirarVizinhosNulos()





# Stage 1 - Algoritmo de Mapeamento do Ambiente com DFS
processoS1 = psutil.Process(os.getpid())
tracemalloc.start()
inicioDFS = time.time()
inicioProcess = time.process_time()
# # exec DFS
DFS = algoritmoDFS([45,45], [4,4], m )  # Calcula o caminho inicial
m = No.resetMatriz(m)
fimDFS = time.time()
fimProcess = time.process_time()
memoriaS1 = processoS1.memory_info().rss / 1024**2
men_atual, men_pico = tracemalloc.get_traced_memory()
men_atual_s1 = men_atual
men_pico_s1 = men_pico
tracemalloc.stop()


inicio = [45,45]
for go in goals:
    # Stage 2 - Busca do Objetivo no Mapa 
    m = No.resetMatriz(m) # Stage 2 - Busca do Objetivo no Mapa 
    tracemalloc.start()
    processoS2 = psutil.Process(os.getpid())
    execDFSinicio = time.time()
    execProcessInicio = time.process_time()
    nos = motionRobot(go, copy.deepcopy(DFS), inicio , m)
    inicio = go
    m = No.resetMatriz(m)
    execDFSfim = time.time()
    execProcessFim = time.process_time()
    memoriaS2 = processoS2.memory_info().rss / 1024**2
    men_atual, men_pico = tracemalloc.get_traced_memory()
    men_atual_s2 = men_atual
    men_pico_s2 = men_pico

    # Dados
    timeDFS = fimDFS - inicioDFS
    execDFS = execDFSfim - execDFSinicio
    tempoDeCiclo = execDFSfim - inicioDFS
    totalRAM = men_atual_s1 + men_atual_s2

    Estatistica(nos[0], nos[-1], timeDFS, memoriaS1, men_atual_s1, execDFS, men_atual_s2, men_pico_s2, len(nos), tempoDeCiclo, totalRAM)


lista_dict = [p.__dict__ for p in Estatistica.resultado]
json_result = json.dumps(lista_dict, ensure_ascii=False, indent=4)

print(json_result)


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