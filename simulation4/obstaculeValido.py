import random
from matriz_obstaculos import gerar_matriz_obstaculos


matriz = gerar_matriz_obstaculos()


def gerarValoresAleatorios():
    x = random.randint(3, 47)
    y = random.randint(3, 47)
    return x, y

def validarPosicao():
    while True:
        x, y = gerarValoresAleatorios()
        if matriz[x][y] != 'X':
            return x, y





