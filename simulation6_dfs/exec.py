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
goals = obter_objetivos()



m = No.matriz


env = irsim.make('/simulation6_dfs/robot_world.yaml')
controle = False
collision = 0
arrived = 0


env.robot._state[0] = [46]  # Define a posição inicial do robô
env.robot._state[1] = [3]

env.robot.set_goal([4,45])  # Define o primeiro objetivo
caminho = algDfs([45,45],goals[0] )  # Calcula o caminho inicial


# for no in caminho:
#      print(m[no[0]][no[1]].posicao , '--', m[no[0]][no[1]].equivalente)


# Define o primeiro objetivo antes do loop
while True:
    env.step()

    if env.status == "Arrived":
        if len(goals) > 1:
             linha = goals[0][0]
             coluna = goals[0][1]
            
             
             goals.pop(0)
             obj = goals[0]
             equivalente = m[goals[0][0]][goals[0][1]].equivalente
             env.robot.set_goal(equivalente)
             caminho = algDfs([linha, coluna], obj)
        else:
            input('Aperte qualquer botão para finalizar')
            env.end()
    else:

        posicao = m[caminho[0][0]][caminho[0][1]].equivalente
        x = posicao[0]
        y = posicao[1]
        env.robot._state[0] = [x]  
        env.robot._state[1] = [y]
        caminho.pop(0)
    env.render(figure_kwargs={'dpi': 100})



    
   
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
