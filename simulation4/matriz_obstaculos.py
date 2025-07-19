import numpy as np

# Gera matriz 50x50 com bordas e blocos internos

def gerar_matriz_vazia(tamanho=50):
    """Retorna matriz tamanho x tamanho preenchida com '0'."""
    return np.full((tamanho, tamanho), '0')


def gerar_matriz_obstaculos(tamanho=50):
    """
    Gera matriz onde as duas primeiras e as duas últimas linhas e colunas
    são marcadas como obstáculos ('X'), além de blocos horizontais internos
    e blocos verticais conforme especificação.
    """
    m = gerar_matriz_vazia(tamanho)

    # Bordas de 2 células
    m[0:2, :] = 'X'    # duas primeiras linhas
    m[-2:, :] = 'X'   # duas últimas linhas
    m[:, 0:2] = 'X'   # duas primeiras colunas
    m[:, -2:] = 'X'   # duas últimas colunas

    # Blocos horizontais internos
    m[40:45, 13:44] = 'X'  # linhas 37–42, colunas 13–43
    m[10:16, 13:44] = 'X'  # linhas 10–15, colunas 13–43

    # Bloco vertical central
    m[21:35, 18:50] = 'X'  # linhas 20–30, colunas 18–48

    # Bloco vertical esquerdo extenso
    m[1:45, 7:13] = 'X'    # linhas 1–43, colunas 8–13

    return m


def inverter_matriz():
    matriz = gerar_matriz_obstaculos()
    return matriz[::-1, :]

