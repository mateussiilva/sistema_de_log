import os
import json
import utils as ut
# from pprint import pprint as print


PATH_BASE =  "/media/mateus/D395-E345/arquivos_json"
PLOTTER = "1904"
MES = "10 23"
ARQUIVO = "04 10 23.json"
caminho_arquivo_json = os.path.join(PATH_BASE,PLOTTER,MES,ARQUIVO)
dados_json = ut.carregar_dados(caminho_arquivo_json)
matrix_dados = ut.criar_matrix(dados=dados_json) 

# print(matrix_dados)
soma_painel = soma_moda = soma_impressao = soma_total = 0
for matrix in matrix_dados:
    nome = matrix[0].lower()
    if "tactel" in nome or "malha" in nome:
        quantidade = float(matrix[1])
        try:
            print(quantidade)
            soma_painel += quantidade
        except:
            pass

        # print(quantidade)
    try:
        
        quantidade = float(matrix[1])
        soma_total += quantidade
    except:
        pass
print("TOTAL: ",soma_total)
print("PAINEL: ",soma_painel)
