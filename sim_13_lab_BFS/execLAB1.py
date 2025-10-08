# importações
import time, os, psutil, tracemalloc, copy
import random
import math, json
import irsim
from sim_13_lab_BFS.src.cenarios.cenario1 import buscarObjetivosCenario1
from sim_13_lab_BFS.src.cenarios.cenarioTeste import buscarObjetivosCenarioTeste
from sim_13_lab_BFS.src.main.definirNos import definirNos
from sim_13_lab_BFS.src.classes.no import No, Status
from sim_13_lab_BFS.src.classes.estatistica import Estatistica
from sim_13_lab_BFS.src.stage1_abstracao.arvore import gerarArvore

from sim_13_lab_BFS.src.stage2_movimentacao.deslocamento import motionRobot
from sim_13_lab_BFS.src.main.buscarObjetivos import varrerMapa
from sim_13_lab_BFS.src.matriz.labirinto1 import gerarMatrizLab1
from sim_13_lab_BFS.src.matriz.teste import getMatrizTeste
###### 

matriz = getMatrizTeste()
No.matriz_binaria = matriz
No.matriz = gerarArvore(matriz)
m = No.matriz

goals = buscarObjetivosCenarioTeste()
No.retirarVizinhosNulos()
# print(f"DEBUG (definirNos.py): ID da classe No é {id(No)}")


# stage 1 - ordenar os nós
inicioBFS, fimBFS, memoriaS1, men_atual_s1, m, timeBFS, inicioProcess, fimProcess, men_pico_s1, BFS = definirNos(m)



# for linha in m:
#     for no in linha:    
#         if no is not None and no.equivalente[1] == 19:
#             print(no.posicao , ' --> ', no.equivalente, "  -  ", no.valor )





# # stage 2 - buscar os objetivos
inicio = [15, 15]
varrerMapa(goals, inicio, m, BFS, inicioBFS, fimBFS, men_atual_s1, memoriaS1)



# input('Aperte qualquer coisa para finalizar')
# lista_dict = [p.__dict__ for p in Estatistica.resultado]
# json_result = json.dumps(lista_dict, ensure_ascii=False, indent=4)
# print(json_result)




