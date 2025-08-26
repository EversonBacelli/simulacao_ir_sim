import copy
from .no import No, Status

from simulation9_motionBFS.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from simulation9_motionBFS.utils.arvore import gerarArvore, printarArvore


# matriz = No.matriz

def algoritmoBFS(pInicio, matriz):
    inicio = matriz[pInicio[0]][pInicio[1]]
    pilha = [inicio]
    caminho = [inicio]


    # Enquanto a pilha não estiver vazia
    while pilha:
        atual = pilha[-1]

        if type(atual) is not list:
            atual = [atual]

        next = []
        for no in atual:
            # print(no.posicao)
            # validar o resultado
            if validarNo(caminho):
                return caminho
            else: 
                if len(no.vizinhos) > 0 and no.status == Status.NAO_VISITADO: 
                    for vizinho_pos in no.vizinhos:
                        vizinho = matriz[vizinho_pos[0]][vizinho_pos[1]]
                        if vizinho is not None:
                            if no.pai != vizinho and vizinho.pai is None:
                                if vizinho.status != Status.VISITADO and vizinho not in next:
                                    caminho.append(vizinho)
                                matriz[vizinho_pos[0]][vizinho_pos[1]].pai = no
                                next.append(matriz[vizinho_pos[0]][vizinho_pos[1]])
                no.status = Status.VISITADO
                
                        
        if len(next) > 0:
            pilha.append(next)



def validarNo(caminho):
    if len(caminho) == 835:
        return True
    