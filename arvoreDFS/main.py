from no import No
import copy

# Nós
from no import No, Status
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

noA.incluirVizinhos([noB, noC])
noB.pai = noA
noC.pai = noA
noB.incluirVizinhos([noD, noE])
noD.pai = noB
noE.pai = noB
noC.incluirVizinhos([noF, noG])
noF.pai = noC
noG.pai = noC
noD.incluirVizinhos([noH, noI])
noH.pai = noD
noI.pai = noD
noE.incluirVizinhos([noJ, noK])
noJ.pai = noE
noK.pai = noE
noF.incluirVizinhos([noL, noM])
noL.pai = noF
noM.pai = noF
noG.incluirVizinhos([noN, noO])
noN.pai = noG
noO.pai = noG

def validarNo(no):
    if no.valor == "O":
        return True
    return False

atual = noA
numeroVisitas = 0


while True:
    
    if atual.status == Status.NAO_VISITADO:
        #print(atual.valor)
        atual.status = Status.VISITADO
        numeroVisitas += 1
        if validarNo(atual):
            print(f"Encontrado: {atual.valor}")
            break
        if len(No.NOS) == numeroVisitas:
            print("Objetivo não encontrado")
    else:
        print(atual.valor)

        nos_a_visitar = False
        for vizinho in atual.vizinhos:
            if vizinho.status == Status.NAO_VISITADO:
                nos_a_visitar = True
                atual = vizinho
                break
    
    if atual.pai is not None and not nos_a_visitar:
        atual = atual.pai

        

            

   


