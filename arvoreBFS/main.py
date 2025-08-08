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


def validarObjetivo(atual):
    if atual.valor == 'O':
        print('Objetivo Alcançado')
        return True

# Buscar vizinhos - descer na hierarquia da árvore
def consultarVizinhos(vizinho_nao_visitado, vizinho_a_explorar, no_resp):
    if no_resp.status == Status.VISITADO:
        # Acessar vizinhos não visitados
        for vizinho in no_resp.vizinhos:
            if vizinho.status == Status.NAO_VISITADO:
                vizinho_nao_visitado = True
                vizinho_a_explorar = True
                no_resp.visitas += 1
                no_resp = vizinho
                return vizinho_nao_visitado, vizinho_a_explorar, no_resp
                
        # Se os Nós já foram visitados
        if not vizinho_nao_visitado:
            if no_resp.continuarVisitas():
                for vizinho in no_resp.vizinhos:
                    if vizinho.continuarVisitas():
                        vizinho_a_explorar = True
                        vizinho_nao_visitado = True
                        no_resp.visitas += 1
                        no_resp = vizinho
                        return vizinho_nao_visitado, vizinho_a_explorar, no_resp
    
    # retorna o nó atual
    return vizinho_nao_visitado, vizinho_a_explorar, no_resp

def algoritmoBFS(no_inicial):
    # Primeiro Nó
    atual = no_inicial

    # Condição de Parada
    nos_consultados = 0

    while True:
        if not noA.continuarVisitas() and atual.valor == 'A':
            for no in No.NOS:
                no.visitas = 0

        if atual.status == Status.NAO_VISITADO:
            nos_consultados += 1
            print(atual.valor, '--' , atual.status, ' -- ', len(atual.vizinhos) )
            if validarObjetivo(atual):
                break
            if len(atual.vizinhos) == 0:
                atual.status = Status.BLOQUEADO
                anterior = atual
                atual = atual.pai
                continue
            else:
                atual.status = Status.VISITADO
                if atual.pai is not None:
                    atual = atual.pai
        if nos_consultados == len(No.NOS):
            print('Todos os nós foram consultados')
            break
        else:
            print(atual.valor, '--' , atual.status )

            # Voltar
            if atual.status == Status.BLOQUEADO:
                print(atual.valor, '--' , atual.status, '--', atual.visitas )
                atual = atual.pai
                continue

            vizinho_nao_visitado, vizinho_a_explorar, no_resp = consultarVizinhos(False, False, atual)
            if atual.valor != no_resp.valor:
                atual = no_resp
                continue

            # subir na hierarquia + Condição de parada       
            if not vizinho_nao_visitado or not vizinho_a_explorar:
                if atual.pai is not None:
                        atual = atual.pai


algoritmoBFS(noA)
     


