from no import No
import copy
from arvore import gerarArvore, printarArvore


No.matriz = gerarArvore(No.matriz)
matriz = No.matriz


# printarArvore(No.matriz)
# objetivo
matriz[46][15].valor = "C"
origem = matriz[4][4]
# origem.pai = matriz[3][4]


def algoritmoBFS(inicio):
    pilha = [inicio]
    

    # Enquanto a pilha não estiver vazia
    while pilha:
        atual = pilha[-1]
        
        if type(atual) is not list:
            atual = [atual]

        next = []
        for no in atual:
            # print(no.posicao)

            # validar o resultado
            if validarNo(no):
                pilha.pop()
                pilha.append(no)
                return pilha
            else: 
                
                if len(no.vizinhos) > 0 and no.visitado == False : 
                    for vizinho_pos in no.vizinhos:
                        if no.pai != matriz[vizinho_pos[0]][vizinho_pos[1]]:
                            matriz[vizinho_pos[0]][vizinho_pos[1]].pai = no
                            next.append(matriz[vizinho_pos[0]][vizinho_pos[1]])
                no.visitado = True
        if len(next) > 0:
            pilha.append(next)




def validarNo(no):
    posicao = no.posicao
    if matriz[posicao[0]][posicao[1]].valor == 'C':
        return True

retorno = algoritmoBFS(origem)


obj = retorno[-1]
caminho = []

while True:
    caminho.append(obj.posicao)
    
    if obj.posicao == origem.posicao:
        break;
    obj = obj.pai

# caminho.append(origem.posicao)
 
Rcaminho = reversed(caminho) 
for no in Rcaminho:
    print(no, end=',')
print()
print(len(caminho))

# def definirCaminho(retorno):
#     objetivo = retorno[-1]
#     caminho = []
#     while objetivo is not None:
#         caminho.append(objetivo)
#         objetivo = objetivo.pai
#     return reversed(caminho)

# caminho = definirCaminho(retorno)

# print(caminho)