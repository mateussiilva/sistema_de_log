from pyjson import PyJson
from utils import limpar_dimensao
from pprint import pprint as pprint
import time



FILE = r"/media/mateus/D395-E345/1904/14 03 24.json"
pyjson =  PyJson(FILE)
for imp in pyjson.ler_json().values():
    nome = imp.get("ARQUIVO").lower()
    if "tactel" in nome:
        dimensoes = imp.get("DIMENS\u00c3O")
        print(dimensoes, "=>", limpar_dimensao(dimensoes))
        time.sleep(1)
    # print()