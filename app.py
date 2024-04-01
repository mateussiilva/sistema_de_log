from pyjson import PyJson
from utils import limpar_dimensao
from pprint import pprint as pprint
import time



FILE = r"/media/mateus/D395-E345/1904/14 03 24.json"
pyjson =  PyJson(FILE)
tactel = malha = 0
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