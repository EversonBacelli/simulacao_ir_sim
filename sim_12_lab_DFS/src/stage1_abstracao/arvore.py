from sim_12_lab_DFS.src.classes.no import No, Status
print(f"DEBUG (definirNos.py): ID da classe No é {id(No)}")


def gerarArvore(matriz):
    # Dimensões corretas (51x51)
    linhas = len(matriz)
    colunas = len(matriz[0])
    novaMatriz = [[None for _ in range(colunas)] for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            
            # --- REMOVEMOS O TRY/EXCEPT ---
            
            # Se for obstáculo (1), trata aqui
            if matriz[i][j] == 1:
                novaMatriz[i][j] = None
            else:
                # O Python vai FALHAR AQUI se houver um erro, mas agora irá MOSTRAR
                no = No(matriz[i][j], i, j) 
                novaMatriz[i][j] = no
    
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

