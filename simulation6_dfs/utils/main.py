from .no import No
import numpy
import copy
from .arvore import gerarArvore, printarArvore
from .matriz_obstaculos import gerar_matriz_obstaculos_invertida

No.matriz = gerarArvore(gerar_matriz_obstaculos_invertida())
matriz = No.matriz





def buscarObjetivoIterativo(origem, destino):
    inicio = matriz[origem[0]][origem[1]]
    fim = matriz[destino[0]][destino[1]]
    pilha = [inicio]
    
    if inicio is None or fim is None:
        return None;

    # Enquanto a pilha não estiver vazia
    while pilha:
        # topo da pilha
        atual = pilha[-1] 
        atual.visitado = True
        # print(atual.posicao)

        # Valida se o objetivo foi encontrado
        if atual.posicao == fim.posicao:
            return pilha

        # Explorar Vizinhos
        encontrou_filho = False
        for vizinho_pos in atual.vizinhos:
            vizinho = matriz[vizinho_pos[0]][vizinho_pos[1]]

            if not vizinho.visitado:
                vizinho.visitado = True
                pilha.append(vizinho)
                encontrou_filho = True
                break  # vai para esse vizinho antes de explorar outros
        
        # Caso nenhum vizinho valido seja encontrado
        if not encontrou_filho:
            pilha.pop()      # volta

    return None


# Executar a busca


def algDfs(origem, destino):
    caminho = []
    resultado = buscarObjetivoIterativo(origem, destino)
    if resultado is not None:
        for no in resultado:
            caminho.append(no.posicao)

    No.matriz = gerarArvore(gerar_matriz_obstaculos_invertida())

   
    return caminho



# if resultado:
#     print("\nCaminho até o objetivo:")
#     for end in resultado:
#         print(end.posicao, end=',')
#     print()
#     print(len(resultado))
# else:
#     print("Objetivo não encontrado")



