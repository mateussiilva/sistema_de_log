import os 
import pyhtml 
import json

# from pprint import pprint as print

def validar_extensao(extensao_arquivo,extensao_alvo="html") -> bool:
    return True if extensao_arquivo.strip(".").lower() == extensao_alvo else False


def pegar_arquivos_html(path):
    import glob
    lista_arquivos = []
    for arquivo in os.listdir(path):
        _,extensao = os.path.splitext(arquivo)

        if validar_extensao(extensao):
            __ = os.path.join(path,arquivo)
            lista_arquivos.append(__)
            
    return sorted(lista_arquivos)


def verificar_pasta_existente(caminho_pasta) -> bool:
    # cam = os.path.join(caminho,nome_pasta) 
    if os.path.exists(caminho_pasta) and os.path.isdir(caminho_pasta):
        return True
    
    return False

def criar_pasta(caminho_pasta) -> bool:
    try:
        os.mkdir(caminho_pasta)
    except:
        return False
    return True
        

if __name__ == "__main__":
    PLOTTERS = {"mutoh":"1604","prisamjet":"1602","prismatetext":"1904"}
    CAMINHO_DE_ORIGEM = "/media/mateussiilva/D395-E345/ARQUIVOS_HTMLS_ATUAIS/"
    CAMINHO_DE_DESTINO = "/media/mateussiilva/D395-E345/arquivos_json"
    MESES = ("08 23","09 23", "10 23","11 23")
    for impressora in PLOTTERS.values():
        caminho_origem_completo = os.path.join(CAMINHO_DE_ORIGEM,impressora)
        for pasta_do_mes  in os.listdir(caminho_origem_completo):
            c_completo = os.path.join(caminho_origem_completo,pasta_do_mes)
            for arquivo_html in os.listdir(c_completo):
                caminho_arquivo = os.path.join(c_completo,arquivo_html)
                print(caminho_arquivo)
            print("=-="*10)
    # print("---------------")
    # arquivo_tex = pegar_arquivos_html(os.path.join(PATH,"1904/09 23"))[0]
    
    # nome_json_file = os.path.split(arquivo_tex)[1].replace(".HTML",".json") 
    # print(nome_json_file)
    
    # contexto_jet  = pyhtml.struct_base_file(pyhtml.create_context_html(arquivo_tex))
    # dicionario = pyhtml.create_dict_dados(contexto_jet)
    
    # with open(nome_json_file,"w+") as file:
    #     json.dump(dicionario,file)