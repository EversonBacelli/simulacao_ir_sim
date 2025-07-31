import copy
from .arvore import gerarArvore, printarArvore
from .no import No
from .matriz_obstaculos import gerar_matriz_obstaculos_invertida

No.matriz = gerarArvore(No.matriz)
matriz = No.matriz


# printarArvore(No.matriz)
# objetivo

# origem.pai = matriz[3][4]


def varredura(inicio, destino):
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
                pilha.pop()
                pilha.append(no)
                return pilha
            else: 
                
                if len(no.vizinhos) > 0 and no.visitado == False : 
                    for vizinho_pos in no.vizinhos:
                        if no.pai != matriz[vizinho_pos[0]][vizinho_pos[1]]:
                            matriz[vizinho_pos[0]][vizinho_pos[1]].pai = no
                            next.append(matriz[vizinho_pos[0]][vizinho_pos[1]])
                no.visitado = True
        if len(next) > 0:
            pilha.append(next)

def validarNo(no, destino):
    if no.posicao == destino.posicao:
        return True
    
def algoritmoBFS(origem, destino):
    retorno = varredura(origem, destino)
    caminho = []
    obj = retorno[-1]
    while True:
        caminho.append(obj.posicao)
        
        if obj.posicao == origem.posicao:
            break;
        obj = obj.pai

    Rcaminho = list(reversed(caminho)) 
    return Rcaminho



