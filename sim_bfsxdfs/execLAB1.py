# importações
import json

# from sim_bfsxdfs.src.cenarios.cenarioTeste import buscarObjetivosCenarioTeste
from sim_bfsxdfs.src.main.definirNos import definirNos
from sim_bfsxdfs.src.classes.no import No
from sim_bfsxdfs.src.classes.estatistica import Estatistica
from sim_bfsxdfs.src.stage1_abstracao.arvore import gerarArvore

from sim_bfsxdfs.src.stage2_movimentacao.deslocamento import definirMapa
from sim_bfsxdfs.src.main.buscarObjetivos import varrerMapa
from sim_bfsxdfs.contexto import definirCenario
######
inicio, numero_de_nos_livres, matriz, goals, diretorio = definirCenario(1)

No.matriz_binaria = matriz
No.matriz = gerarArvore(matriz)
m = No.matriz
No.retirarVizinhosNulos()

# stage 1 - ordenar os nós


#inicioDFS, fimDFS, memoriaS1, men_atual_s1, m, timeDFS, inicioProcess, fimProcess, men_pico_s1, DFS = definirNos(m, inicio, numero_de_nos_livres)
inicioBFS, fimBFS, memoriaS1, men_atual_s1, m, timeBFS, inicioProcess, fimProcess, men_pico_s1, BFS = definirNos(m, inicio, numero_de_nos_livres)

# print(len(DFS), " nós foram ordenados pelo DFS.")

# for linha in m:
#     for no in linha:
#         if no is not None:
#             print(no.posicao , ' --> ', no.equivalente, "  -  ", no.valor )

# # stage 2 - buscar os objetivos
definirMapa(diretorio)
#varrerMapa(goals, inicio, m, DFS, inicioDFS, fimDFS, men_atual_s1, memoriaS1)
varrerMapa(goals, inicio, m, BFS, inicioBFS, fimBFS, men_atual_s1, memoriaS1)


# Printr Resultado
input('Aperte qualquer coisa para finalizar')
lista_dict = [p.__dict__ for p in Estatistica.resultado]
json_result = json.dumps(lista_dict, ensure_ascii=False, indent=4)
print(json_result)




