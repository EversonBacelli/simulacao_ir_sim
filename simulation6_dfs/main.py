from no import No
from pprint import pprint


# buscar Matriz
matriz = No.matriz

novaMatriz = [[None for _ in range(50)] for _ in range(50)]


for i in range(50):
    for j in range(50):
        try:
            no = No(matriz[i][j], i, j)
            novaMatriz[i][j] = no
        except:
            novaMatriz[i][j] = None
            

for i in range(50):
     for j in range(50):
         no = novaMatriz[i][j]
         try:
             print(f'[{i}, {j}] = {no.valor} {no.vizinhos} ')
         except:
             print('')
        
         print('----')



