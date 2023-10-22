from files.pyjson import json_mat
from files.pytxt import pytxt

if __name__ == "__main__":
    file_json = r"json_files/1904/01 09 23.json"
    dados_json = json_mat.read_json_file(file_json)
    lista_dados = pytxt.gravar_informações_uteis(dados_json)
    print(lista_dados)
    # with open("arquivos_.txt","w+") as file:
    #     for linhas in lista_dados:
    #         l = linhas + "\n"
    #         file.write(l)