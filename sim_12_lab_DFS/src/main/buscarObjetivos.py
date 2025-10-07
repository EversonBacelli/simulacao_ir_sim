import time, os, psutil, tracemalloc, copy
import irsim
from sim_12_lab_DFS.src.classes.no import No, Status
from sim_12_lab_DFS.src.stage2_movimentacao.deslocamento import motionRobot
from sim_12_lab_DFS.src.classes.estatistica import Estatistica

def varrerMapa(goals, inicio, m, DFS, inicioDFS, fimDFS, men_atual_s1, memoriaS1):

    for go in goals:
        # print('-- inicio do processo -- : ', go)
        m = No.resetMatriz(m) 
        tracemalloc.start()
        processoS2 = psutil.Process(os.getpid())
        execDFSinicio = time.time()
        execProcessInicio = time.process_time()
        execBFSinicio = time.time()
        nos = motionRobot(go, copy.deepcopy(DFS), inicio, m)
       
        inicio = go
        execDFSfim = time.time()
        execProcessFim = time.process_time()
        memoriaS2 = processoS2.memory_info().rss / 1024**2
        men_atual, men_pico = tracemalloc.get_traced_memory()
        men_atual_s2 = men_atual
        men_pico_s2 = men_pico

        # Dados
        timeDFS = fimDFS - inicioDFS
        execDFS = execDFSfim - execDFSinicio
        tempoDeCiclo = execDFSfim - inicioDFS
        totalRAM = men_atual_s1 + men_atual_s2
       
        Estatistica(nos[0], nos[-1], timeDFS, memoriaS1, men_atual_s1, execDFS, men_atual_s2, men_pico_s2, len(nos), tempoDeCiclo, totalRAM)

       