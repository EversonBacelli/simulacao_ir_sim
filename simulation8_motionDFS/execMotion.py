import irsim
import time, os, psutil, tracemalloc, random, math
import numpy as np

from simulation8_motionDFS.utils.goals import obter_objetivos
from simulation8_motionDFS.utils.obstaculeValido import validarPosicao
from simulation8_motionDFS.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from simulation8_motionDFS.utils.no import No, Status
from simulation8_motionDFS.utils.arvore import gerarArvore, printarArvore
from simulation8_motionDFS.utils.main import menorCaminho
from simulation8_motionDFS.utils.algDFS import algoritmoDFS

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



# Stage 1 - Algoritmo de Mapeamento do Ambiente com DFS
processoS1 = psutil.Process(os.getpid())
tracemalloc.start()
inicioDFS = time.time()
inicioProcess = time.process_time()
# # exec DFS
pilhaDFS = algoritmoDFS([45,45], [4,4], m )  # Calcula o caminho inicial
m = No.resetMatriz(m)
fimDFS = time.time()
fimProcess = time.process_time()
memoriaS1 = processoS1.memory_info().rss / 1024**2
men_atual, men_pico = tracemalloc.get_traced_memory()
men_atual_s1 = men_atual
men_pico_s1 = men_pico
tracemalloc.stop()


# Stage 2 - Busca do Objetivo no Mapa 
tracemalloc.start()
processoS2 = psutil.Process(os.getpid())
execDFSinicio = time.time()
execProcessInicio = time.process_time()
nos = motionRobot([4, 4], pilhaDFS, m)
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

print('-----Estatísticas DFS --------------------------------------------')
print(f'Stage 1 - Algoritmo de Mapeamento com DFS: ')
print(f'---- Tempo de processamento {timeDFS} segundos')
# print(f'---- Tempo de processamento na definição dos nós: {fimProcess - inicioProcess:.5f} segundos')
print(f'---- Consumo de Memória RAM: {men_atual_s1 / 1024**2:.5f} em MB')
print(f'---- Pico de Memória RAM: {men_pico_s1 / 1024**2:.5f} MB')

print(f'Stage 2 - Busca de Objetivo no Mapa, algoritmo de movimentação: ')
print(f'---- Tempo de uso do processador na busca de objetivo: {execProcessFim - execProcessInicio:.5f} segundos')
print(f'---- Consumo de memória RAM: {men_atual_s2 / 1024**2:.5f} em MB')
print(f'---- Pico de Memória RAM: {men_pico_s2 / 1024**2:.5f} MB')
print()
print(f'Dados Consolidados: ')
print(f'Tempo Total: {tempoDeCiclo} em segundos - 100%')
print(f'---- Stage 1: {timeDFS / tempoDeCiclo * 100:.5f} %')
print(f'---- Stage 2: {execDFS / tempoDeCiclo * 100:.5f} %')
print(f'Memoria RAM: {totalRAM / 1024**2:.2f} MB')
print(f'--- Stage 1: { float(men_atual_s1) / totalRAM * 100 } % ')
print(f'--- Stage 2: { float(men_atual_s2) / totalRAM * 100 } %')

print(f'Número de Nós consultados: ' , len(nos))
print('____________________________________________________________')


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