from .no import No, Status
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



def validarObjetivo(atual):
    if atual.valor == 'O':
        print('Objetivo Alcançado')
        return True




atual = noA

pilha = [noA]

while True:

    if not pilha[0].status != Status.BLOQUEADO:
        print('Objetivo não alcançado')
        break
    elif not noA.continuarVisitas() and atual.valor == 'A':
        for no in No.NOS:
            no.visitas = 0

    if atual.status == Status.NAO_VISITADO:
        print(atual.valor, '--' , atual.status )
        if validarObjetivo(atual):
            break
        atual.status = Status.VISITADO
        if atual.pai is not None:
            atual = atual.pai
    else:
        print(atual.valor, '--' , atual.status )
        # Verificar se apesar de não ser o alvo
        # Possui vizinhos
        if len(atual.vizinhos) == 0:
            atual.status = Status.BLOQUEADO
            anterior = atual
            atual = atual.pai
            continue
        
        # Voltar
        if atual.status == Status.BLOQUEADO:
            print(atual.valor, '--' , atual.status, '--', atual.visitas )
            anterior = atual
            atual = atual.pai

        vizinho_nao_visitado = False
        vizinho_a_explorar = False
        numero_bloqueados = 0

        if atual.status == Status.VISITADO:
        # Acessar vizinhos não visitados
            for vizinho in atual.vizinhos:
                if vizinho.status == Status.NAO_VISITADO:
                    vizinho_nao_visitado = True
                    vizinho_a_explorar = True
                    atual.visitas += 1
                    atual = vizinho
                    break
            
            # Se os Nós já foram visitados
            if not vizinho_nao_visitado:
                if atual.continuarVisitas():
                    for vizinho in atual.vizinhos:
                        if vizinho.continuarVisitas():
                            vizinho_a_explorar = True
                            vizinho_nao_visitado = True
                            atual.visitas += 1
                            atual = vizinho
                            break
            
        
        
        # subir na hierarquia + Condição de parada       
        if not vizinho_nao_visitado or not vizinho_a_explorar:
           if atual.pai is not None:
                atual = atual.pai
        

        
     


