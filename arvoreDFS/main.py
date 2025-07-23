from no import No
import copy

# Nós
noC = No(4, [])
noD = No(3, [])

noF = No(1, [])
noB = No(5, [noC, noD, noF])
noG = No(8, [])
noE = No(2, [noF, noG])
noA = No(10, [noB, noE])

pilha = [noA]

def arvore_dfs(pilha):
    print(pilha[-1].valor)
    pilha[-1].visitado = True

    if pilha[-1].valor == 8:
        novaPilha = copy.deepcopy(pilha)
        return novaPilha
    else:
        if len(pilha[-1].vizinhos) == pilha[-1].numeroVisitas:
            pilha.pop()
            if pilha:  # Precisa checar se ainda há elementos
                return arvore_dfs(pilha)
            else:
                return None
        else:
            return buscarFilhos(pilha)

def buscarFilhos(pilha):
    vizinhos = pilha[-1].vizinhos
    for vizinho in vizinhos:
        if not vizinho.visitado:
            pilha[-1].numeroVisitas += 1
            vizinho.visitado = True
            pilha.append(vizinho)
            return arvore_dfs(pilha)
    return arvore_dfs(pilha)  # Se todos já foram visitados, tenta continuar

# Executar a busca
resultado = arvore_dfs(pilha)

if resultado:
    print("\nCaminho até o objetivo:")
    print([no.valor for no in resultado])
else:
    print("Objetivo não encontrado")
