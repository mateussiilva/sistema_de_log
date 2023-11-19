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


def verificar_pasta_existente(nome_pasta,caminho=".") -> bool:
    cam = os.path.join(caminho,nome_pasta) 
    if os.path.exists(cam) and os.path.isdir(cam):
        return True
    
    return False



if __name__ == "__main__":
    PLOTTERS = {"mutoh":"1604","prisamjet":"1602","prismatetext":"1904"}
    PATH = "/media/mateussiilva/D395-E345/ARQUIVOS_HTMLS_ATUAIS/"

    print(verificar_pasta_existente(PATH,PLOTTERS.get("mutoh")))
    # arquivo_tex = pegar_arquivos_html(os.path.join(PATH,"1904/09 23"))[0]
    
    # nome_json_file = os.path.split(arquivo_tex)[1].replace(".HTML",".json") 
    # print(nome_json_file)
    
    # contexto_jet  = pyhtml.struct_base_file(pyhtml.create_context_html(arquivo_tex))
    # dicionario = pyhtml.create_dict_dados(contexto_jet)
    
    # with open(nome_json_file,"w+") as file:
    #     json.dump(dicionario,file)