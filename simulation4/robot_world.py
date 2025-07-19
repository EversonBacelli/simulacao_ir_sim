import irsim
import time
import numpy as np
import random
import math

from obstaculeValido import validarPosicao
from matriz_obstaculos import gerar_matriz_obstaculos_invertida

matriz =  gerar_matriz_obstaculos_invertida()



env = irsim.make()
controle = False
collision = 0
arrived = 0


env.robot.set_goal([6, 45])
# Define o primeiro objetivo antes do loop

print(vars(env._world))


for i in range(1000):
    env.step()

    
    
    if env.robot.collision:
        collision += 1
        env.robot.state[2] = math.radians(90)
    
    if env.status == "Arrived":
        arrived += 1
        x,y = validarPosicao()
        theta = random.uniform(-3.14, 3.14)
        env.robot.set_goal([x, y])




    env.render(figure_kwargs={'dpi': 100})

env.set_title(f'Número de colisões na simulação foi {collision}')
env.render()
print(collision)
print(arrived)
env.pause()
time.sleep(5)
input("Simulação pausada. Pressione Enter para encerrar.")
env.end()
