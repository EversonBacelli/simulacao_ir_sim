import irsim
import time
import numpy as np
import random
import math
from goals import obter_objetivos

from simulation6_dfs.utils.obstaculeValido import validarPosicao
from simulation6_dfs.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida

matriz =  gerar_matriz_obstaculos_invertida()
goals = obter_objetivos()


env = irsim.make()
controle = False
collision = 0
arrived = 0
goals_index = 0

caminho = []
env.robot.set_goal(goals[0])

# Define o primeiro objetivo antes do loop


for i in range(1000):
    env.step()

    caminho.append([(env.robot.state[0])[0],(env.robot.state[1])[0], (env.robot.state[2])[0]])
    if env.robot.collision:
        collision += 1
        env.robot.state[2] = math.radians(90)
    
    if env.status == "Arrived":
        arrived += 1
        goals_index += 1
        if goals_index < len(goals) :
            env.robot.set_goal(goals[goals_index])
        else:
            print("Todos os objetivos alcançados.")
            break
        

      


    env.render(figure_kwargs={'dpi': 100})

for end in caminho:
    print(f'[{end[0]}, {end[1]}, {end[2]}],')

env.set_title(f'Número de colisões na simulação foi {collision}')
env.render()
print(collision)
print(arrived)
env.pause()
time.sleep(5)
input("Simulação pausada. Pressione Enter para encerrar.")
env.end()
