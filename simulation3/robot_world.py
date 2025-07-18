import irsim
import time
import numpy as np

env = irsim.make()
controle = False
collision = 0

for i in range(200):

    env.step()

    if i > 15 & controle == False:
        env.robot.vel_max[0] = 70
        env.robot.vel_max[1] = 70
        env.robot.vel_min[0] = -70
        env.robot.vel_min[1] = -70
        
        env.robot.color = (0, 0, 0)
        env.reset_plot()
        
        controle = True
        env.render()
        print('Velocidade alterada para 70  ')
        
        if env.robot.collision:
            collision += 1

    env.render(figure_kwargs={'dpi': 100})
    
env.set_title(f'Número de colisões na simulação foi {collision}') # set the title of the environment
env.render()

env.pause()
time.sleep(1) 
input("Simulação pausada. Pressione Enter para encerrar.")  
env.end()

""" 
    status simulation
       pause, resume, stop, arrived, collided, done
       env.status() # get the status of the simulation
       env.status('pause') # pause the simulation
       env.status('resume') # resume the simulation
       env.status('stop') # stop the simulation
       env.status('arrived') # check if the robot has arrived at the goal
       env.status('collided') # check if the robot has collided with an obstacle
       env.status('done') # check if the simulation is done
"""