import irsim
import time
import numpy as np
from matriz import marcar_colunas_personalizadas

# Gerar matriz com obstáculos
# Esta função cria uma matriz representando o ambiente com obstáculos
matriz = marcar_colunas_personalizadas()
#for linha in matriz:
#    print(' '.join(linha))


env = irsim.make()
controle = False
collision = 0

for i in range(2000):

    env.step()

    if env.robot.collision:
            collision += 1
           
            

    if i > 15 & controle == False:
        #env.robot.vel_max[0] = 50
        #env.robot.vel_max[1] = 50
        #env.robot.vel_min[0] = -50
        #env.robot.vel_min[1] = -50
        
        #env.robot.color = (0, 0, 0)
        #env.reset_plot()
        
        controle = True
        #env.render()
        #print('Velocidade alterada para 50  ')
        
        

    env.render(figure_kwargs={'dpi': 100})
    
env.set_title(f'Número de colisões na simulação foi {collision}') # set the title of the environment
env.render()
print(collision)
env.pause()
time.sleep(5) 
input("Simulação pausada. Pressione Enter para encerrar.")  
env.end()

