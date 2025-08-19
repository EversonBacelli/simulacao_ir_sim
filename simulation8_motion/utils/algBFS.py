import copy
from .no import No, Status



def validarObjetivo(nos_consultado):
    if nos_consultado == 835:
        # print('Objetivo Atingido')
        return True

# Buscar vizinhos - descer na hierarquia da árvore
def consultarVizinhos(vizinho_nao_visitado, vizinho_a_explorar, no_resp):
    if no_resp.status == Status.VISITADO:
        # Acessar vizinhos não visitados
        for vizinho_pos in no_resp.vizinhos:
            vizinho = No.matriz[vizinho_pos[0]][vizinho_pos[1]]
            if vizinho is None:
                no_resp.vizinhos.remove(vizinho_pos)
                continue

            if vizinho.status == Status.NAO_VISITADO:
                vizinho_nao_visitado = True
                vizinho_a_explorar = True
                no_resp.visitas += 1
                no_resp = vizinho
                return vizinho_nao_visitado, vizinho_a_explorar, no_resp
                
        # Se os Nós já foram visitados
        if not vizinho_nao_visitado:
            if no_resp.continuarVisitas():
                for vizinho_pos in no_resp.vizinhos:
                    vizinho = No.matriz[vizinho_pos[0]][vizinho_pos[1]]
                    if vizinho is None:
                        no_resp.vizinhos.remove(vizinho_pos)
                        continue

                    if vizinho.continuarVisitas():
                        vizinho_a_explorar = True
                        vizinho_nao_visitado = True
                        no_resp.visitas += 1
                        no_resp = vizinho
                        return vizinho_nao_visitado, vizinho_a_explorar, no_resp
    
    # retorna o nó atual
    return vizinho_nao_visitado, vizinho_a_explorar, no_resp

def algoritmoBFS(no_inicial, no_final, matriz):
    m = matriz[45][45]
    nos_visitados = []
    # Primeiro Nó

    inicio = matriz[no_inicial[0]][no_inicial[1]]
    atual = matriz[no_inicial[0]][no_inicial[1]]
    objetivo = matriz[no_final[0]][no_final[1]]

    listaBFS = []
    # Condição de Parada
    nos_consultados = 0
    
    while True:

        if not atual.continuarVisitas() and atual.posicao == inicio.posicao:
            for no in nos_visitados:
                no.visitas = 0
            # print('##### Numero de Visitados #####: ', nos_consultados)
            # print('', end='')
            

        if atual.status == Status.NAO_VISITADO:
            nos_consultados += 1
            # print(atual.posicao, '--' , atual.status)
            listaBFS.append(atual)
            if validarObjetivo(nos_consultados):
                return listaBFS
                # break
            if len(atual.vizinhos) == 0:
                atual.status = Status.BLOQUEADO
                atual = atual.pai
                continue
            else:
                atual.status = Status.VISITADO
                nos_visitados.append(atual)
                if atual.pai is not None:
                    atual = atual.pai
                    continue
        # if nos_consultados == len(No.NOS):
        #     print('Todos os nós foram consultados')
        #     break
        else:
            # print(atual.posicao, '--' , atual.status)

            vizinho_nao_visitado, vizinho_a_explorar, no_resp = consultarVizinhos(False, False, atual)
            if atual.posicao != no_resp.posicao:
                if no_resp.posicao != atual.pai:
                    no_resp.incluirPai(atual)
                    atual = no_resp
                    continue

            # subir na hierarquia + Condição de parada       
            if not vizinho_nao_visitado or not vizinho_a_explorar:
                if atual.pai is not None:
                        atual = atual.pai

 





# Exemplo de uso com coordenadas iniciais e finais
# def algoritmoBFS(origem, destino, env):
    

#     for linha in matriz:
#         for no in linha:
#             if no is not None:
#                 no.visitado = False
#                 no.pai = None

#     return



