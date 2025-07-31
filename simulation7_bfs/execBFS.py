import irsim
import time
import numpy as np
import random
import math
from simulation7_bfs.utils.goals import obter_objetivos

from simulation7_bfs.utils.obstaculeValido import validarPosicao
from simulation7_bfs.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from simulation7_bfs.utils.no import No
from simulation7_bfs.utils.arvore import gerarArvore
from simulation7_bfs.utils.main import algoritmoBFS

matriz =  gerar_matriz_obstaculos_invertida()
No.matriz = gerarArvore(matriz)
# goals = obter_objetivos()


m = No.matriz

env = irsim.make('/simulation7_bfs/robot_world.yaml')
controle = False
collision = 0
arrived = 0

# em plano cartesiano
# goals = [ [4, 4] , [ 47 , 46 ] , [49-43 , 43 ], [ 49 - 5 , 49 ], [49 - 45, 47]]
# inicio = [45, 45]

env.robot._state[0] = [46]  # Define a posição inicial do robô
env.robot._state[1] = [3]

env.robot.set_goal([4,4])  # Define o primeiro objetivo
caminho = algoritmoBFS(m[46][46], m[45][4])  # Calcula o caminho inicial

# for no in caminho:
#     print(no , '--', m[no[0]][no[1]].equivalente)


# # Define o primeiro objetivo antes do loop
while True:
    env.step()
    
    if env.status == "Arrived":
        input('Aperte qualquer botão para finalizar')
        env.end()

    posicao = m[caminho[0][0]][caminho[0][1]].equivalente
    x = posicao[0]
    y = posicao[1]
   
    env.robot._state[0] = [x]  
    env.robot._state[1] = [y]
    caminho.pop(0)
    env.render(figure_kwargs={'dpi': 100})