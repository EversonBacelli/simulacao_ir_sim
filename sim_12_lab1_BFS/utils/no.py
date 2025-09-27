from .matriz_obstaculos import gerar_matriz_obstaculos_invertida
from enum import Enum

class No:
    matriz = gerar_matriz_obstaculos_invertida()
    NOS = []
    lista_de_vizinhos = set()
    NOS_ACESSIVEIS = 0
    def __init__(self, valor, linha, coluna ):
        if valor == 1:
            raise ValueError("Não é possível criar um nó em um obstáculo")
        
        self.valor = valor
        self.vizinhos = self.incluirVizinhos(linha, coluna)
        self.status = Status.NAO_VISITADO
        self.posicao = [linha, coluna]
        self.pai = None
        self.equivalente = [coluna, 49 - linha]
        self.visitas = 0
        No.NOS.append(self)
        if self.valor != "X":
            No.NOS_ACESSIVEIS += 1
            
    def validarVizinho(self, linha, coluna):
        if linha < 51 and linha > 0 and coluna > 0 and coluna < 51 :
            
            if No.matriz[linha][coluna] == '1': 
                return False
            else: 

                return [linha, coluna]
        else:
            return False

    def fabricaDeVizinhos(self, novaLinha, novaColuna):
        v = self.validarVizinho(novaLinha, novaColuna)
        return v

    def validarPosicao(self, linha, coluna):
        for ramo in No.lista_de_vizinhos :
            if ramo[0] == linha and ramo[1] == coluna:
                return False
        No.lista_de_vizinhos.append([linha, coluna]) 
        return True

    def incluirVizinhos(self, linha, coluna):
        vd = self.fabricaDeVizinhos((linha + 1), coluna)
        ve = self.fabricaDeVizinhos((linha - 1), coluna)
        vb = self.fabricaDeVizinhos(linha, (coluna - 1))
        vc = self.fabricaDeVizinhos(linha, (coluna + 1))
        listaPotenciaisFilhos = [vd, ve, vb, vc]
        vizinhos = []
        for filho in listaPotenciaisFilhos:
            if filho != False:
                vizinhos.append(filho)
        return vizinhos
    
    def continuarVisitas(self):
        if len(self.vizinhos) == self.visitas:
            return False
        else:
            return True
    def incluirPai(self, pai):
        if pai.posicao in self.vizinhos:
            self.vizinhos.remove(pai.posicao)
        self.pai = pai


    def retirarVizinhosNulos():
        for linha in No.matriz:
            for no in linha:
                if no is not None:
                    for vizinho_pos in no.vizinhos:
                        vizinho = No.matriz[vizinho_pos[0]][vizinho_pos[1]]
                        if vizinho is None:
                            no.vizinhos.remove(vizinho_pos)
    
    def resetMatriz(m):
        for linha in m:
            for no in linha:
                if no is not None:
                    no.status = Status.NAO_VISITADO
                    no.pai = None
        return m
   
class Status(Enum):
    NAO_VISITADO = 1
    VISITADO = 2
    BLOQUEADO = 3