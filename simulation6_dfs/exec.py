import irsim
import time
import numpy as np
import random
import math
from simulation6_dfs.utils.goals import obter_objetivos
from simulation6_dfs.utils.no import No
from simulation6_dfs.utils.obstaculeValido import validarPosicao
from simulation6_dfs.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from simulation6_dfs.utils.main import algDfs
from simulation6_dfs.utils.no import No

matriz =  gerar_matriz_obstaculos_invertida()
# goals = obter_objetivos()



m = No.matriz


env = irsim.make('/simulation6_dfs/robot_world.yaml')
controle = False
collision = 0
arrived = 0

# em plano cartesiano
goals = [ [4, 4] , [ 47 , 46 ] , [49-43 , 43 ], [ 49 - 5 , 49 ], [49 - 45, 47]]
inicio = [45, 45]




env.robot._state[0] = [46]  # Define a posição inicial do robô
env.robot._state[1] = [3]

env.robot.set_goal([4,4])  # Define o primeiro objetivo
caminho = algDfs([45,45],[4,4] )  # Calcula o caminho inicial


# for no in caminho:
#      print(m[no[0]][no[1]].posicao , '--', m[no[0]][no[1]].equivalente)


# Define o primeiro objetivo antes do loop
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


#     if env.status == "Arrived":
#           print('Objetivo alcançado:', env.robot.goal)
#           arrived += 1
#           linha = goals[0][0]
#           coluna = goals[0][1]
#           inicio = [linha, coluna]
#           goals.pop(0)
#           if len(goals) != 0 :
#               env.robot.set_goal(goals[0])
#               caminho = algDfs(inicio, goals[0])  #Calcula o caminho para o próximo objetivo
#           else:
#               print("Todos os objetivos alcançados.")
#               break
     
# #     #Remove o primeiro elemento do caminho
#      posicao = m[caminho[0][0]][caminho[0][1]].equivalente
#      x = posicao[0]
# #    y = posicao[1]
#     env.robot._state[0] = [x]  
#     env.robot._state[1] = [y]
    
   
#     caminho.pop(0)

#     env.render(figure_kwargs={'dpi': 100})


# env.set_title(f'Número de colisões na simulação foi {collision}')
# env.render()
# print(collision)
# print(arrived)
# env.pause()
# time.sleep(5)
# input("Simulação pausada. Pressione Enter para encerrar.")
# env.end()
