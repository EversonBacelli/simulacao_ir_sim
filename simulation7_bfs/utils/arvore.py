from no import No


def gerarArvore(matriz):
    novaMatriz = [[None for _ in range(50)] for _ in range(50)]

    for i in range(50):
        for j in range(50):
            try:
                if matriz[49-i][j] == 'X':
                    novaMatriz[49-i][j] = None
                else:
                    no = No(matriz[49-i][j], i, j)
                    novaMatriz[49-i][j] = no
            except:
                novaMatriz[49-i][j] = None
    
    return novaMatriz

def printarArvore(matriz):
    for i in range(50):
        for j in range(50):
            no = None
            if matriz[i][j] is not None:
                no = matriz[i][j]
                
            
            try:
                print(f' posicao = {no.posicao} - vizinhos: {(no.vizinhos)} numeroVizinho {no.numeroVizinhos}')
            except:
                print('', end='')
            
            print('', end='')

