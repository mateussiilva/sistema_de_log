import os 
import pyhtml 
import json




        

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
