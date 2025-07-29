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


matriz =  gerar_matriz_obstaculos_invertida()
# goals = obter_objetivos()


# print(f'Iniciando Teste BFS')
# for obj in goals:
#     print(f'De: {inicio}  Para:  {obj}')
#     resp = algDfs(inicio, obj)
#     if resp is not None:
#         print(resp, end=",")
#         print('----')
    
#     inicio = obj



env = irsim.make('/simulation6_dfs/robot_world.yaml')
controle = False
collision = 0
arrived = 0
goals_index = 0

goals = [ [46 - 4,46] , [49-19,2] , [49 - 7, 43], [49 -2,5], [49 - 45,47]]
inicio = [4, 4]



print([inicio[0]])
env.robot._state[0] = [inicio[0]]  # Define a posição inicial do robô
env.robot._state[1] = [inicio[1]]
#robot.state = [inicio]
env.robot.set_goal(goals[0])  # Define o primeiro objetivo
caminho = algDfs(inicio, goals[0])  # Calcula o caminho inicial



# Define o primeiro objetivo antes do loop
while True:
    env.step()
   
     # if env.robot.collision:
     #     collision += 1
       
    
    if env.status == "Arrived":
        arrived += 1
        goals_index += 1
        if goals_index < len(goals) :
            env.robot.set_goal(goals[goals_index])
            caminho = algDfs(inicio, goals[0])
        else:
            print("Todos os objetivos alcançados.")
            break
     
    # Remove o primeiro elemento do caminho
    
    posicao = caminho[0]
    x = posicao[0]
    y = posicao[1]
    env.robot._state[0] = [x]  
    env.robot._state[1] = [y]
    
    if [x, y] != goals[goals_index]:
        caminho.pop(0)


    env.render(figure_kwargs={'dpi': 100})

# for end in caminho:
#     print(f'[{end[0]}, {end[1]}, {end[2]}],')

# env.set_title(f'Número de colisões na simulação foi {collision}')
# env.render()
# print(collision)
# print(arrived)
# env.pause()
# time.sleep(5)
input("Simulação pausada. Pressione Enter para encerrar.")
env.end()
