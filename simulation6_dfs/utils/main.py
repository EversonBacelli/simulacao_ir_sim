from no import No
import copy
from arvore import gerarArvore, printarArvore



No.matriz = gerarArvore(No.matriz)
matriz = No.matriz



# printarArvore(No.matriz)

# objetivo
matriz[46][15].valor = "C"


origem = matriz[4][4]



def buscarObjetivoIterativo(inicio):
    pilha = [inicio]
    caminho = []

    while pilha:
        atual = pilha[-1]  # topo da pilha
        atual.visitado = True
        caminho.append(atual)
        # print(atual.posicao)

        if atual.valor == 'C':
            return copy.deepcopy(caminho)

        encontrou_filho = False
        for vizinho_pos in atual.vizinhos:
            vizinho = matriz[vizinho_pos[0]][vizinho_pos[1]]

            if not vizinho.visitado:
                vizinho.visitado = True
                pilha.append(vizinho)
                encontrou_filho = True
                break  # vai para esse vizinho antes de explorar outros

        if not encontrou_filho:
            pilha.pop()      # volta
            caminho.pop()    # remove do caminho atual

    return None


# Executar a busca
resultado = buscarObjetivoIterativo(origem)

if resultado:
    print("\nCaminho até o objetivo:")
    for end in resultado:
        print(end.posicao, end='')
else:
    print("Objetivo não encontrado")



