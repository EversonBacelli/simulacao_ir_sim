import numpy as np

def gerar_borda_marcada():
    rows, cols = 50, 50
    matriz = np.full((rows, cols), 'O', dtype=str)

    # Marcar as duas primeiras e últimas linhas com 'X'
    matriz[0:2, :] = 'X'
    matriz[-2:, :] = 'X'

    # Marcar as duas primeiras e últimas colunas com 'X'
    matriz[:, 0:2] = 'X'
    matriz[:, -2:] = 'X'

    return matriz

def marcar_colunas_personalizadas():
    matriz = gerar_borda_marcada()
    rows, cols = matriz.shape

    # Marcar colunas 8 a 12, exceto linhas 3 a 8 e 43 a 48
    for col in range(8, 13):  # colunas 8 a 12
        for row in range(rows):
            if not (2 <= row <= 8 or 43 <= row <= 48):
                matriz[row, col] = 'X'

    # Marcar linhas 42 a 37 (inclusive), colunas 13 a 43 (inclusive)
    for row in range(42, 36, -1):  # 42 até 37
        for col in range(13, 43):  # 13 até 43
            matriz[row, col] = 'X'

    # Marcar linhas 10 a 15 (inclusive), colunas 13 a 43 (inclusive)
    for row in range(9, 16):  # 10 até 15
        for col in range(13, 43):  # 13 até 43
            matriz[row, col] = 'X'

    # Marcar linhas 20 a 30 (inclusive), colunas 18 a 48 (inclusive)
    for row in range(21, 31):  # 20 até 30
        for col in range(19, 49):  # 18 até 48
            matriz[row, col] = 'X'

    return matriz