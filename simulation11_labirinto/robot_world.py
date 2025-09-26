# import lib
import irsim

# criate environment
# file robot_world.yaml configures the environment
# it contains the world, robot, and sensors configurations
env = irsim.make('robot_world.yaml') # initialize the environment with the configuration file

world = env._world # get the world object
world.add_obstacle(type='rect', start_point=[0, 0], end_point=[10, 0.2])  # inferior


for i in range(1000): # run the simulation for 300 steps

    env.step()  # update the environment


    env.render(0.05) # render the environment

    if env.done(): 
        break # check if the simulation is done

print(env.status) # print the status of the simulation
env.end() # close the environment

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