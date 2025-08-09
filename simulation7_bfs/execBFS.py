import irsim
import time
import numpy as np
import random
import math
from simulation7_bfs.utils.goals import obter_objetivos

from simulation7_bfs.utils.obstaculeValido import validarPosicao
from simulation7_bfs.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from simulation7_bfs.utils.no import No
from simulation7_bfs.utils.arvore import gerarArvore, printarArvore
from simulation7_bfs.utils.main import algoritmoBFS

matriz =  gerar_matriz_obstaculos_invertida()
No.matriz = gerarArvore(matriz)
goals = obter_objetivos()


m = No.matriz
no_inicial = m[45][45]
# print(no_inicial.posicao, '--', no_inicial.vizinhos)

No.retirarVizinhosNulos()
        

# for linha in m:
#     for no in linha:
#         if no is not None:
#            print(no.posicao, '--', no.vizinhos, '-----' , len(no.vizinhos))



algoritmoBFS([45,45], [4,4])  

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