import copy
from .no import No, Status
from simulation8_motionDFS.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida
from simulation8_motionDFS.utils.arvore import gerarArvore, printarArvore


def validarObjetivo(atual, objetivo):
    if atual.posicao == objetivo.posicao:
        # print('Objetivo Atingido')
        return True

def menorCaminho(pInicio, pDestino, matriz):
    inicio = matriz[pInicio[0]][pInicio[1]]
    destino = matriz[pDestino[0]][pDestino[1]]
    pilha = [inicio]

    # Enquanto a pilha não estiver vazia
    while pilha:
        atual = pilha[-1]

        if type(atual) is not list:
            atual = [atual]

        next = []
        for no in atual:
            # print(no.posicao)
            # validar o resultado
            if validarNo(no, destino):
                caminho = obterCaminho(no, inicio)
                return caminho
            else: 
                if len(no.vizinhos) > 0 and no.status == Status.NAO_VISITADO: 
                    for vizinho_pos in no.vizinhos:
                        vizinho = matriz[vizinho_pos[0]][vizinho_pos[1]]
                        if vizinho is not None:
                            if no.pai != vizinho:
                                matriz[vizinho_pos[0]][vizinho_pos[1]].pai = no
                                next.append(matriz[vizinho_pos[0]][vizinho_pos[1]])
                no.status = Status.VISITADO
                        

        if len(next) > 0:
            pilha.append(next)



def validarNo(no, destino):
    if no.posicao == destino.posicao:
        return True

def obterCaminho(no, inicio):
    caminho = []
    if no is not None: 
        while True:
            caminho.insert(0, no)
            if no.posicao == inicio.posicao:
                break
            else:
                no = no.pai
    return caminho





