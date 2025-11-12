# importações
import time, os, psutil, tracemalloc, copy
import random
import math, json
import irsim

# Modulos Internos
from sim_12_lab_DFS.src.cenarios.listaDeObjetivos import buscarObjetivosCenarioTeste
from sim_12_lab_DFS.src.main.definirNos import definirNos
from sim_12_lab_DFS.src.classes.no import No, Status
from sim_12_lab_DFS.src.classes.estatistica import Estatistica
from sim_12_lab_DFS.src.stage1_abstracao.arvore import gerarArvore

from sim_12_lab_DFS.src.stage2_movimentacao.deslocamento import motionRobot
from sim_12_lab_DFS.src.main.buscarObjetivos import varrerMapa
from sim_12_lab_DFS.src.matriz.teste import getMatrizTeste
from sim_12_lab_DFS.src.mapas.mapa_20x20.matriz_referencia_20x20 import getMatriz20x20_15, getMatriz20x20_30, getMatriz20x20_45
from sim_12_lab_DFS.src.mapas.mapa_30x30.matriz_referencia_30x30 import getMatriz30x30_15, getMatriz30x30_30, getMatriz30x30_45
from sim_12_lab_DFS.src.mapas.mapa_40x40.matriz_referencia_40x40 import getMatriz40x40_15, getMatriz40x40_30, getMatriz40x40_45
from sim_12_lab_DFS.src.mapas.mapa_50x50.matriz_referencia_50x50 import getMatriz50x50_15, getMatriz50x50_30, getMatriz50x50_45
#####

matriz = getMatriz50x50_45()
No.matriz_binaria = matriz
No.matriz = gerarArvore(matriz)
m = No.matriz

goals = buscarObjetivosCenarioTeste()
No.retirarVizinhosNulos()
# print(f"DEBUG (definirNos.py): ID da classe No é {id(No)}")


# stage 1 - ordenar os nós
inicioDFS, fimDFS, memoriaS1, men_atual_s1, m, timeDFS, inicioProcess, fimProcess, men_pico_s1, DFS = definirNos(m)



for linha in m:
    for no in linha:    
        if no is not None:
            print(no.posicao , ' --> ', no.equivalente, "  -  ", no.valor )
print(len(No.NOS))
print(len(m))



# stage 2 - buscar os objetivos
inicio = [15, 15]

# varrerMapa(goals, inicio, m, DFS, inicioDFS, fimDFS, men_atual_s1, memoriaS1)



# input('Aperte qualquer coisa para finalizar')
# lista_dict = [p.__dict__ for p in Estatistica.resultado]
# json_result = json.dumps(lista_dict, ensure_ascii=False, indent=4)
# print(json_result)




