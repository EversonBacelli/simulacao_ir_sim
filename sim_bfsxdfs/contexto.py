# número de nós Livres em cada mapa
    # 20x20_15: 204, 20x20_30: 209, 20x20_45: 214
    # 30x30_15: 461, 30x30_30: 472 , 30x30_45: 479
    # 40x40_15: 815, 40x40_30: 838 , 40x40_45: 855


# Cenários de Busca no Espaço
from sim_bfsxdfs.src.cenarios.cenario1 import buscarCenario20x20_15, buscarCenario20x20_30, buscarCenario20x20_45
from sim_bfsxdfs.src.cenarios.cenario2 import buscarCenario30x30_15, buscarCenario30x30_30, buscarCenario30x30_45
from sim_bfsxdfs.src.cenarios.cenario3 import buscarCenario40x40_15, buscarCenario40x40_30, buscarCenario40x40_45

# Mapas
from sim_bfsxdfs.src.matriz.mapa_20x20.matriz20x20 import getMatriz20x20_15, getMatriz20x20_30, getMatriz20x20_45
from sim_bfsxdfs.src.matriz.mapa_30x30.matriz30x30 import getMatriz30x30_15, getMatriz30x30_30, getMatriz30x30_45
from sim_bfsxdfs.src.matriz.mapa_40x40.matriz40x40 import getMatriz40x40_15, getMatriz40x40_30, getMatriz40x40_45


def definirCenario(opc):
    inicio, matriz, goals, diretorio = None, None, None, None
    if opc == 1:
        inicio = [15, 15]
        numero_de_nos_livres = 204
        matriz = getMatriz20x20_15()
        goals = buscarCenario20x20_15()
        diretorio = 'mapa_20x20/mapa20x20_15.yaml'
    elif opc == 2:
        inicio = [15, 15]
        numero_de_nos_livres = 209
        matriz = getMatriz20x20_30()
        goals = buscarCenario20x20_30()
        diretorio = 'mapa_20x20/mapa20x20_30.yaml'
    elif opc == 3:
        inicio = [15, 15]
        numero_de_nos_livres = 214
        matriz = getMatriz20x20_45()
        goals = buscarCenario20x20_45()
        diretorio = 'mapa_20x20/mapa20x20_45.yaml'
    elif opc == 4:
        inicio = [15, 15]
        numero_de_nos_livres = 461  
        matriz = getMatriz30x30_15()
        goals = buscarCenario30x30_15()
        diretorio = 'mapa_30x30/mapa30x30_15.yaml'
    elif opc == 5:
        inicio = [15, 15]
        numero_de_nos_livres = 472
        matriz = getMatriz30x30_30()
        goals = buscarCenario30x30_30()
        diretorio = 'mapa_30x30/mapa30x30_30.yaml'
    elif opc == 6:
        inicio = [15, 15]
        numero_de_nos_livres = 483
        matriz = getMatriz30x30_45()
        goals = buscarCenario30x30_45()
        diretorio = 'mapa_30x30/mapa30x30_45.yaml'
    elif opc == 7:
        inicio = [15, 15]
        numero_de_nos_livres = 815
        matriz = getMatriz40x40_15()
        goals = buscarCenario40x40_15()
        diretorio = 'mapa_40x40/mapa40x40_15.yaml'
    elif opc == 8:
        inicio = [15, 15]
        numero_de_nos_livres = 838
        matriz = getMatriz40x40_30()
        goals = buscarCenario40x40_30()
        diretorio = 'mapa_40x40/mapa40x40_30.yaml'
    elif opc == 9:
        inicio = [15, 15]
        numero_de_nos_livres = 859
        matriz = getMatriz40x40_45()
        goals = buscarCenario40x40_45()
        diretorio = 'mapa_40x40/mapa40x40_45.yaml'
    
    return inicio, numero_de_nos_livres, matriz, goals, diretorio