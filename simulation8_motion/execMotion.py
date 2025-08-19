import irsim
import time
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





# exec DFS
pilhaDFS = algoritmoDFS([45,45], [4,4], m )  # Calcula o caminho inicial

# cont = 0
# for no in pilhaDFS:
#      print(cont , '--' , no.posicao)
#      cont += 1

# Resetando
for linha in m:
    for no in linha:
        if no is not None:
            no.status = Status.NAO_VISITADO


# # pilhaBFS = algoritmoBFS([45,45], [4,4], m)  

obj = [4,4]
obj_atingido = False
# caminho via DFS
visitados = [pilhaDFS[0]]

while True:
    topo = pilhaDFS[0]
    proximo = pilhaDFS[1]
    visitados.append(proximo)

    caminho = menorCaminho(topo.posicao, proximo.posicao, m)  
    print(f'De {topo.posicao} até {proximo.posicao} ', end=' ')
    for no in caminho:
        print(no.posicao, end=' --> ')
        if no.posicao == obj:
            obj_atingido = True
            break
    print('')
    if obj_atingido:
        print('Objetivo alcançado: ')
        break
    elif len(pilhaDFS) == 0:
        print('Objetivo não encontrado')
        break
    else:
        for no in visitados:
            no.status = Status.NAO_VISITADO
        pilhaDFS.pop(0)


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