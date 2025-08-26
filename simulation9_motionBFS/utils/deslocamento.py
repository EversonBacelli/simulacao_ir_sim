from simulation9_motionBFS.utils.main import menorCaminho
from simulation9_motionBFS.utils.no import No, Status


def remontarLista(pontoInicial, lista):
    while True:
        objeto = lista.pop(0)
        lista.append(objeto)
        if lista[0].posicao == pontoInicial:
            break
    
    return lista

def motionRobot(objetivo, list, inicio, m):
    obj = objetivo
    listaDeNos = remontarLista(inicio, list)
    
    objetivo_atingido = False
    nos = []

    while True:
        # print(len(listaDeNos))
        atual = listaDeNos[0]
        proximo = listaDeNos[1]

        # validar posicao
        if atual.posicao == obj:
            nos.append(atual)
            return nos
        elif len(listaDeNos) > 0:
            posicaoInicial = atual.posicao 
            posicaoFinal = proximo.posicao 
            # print(posicaoInicial, '--->', posicaoFinal) 
            caminho, m = menorCaminho(posicaoInicial, posicaoFinal , m)
            topo = caminho.pop()
            for no in caminho:
                nos.append(no)
            listaDeNos.pop(0)
            for item in nos:
                item.status = Status.NAO_VISITADO
                item.pai = None
            topo.status = Status.NAO_VISITADO
            topo.pai = None
        else: 
            print('Objetivo Não encontrado')
            break
    