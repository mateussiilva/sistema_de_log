import os 
import pyhtml 
import json

# from pprint import pprint as print

def validar_extensao(extensao_arquivo,extensao_alvo="html") -> bool:
    return True if extensao_arquivo.strip(".").lower() == extensao_alvo else False


def get_files_htmls(path):
    import glob
    lista_arquivos = []
    for arquivo in os.listdir(path):
        _,extensao = os.path.splitext(arquivo)

        if validar_extensao(extensao):
            __ = os.path.join(path,arquivo)
            lista_arquivos.append(__)
            
    return sorted(lista_arquivos)





if __name__ == "__main__":
    PATH = "/media/mateussiilva/D395-E345/ARQUIVOS_HTMLS_ATUAIS/"
    # arquivo_jet = get_files_htmls("/tmp/files_htmls/1602/09 23")[0]
    # arquivo_mutoh = get_files_htmls("/tmp/files_htmls/1604/09 23")[0]
    arquivo_tex = get_files_htmls(os.path.join(PATH,"1904/09 23"))[0]
    
    nome_json_file = os.path.split(arquivo_tex)[1].replace(".HTML",".json") 
    print(nome_json_file)
    
    contexto_jet  = pyhtml.struct_base_file(pyhtml.create_context_html(arquivo_tex))
    dicionario = pyhtml.create_dict_dados(contexto_jet)
    
    with open(nome_json_file,"w+") as file:
        json.dump(dicionario,file)