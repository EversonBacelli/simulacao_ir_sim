from enum import Enum

class No:
    NOS = []
    def __init__(self, valor, vizinhos):
        self.valor = valor
        self.vizinhos = vizinhos
        self.numeroVisitas = 0
        self.status = Status.NAO_VISITADO
        self.pai = None  # Adicionando atributo pai para rastrear o nó pai
        self.visitas = 0
        No.NOS.append(self)
    def incluirVizinhos(self, vizinhos):
        for vizinho in vizinhos:
            self.vizinhos.append(vizinho)
    
    def continuarVisitas(self):
        if len(self.vizinhos) == self.visitas:
            return False
        else:
            return True
        

class Status(Enum):
    NAO_VISITADO = 1
    VISITADO = 2
    EXPLORADO = 3
    BLOQUEADO = 4
    