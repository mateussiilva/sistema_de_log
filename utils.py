from pprint import pprint as print
import json




def limpar_nome(texto):
    lista_texto = texto.split("\\")
    return lista_texto[len(lista_texto) -1]


def limpar_dimensao(texto):
    return float(texto.replace("cm","").split(" x ")[1])


def orgnizar_lista(dicionario,env):
    
    for chave,valor in dicionario.items():
        if chave == "DIMENSÃO":
            qtd_copias = 1
            try:
                qtd_copias = int(dicionario["QUANTIDADE DE C\u00d3PIAS"])
            except:
                qtd_copias = 1
            metros = str(round(qtd_copias * limpar_dimensao(valor))/100)
            env.append(metros)
        elif chave == "ARQUIVO":
            nome_limpo = limpar_nome(valor)
            env.append(nome_limpo)
        elif chave != "QUANTIDADE DE C\u00d3PIAS" and \
            chave != "PERFIL ICC DE SA\u00cdDA":
            env.append(valor)

    return env


def criar_matrix(dados:dict):
    matrix = []
    tmp = []
    for _,dado in dados.items():
        tmp = orgnizar_lista(dado,tmp)
        matrix.append(tmp[:])
        tmp.clear()   
    return matrix

def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo,"r") as file:
        dados = json.load(file)
    return dados


    