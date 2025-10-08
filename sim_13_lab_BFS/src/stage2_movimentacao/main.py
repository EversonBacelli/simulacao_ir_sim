import copy
from sim_13_lab_BFS.src.classes.no import No, Status


def validarObjetivo(atual, objetivo):
    if atual.posicao == objetivo.posicao:
        # print('Objetivo Atingido')
        return True

def menorCaminho(pInicio, pDestino, m):
    inicio = m[pInicio[0]][pInicio[1]]
    destino = m[pDestino[0]][pDestino[1]]
    pilha = [inicio]

    # Enquanto a pilha não estiver vazia
    while pilha:
        atual = pilha[-1]

        if type(atual) is not list:
            atual = [atual]
            pilha = [atual]
        next = []
        for no in atual:
            # print(no.posicao)
            # validar o resultado
            if validarNo(no, destino):
                for stage in pilha:
                    for n in stage:
                        n.status = Status.NAO_VISITADO
                        #n.pai = None
                caminho = obterCaminho(no, inicio)
                return caminho, m
            else: 
                if len(no.vizinhos) > 0 and no.status == Status.NAO_VISITADO: 
                    for vizinho_pos in no.vizinhos:
                        vizinho = m[vizinho_pos[0]][vizinho_pos[1]]
                        if vizinho is not None:
                            if no.pai != vizinho:
                                vizinho.pai = no
                            next.append(vizinho)
                no.status = Status.VISITADO
                        

        if len(next) > 0:
            # for no in next:
            #     no.status = Status.NAO_VISITADO
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





