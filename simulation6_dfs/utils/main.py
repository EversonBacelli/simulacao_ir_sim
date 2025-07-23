from no import No
from arvore import gerarArvore, printarArvore



No.matriz = gerarArvore(No.matriz)
matriz = No.matriz



#printarArvore(No.matriz)



# #Objetivo
matriz[47][22].valor = 'C'


## Origem
origem = matriz[47][5]

pilha = []

def buscarObjetivo(no):
    
    if no.visitado == False:
        no.signal = True
        pilha.append(no)
    else: 
        raise ValueError("Nó já visitado")
    
    if no.valor == 'C':
        print('Objetivo encontrado na posicao', no.posicao)
        return True
    else:
        print('Visitando nó:', no.posicao)


    no.visitado = True
    pilha.append(no)
    
    if no.valor == 'C':
        print('Objetivo encontrado na posicao', no.posicao)
        return True
    
    for vizinho in no.vizinhos:
        linha, coluna = vizinho
        vizinho_no = matriz[linha][coluna]
        
        if not vizinho_no.visitado and vizinho_no.valor != 'X':
            if buscarObjetivo(vizinho_no):
                return True
    
    pilha.pop()
    return False










def buscarValor(index):
    vizinho = origem.vizinhos[index]
    try:
        linha = vizinho[0]
        coluna = vizinho[1]

        if matriz[linha][coluna].valor != 'C':
            print(f'Não encontrado na posicao {matriz[linha][coluna].posicao}')
            raise ValueError("Não é possível criar um nó em um obstáculo")
        else: 
            print('Encontrado na posicao', matriz[linha][coluna].posicao)
    except:
        buscarValor(index+1)

buscarValor(0)