from .no import No, Status
import numpy
import copy
from .arvore import gerarArvore, printarArvore
from .matriz_obstaculos import gerar_matriz_obstaculos_invertida


def algoritmoDFS(origem, destino, matriz):
   
    inicio = matriz[origem[0]][origem[1]]
    fim = matriz[destino[0]][destino[1]]
    pilha = [inicio]
    consultados = 1
    caminho = [inicio]
    if inicio is None or fim is None:
        return pilha;

    # Enquanto a pilha não estiver vazia
    while pilha:
        # topo da pilha
        atual = pilha[-1] 
        atual.visitado = True
 
        # Valida se o objetivo foi encontrado
        if consultados == 835:
            return caminho

        # Explorar Vizinhos
        encontrou_filho = False
        for vizinho_pos in atual.vizinhos:
            vizinho = matriz[vizinho_pos[0]][vizinho_pos[1]]
            if vizinho is not None:
                if vizinho.status == Status.NAO_VISITADO:
                    vizinho.status = Status.VISITADO
                    pilha.append(vizinho)
                    caminho.append(vizinho)
                    consultados += 1
                    encontrou_filho = True
                    break 

        # Caso nenhum vizinho valido seja encontrado
        if not encontrou_filho:
            pilha.pop()      # volta
    



# def algDfs(origem, destino):
#     caminho = []
#     env = buscarObjetivoIterativo(origem, destino)
#     for linha in No.matriz:
#         for no in linha:
#             if no is not None:
#                 no.visitado = False
#     return env