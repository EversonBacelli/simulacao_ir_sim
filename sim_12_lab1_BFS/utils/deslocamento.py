import irsim
from sim_12_lab1_BFS.utils.main import menorCaminho
from sim_12_lab1_BFS.utils.no import No, Status


env = irsim.make('/sim_12_lab1_BFS/utils/lab1_world.yaml')
controle = False
collision = 0
arrived = 0




def remontarLista(pontoInicial, lista):
    while True:
        objeto = lista.pop(0)
        lista.append(objeto)
        if lista[0].posicao == pontoInicial:
            break
    
    return lista

def motionRobot(objetivo, list, inicio, m):
    obj = objetivo
    # Definir Objetivo no IR-SIM
    definirObjetivo(obj, m)
    
    listaDeNos = remontarLista(inicio, list)
    eq = m[inicio[0]][inicio[1]]
    movimentacaoIR_SIM(eq)

    objetivo_atingido = False
    nos = []

    while True:
        # print(len(listaDeNos))
        atual = listaDeNos[0]
        proximo = listaDeNos[1]

        # validar posicao
        if atual.posicao == obj:
            movimentacaoIR_SIM(atual)
            print("Objetivo Alcançado: ", end=' ')
            print(atual.posicao)
            # env.end()
            nos.append(atual)
            return nos
        elif len(listaDeNos) > 0:
            posicaoInicial = atual.posicao 
            posicaoFinal = proximo.posicao 
            # print(posicaoInicial, '--->', posicaoFinal) 
            caminho, m = menorCaminho(posicaoInicial, posicaoFinal , m)
            topo = caminho.pop()
            #movimentacaoIR_SIM(topo)
            for no in caminho:
                movimentacaoIR_SIM(no)
                nos.append(no)
                # nos = inserirNaLista(nos, no)
            listaDeNos.pop(0)
            for item in nos:
                item.status = Status.NAO_VISITADO
                item.pai = None
            topo.status = Status.NAO_VISITADO
            topo.pai = None
        else: 
            print('Objetivo Não encontrado')
            break

def definirObjetivo(objetivo, m):
    equivalente = m[objetivo[0]][objetivo[1]].equivalente
    # equivalente = m[objetivo[0]][objetivo[1]].posicao
    env.robot.set_goal(equivalente)
    env.step()
    env.render(figure_kwargs={'dpi': 100})

def movimentacaoIR_SIM(no):
    posicao = no.equivalente
    # posicao = no.posicao

    # set robot position
    env.robot._state[0] = posicao[0] 
    env.robot._state[1] = posicao[1]
    env.step()
    env.render(figure_kwargs={'dpi': 100})


def inserirNaLista(lista, no):
    if no not in lista:
        lista.append(no)
    return lista