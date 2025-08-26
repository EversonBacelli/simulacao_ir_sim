
import random
from simulation9_motionBFS.utils.matriz_obstaculos import gerar_matriz_obstaculos_invertida

matriz = gerar_matriz_obstaculos_invertida()

def gerarValoresAleatorios():
    x = random.randint(3, 47)
    y = random.randint(3, 47)
    return x, y

def validarPosicao():
    while True:
        x, y = gerarValoresAleatorios()
        if matriz[49 - y][x] != 'X':  # Inverte o Y para alinhar com a matriz invertida
            return x, y
