from .matriz_obstaculos import gerar_matriz_obstaculos_invertida


class No:
    matriz = gerar_matriz_obstaculos_invertida()
    filhos = []
    
    def __init__(self, valor, linha, coluna ):
        if valor == "X":
            raise ValueError("Não é possível criar um nó em um obstáculo")
        
        self.valor = valor
        self.vizinhos = self.incluirVizinhos(linha, coluna)
        self.visitado = False
        self.posicao = [linha, coluna]
        self.pai = None
        self.equivalente = [coluna, 49 - linha]
            
    def validarVizinho(self, linha, coluna):
        if linha < 51 and linha > 0 and coluna > 0 and coluna < 51 :
            
            if No.matriz[linha][coluna] == 'X': 
                return False
            else: 

                return [linha, coluna]
        else:
            return False

    def fabricaDeVizinhos(self, novaLinha, novaColuna):
        v = self.validarVizinho(novaLinha, novaColuna)
        return v

    def validarPosicao(self, linha, coluna):
        for ramo in self.filhos:
            if ramo == [linha, coluna]:
                return False
        self.filhos.append([linha, coluna]) 
        return True

    def incluirVizinhos(self, linha, coluna):
        vd = self.fabricaDeVizinhos((linha + 1), coluna)
        ve = self.fabricaDeVizinhos((linha - 1), coluna)
        vb = self.fabricaDeVizinhos(linha, (coluna - 1))
        vc = self.fabricaDeVizinhos(linha, (coluna + 1))
        listaPotenciaisFilhos = [vd, ve, vb, vc]
        vizinhos = []
        for filho in listaPotenciaisFilhos:
            if filho:
                vizinhos.append(filho)
         
        return vizinhos
        