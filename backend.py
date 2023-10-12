import files.html.pyhtml as pyhtml
from files.json.json_mat import write_json_file
import os
import glob

FOLDER_JSON_FILES = "json_files"


def create_new_name(path):
    nome, e = os.path.split(path)
    n, exte = os.path.splitext(e)
    return n+".json"

    
def main():
    PATH = "testes/1904/09 23"
    EXTE = "*.HTML"
    for file_html in glob.glob(os.path.join(PATH,EXTE)):
        print(create_new_name(file_html))
        




if __name__ == "__main__":
    main()
    # path_html_file = "gerenciador_de_log/arquivos_htmls/29 08 23.HTML"
    # dicionario = {"matesu":"jose"}
    # write_json_file(os.path.join(FOLDER_JSON_FILES,create_new_name(path_html_file)),dicionario)
    
    # content_html = pyhtml.create_context_html(path_html_file)
    # list_dados = pyhtml.struct_base_file(content_html,"table")
    # dicinarios_limpos = pyhtml.create_dict_dados(list_dados)
    # for dados in dicinarios_limpos:
    #     print(dados)


