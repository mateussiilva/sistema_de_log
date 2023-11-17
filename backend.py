import os 
import pyhtml 


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
    arquivo_jet = get_files_htmls("/tmp/files_htmls/1602/09 23")[0]
    arquivo_mutoh = get_files_htmls("/tmp/files_htmls/1604/09 23")[0]
    arquivo_tex = get_files_htmls("/tmp/files_htmls/1904/09 23")[0]

    print(arquivo_jet)
    print(arquivo_mutoh)
    print(arquivo_tex)
    