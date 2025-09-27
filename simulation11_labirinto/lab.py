from pyamaze import maze
import numpy as np


# Tamanho do labirinto
rows, cols = 25, 25  # você pode alterar para 50x50

# Criar labirinto
m = maze(rows, cols)
m.CreateMaze()

# Inicializar matriz cheia de 1 (paredes)
matriz = [[1 for _ in range(cols*2 + 1)] for _ in range(rows*2 + 1)]

# Preencher caminhos
for i in range(1, rows*2, 2):
    for j in range(1, cols*2, 2):
        matriz[i][j] = 0  # célula livre
        cell = m.maze_map[(i//2 + 1, j//2 + 1)]
        if cell['E']:  # passagem para leste
            matriz[i][j+1] = 0
        if cell['S']:  # passagem para sul
            matriz[i+1][j] = 0



np.savetxt("labirinto3.txt", matriz, fmt='%d')
# m.run()

# Imprimir matriz no console
# labirinto_carregado = np.loadtxt("labirinto.txt", dtype=int)


# for row in labirinto_carregado:
#     print(' '.join(map(str, row)))