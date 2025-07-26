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



def arvore_dfs(topo):
    pilha = [topo]
    
    while pilha:
        atual = pilha[-1]
        if atual.valor == 8:
            novaPilha = copy.deepcopy(pilha)
            return novaPilha

        encontrou_filho = False
        vizinhos = atual.vizinhos
        for vizinho in vizinhos:
            if vizinho.visitado == False:
                vizinho.visitado = True
                encontrou_filho = True
                pilha.append(vizinho)
                break;
        
        if not encontrou_filho:
            pilha.pop()


# Executar a busca
resultado = arvore_dfs(noA)

if resultado:
    print("\nCaminho até o objetivo:")
    print([no.valor for no in resultado])
else:
    print("Objetivo não encontrado")