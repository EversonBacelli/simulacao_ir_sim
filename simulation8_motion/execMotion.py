import irsim
import time, os, psutil
import numpy as np
import random
import math
from simulation8_motion.utils.goals import obter_objetivos

from simulation8_motion.utils.obstaculeValido import validarPosicao
from simulation8_motion.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from simulation8_motion.utils.no import No, Status
from simulation8_motion.utils.arvore import gerarArvore, printarArvore
from simulation8_motion.utils.main import menorCaminho
from simulation8_motion.utils.algDFS import algoritmoDFS
from simulation8_motion.utils.algBFS import algoritmoBFS

matriz =  gerar_matriz_obstaculos_invertida()
No.matriz = gerarArvore(matriz)
m = No.matriz
goals = obter_objetivos()

No.retirarVizinhosNulos()

def motionRobot(objetivo, listaDeNos, m):
    obj = objetivo
    atual = [listaDeNos[0]]
    objetivo_atingido = False
    nos = []

    while True:
        # print(len(listaDeNos))
        atual = listaDeNos[0]
        proximo = listaDeNos[1]

        # validar posicao
        if atual.posicao == obj:
            nos.append(atual)
            return nos
        elif len(listaDeNos) > 0:
            posicaoInicial = atual.posicao 
            posicaoFinal = proximo.posicao  
            caminho = menorCaminho(posicaoInicial, posicaoFinal , m)
            for no in caminho[1:]:
                nos.append(no)
            listaDeNos.pop(0)
            for item in nos:
                item.status = Status.NAO_VISITADO
        else: 
            print('Objetivo Não encontrado')




processo = psutil.Process(os.getpid())
inicioDFS = time.time()
inicioProcess = time.process_time()
# # exec DFS
pilhaDFS = algoritmoDFS([45,45], [4,4], m )  # Calcula o caminho inicial
m = No.resetMatriz(m)
fimDFS = time.time()

fimProcess = time.process_time()


execDFSinicio = time.time()
execProcessInicio = time.process_time()
nos = motionRobot([4, 4], pilhaDFS, m)
execDFSfim = time.time()
execProcessFim = time.process_time()

timeDFS = f'{fimDFS - inicioDFS:.5f}'
execDFS = f'{execDFSfim - execDFSinicio:.5f}'
memoria = processo.memory_info().rss / 1024**2
print('-----Estatísticas DFS --------------------------------------------')
print(f'Identificação dos Nós: {timeDFS} segundos')
print(f'Tempo de processamento na definição dos nós: {fimProcess - inicioProcess:.5f} segundos')
print(f'Tempo de busca de um objetivo com algoritmo DFS: {execDFS} segundos')
print(f'Tempo de uso do processador na busca de objetivo: {execProcessFim - execProcessInicio:.5f} segundos')
print(f'Tempo total de ciclo DFS: {execDFSfim - inicioDFS} segundos')
print(f'Consumo de memória RAM: {memoria:.2f} em MB')
print(f'Número de Nós consultados: ' , len(nos))
print('____________________________________________________________')

# Resetando
m = No.resetMatriz(m)

# lista_de_vizinhos = set()

# # Obter Arvore
# for linha in m:
#     for no in linha:
#         if no is not None:
#             for v in no.vizinhos[:]:  # cópia para poder remover
#                 vizinho_tuple = (v[0], v[1])
#                 if vizinho_tuple in lista_de_vizinhos and len(no.vizinhos) > 1:
#                     no.vizinhos.remove(v)
#                 else:
#                     lista_de_vizinhos.add(vizinho_tuple)


# inicioBFS = time.time()
# BFS = algoritmoBFS([45,45], m)  





# fimBFS = time.time()
# timeBFS = f'{fimBFS - inicioBFS:.5f}'

# m = No.resetMatriz(m)
# execBFSinicio = time.time()
# contBFS = motionRobot([4,4], BFS, m)
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