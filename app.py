from pyjson import PyJson
from utils import limpar_dimensao,pegar_arquivos_html
from pprint import pprint as pprint
import time
import os 





PATH = "/media/mateus/D395-E345/1904/"
tactel = malha = 0
for arquivo in os.listdir(PATH):
    arquivo = os.path.join(PATH,arquivo)
    pyjson =  PyJson(arquivo)
   

    for imp in pyjson.ler_json().values():
        nome = imp.get("ARQUIVO").lower()
        if "tactel" in nome or "tactl" in nome:
            dimensoes = imp.get("DIMENS\u00c3O")
            metro = limpar_dimensao(dimensoes)
            tactel += metro
        if "malha" in nome:
            dimensoes = imp.get("DIMENS\u00c3O")
            metro = limpar_dimensao(dimensoes)
            malha += metro
        # print()
    
    print(tactel // 100)
    print(malha // 100)
    print("---------------")