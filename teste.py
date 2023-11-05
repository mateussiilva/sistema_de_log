from files.pyjson import pyjson
from files.pytxt import pytxt

file_json = r"json_files/1904/09 23/01 09 23.json"
dados_json = pyjson.read_json_file(file_json).get("imp_1")

CHAVES_CORRETAS = ("")

file_json = r"json_files/1904/01 09 23.json"
dados_json = pyjson.read_json_file(file_json).get("imp_1")
lista_dados = pytxt.gravar_informações_uteis(dados_json)
with open("01 09 23.txt","w+") as file:
    for linhas in lista_dados:
        l = linhas + "\n"
        file.write(l)


dado_selecionados = []
for dado in dados_json.values():
    print(dado)

    
    
