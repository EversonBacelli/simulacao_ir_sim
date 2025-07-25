from no import No
import copy

# Construindo a árvore
noA = No("A", [])
noB = No("B", [])

noC = No("C", [])
noD = No("D", [])
noE = No("E", [])
noF = No("F", [])
noG = No("G", [])
noH = No("H", [])
noI = No("I", [])
noJ = No("J", [])
noK = No("K", [])
noL = No("L", [])
noM = No("M", [])
noN = No("N", [])
noO = No("O", [])

noA.incluirVizinhos([noB, noE])
noB.incluirVizinhos([noC, noD])
noC.incluirVizinhos([noH, noI])
noD.incluirVizinhos([noJ, noK])
noE.incluirVizinhos([noF, noG])
noF.incluirVizinhos([noL, noM])
noG.incluirVizinhos([noN, noO])



def buscarObjetivo(topo):
    pilha = [topo]
    
    # Explorando a pilha
    while pilha:
        estagioAtual = pilha[-1]
       
        if type(estagioAtual) is not list:
            estagioAtual = [estagioAtual]
        
        
        # Validar nós
        next = []
        for no in estagioAtual:
            # print(f"Visitando: {no.valor}")
            if validarNo(no):
                pilha.pop()
                pilha.append(no)
                return pilha
            
            if no.visitado:
                estagioAtual.remove(no)
                continue
            else:
                no.visitado = True
                if len(no.vizinhos) > 0:
                    for filho in no.vizinhos:
                        filho.pai = no
                        next.append(filho)
            
        # criar próximo estágio
        if len(next) > 0:
           pilha.append(next)
                
        
    
                

def validarNo(noAtual):
    if noAtual.valor == "O":
        return True
    

retorno = buscarObjetivo(noA)

# for i in retorno:
#     if type(i) is not list:
#         print(i.valor, end=" -> ")
#     else:
#         for j in i:
#             print(j.valor, end=" -> ")      

inicio = 'A'
caminho = []
fim = noO

controle = False
while controle != True:
    caminho.append(fim)
    
    if fim.valor == inicio:
        controle = True
    fim = fim.pai
for posicao in reversed(caminho):
    print(posicao.valor, end=" -> ")
