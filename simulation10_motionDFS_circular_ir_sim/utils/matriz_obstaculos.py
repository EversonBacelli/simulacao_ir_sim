import numpy as np

def gerar_matriz_obstaculos_invertida():
    matriz = np.full((50, 50), '0')

    def marcar_retangulo(cx, cy, length, width):
        x1 = int(round(cx - length / 2))
        x2 = int(round(cx + length / 2))
        y1 = int(round(cy - width / 2))
        y2 = int(round(cy + width / 2))

        # Atenção: invertendo Y (50 - 1 - y) para transformar em coordenada cartesiana
        for x in range(max(0, x1), min(50, x2)):
            for y in range(max(0, y1), min(50, y2)):
                matriz[49 - y, x] = 'X'  # Inverte Y para representar plano cartesiano

    # Bordas
    marcar_retangulo(25.0, 1.5, 50.0, 2.0)     # superior
    marcar_retangulo(25.0, 49.0, 50.0, 2.0)    # inferior
    marcar_retangulo(2.0, 25.0, 1.5, 50.0)     # esquerda
    marcar_retangulo(49.0, 25.0, 0.99 , 50.0)    # direita

    # Blocos internos
    marcar_retangulo(11.0, 22.5, 7.0, 41.0)    # vertical
    marcar_retangulo(29.0, 40.0, 30.0, 6.9)    # horizontal SUPERIOR
    marcar_retangulo(28.0, 13.5, 33.0, 6.0)    # horizontal INFERIOR
    marcar_retangulo(34.0, 25.5, 30.5, 11.0)   # horizontal MEIO

    return matriz