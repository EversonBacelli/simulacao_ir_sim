import time, os, psutil, tracemalloc, copy

from sim_12_lab_DFS.src.stage1_abstracao.algDFS import algoritmoDFS

def definirNos(m):
     inicio = [15, 15]    # 5 , 15
     # Stage 1 - Algoritmo de Mapeamento do Ambiente com BFS
     processoS1 = psutil.Process(os.getpid())
     tracemalloc.start()
     inicioProcess = time.process_time()
     inicioDFS = time.time()
     DFS = algoritmoDFS(inicio, m)  
     fimDFS = time.time()
     timeDFS = fimDFS - inicioDFS
     fimProcess = time.process_time()
     memoriaS1 = processoS1.memory_info().rss / 1024**2
     men_atual, men_pico = tracemalloc.get_traced_memory()
     men_atual_s1 = men_atual
     men_pico_s1 = men_pico
     tracemalloc.stop()

     return inicioDFS, fimDFS, memoriaS1, men_atual_s1, m, timeDFS, inicioProcess, fimProcess, men_pico_s1, DFS