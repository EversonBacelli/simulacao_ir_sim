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
    

    # Enquanto a pilha não estiver vazia
    while pilha:
        # topo da pilha
        atual = pilha[-1] 
        atual.visitado = True
        # print(atual.posicao)

        # Valida se o objetivo foi encontrado
        if atual.valor == 'C':
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
resultado = buscarObjetivoIterativo(origem)

if resultado:
    print("\nCaminho até o objetivo:")
    for end in resultado:
        print(end.posicao, end=',')
else:
    print("Objetivo não encontrado")



