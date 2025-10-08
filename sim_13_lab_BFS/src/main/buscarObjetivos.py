import time, os, psutil, tracemalloc, copy
import irsim
from sim_13_lab_BFS.src.classes.no import No, Status
from sim_13_lab_BFS.src.stage2_movimentacao.deslocamento import motionRobot
from sim_13_lab_BFS.src.classes.estatistica import Estatistica

def varrerMapa(goals, inicio, m, BFS, inicioBFS, fimBFS, men_atual_s1, memoriaS1):

    for go in goals:
        # print('-- inicio do processo -- : ', go)
        m = No.resetMatriz(m) 
        tracemalloc.start()
        processoS2 = psutil.Process(os.getpid())
        execDFSinicio = time.time()
        execProcessInicio = time.process_time()
        execBFSinicio = time.time()
        nos = motionRobot(go, copy.deepcopy(BFS), inicio, m)
       
        inicio = go
        execBFSfim = time.time()
        execProcessFim = time.process_time()
        memoriaS2 = processoS2.memory_info().rss / 1024**2
        men_atual, men_pico = tracemalloc.get_traced_memory()
        men_atual_s2 = men_atual
        men_pico_s2 = men_pico

        # Dados
        timeBFS = fimBFS - inicioBFS
        execBFS = execBFSfim - execBFSinicio
        tempoDeCiclo = execBFSfim - inicioBFS
        totalRAM = men_atual_s1 + men_atual_s2
       
        Estatistica(nos[0], nos[-1], timeBFS, memoriaS1, men_atual_s1, execBFS, men_atual_s2, men_pico_s2, len(nos), tempoDeCiclo, totalRAM)

       