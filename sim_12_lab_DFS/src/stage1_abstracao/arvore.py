from sim_12_lab_DFS.src.classes.no import No, Status



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



