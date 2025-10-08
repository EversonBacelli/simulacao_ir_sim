import time, os, psutil, tracemalloc, copy

from sim_13_lab_BFS.src.stage1_abstracao.algBFS import algoritmoBFS

def definirNos(m):
     inicio = [15, 15]    # 5 , 15
     # Stage 1 - Algoritmo de Mapeamento do Ambiente com BFS
     processoS1 = psutil.Process(os.getpid())
     tracemalloc.start()
     inicioProcess = time.process_time()
     inicioBFS = time.time()
     BFS = algoritmoBFS(inicio, m)  
     fimBFS = time.time()
     timeBFS = fimBFS - inicioBFS
     fimProcess = time.process_time()
     memoriaS1 = processoS1.memory_info().rss / 1024**2
     men_atual, men_pico = tracemalloc.get_traced_memory()
     men_atual_s1 = men_atual
     men_pico_s1 = men_pico
     tracemalloc.stop()

     return inicioBFS, fimBFS, memoriaS1, men_atual_s1, m, timeBFS, inicioProcess, fimProcess, men_pico_s1, BFS