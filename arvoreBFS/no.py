
class No:
    def __init__(self, valor, vizinhos):
        self.valor = valor
        self.vizinhos = vizinhos
        self.visitado = False 
        self.numeroVisitas = 0
        self.pai = None  # Adicionando atributo pai para rastrear o nó pai
    def incluirVizinhos(self, vizinhos):
        for vizinho in vizinhos:
            self.vizinhos.append(vizinho)