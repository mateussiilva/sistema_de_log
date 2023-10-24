import files.html.pyhtml as pyhtml
from files.pyjson.json_mat import write_json_file
import os
import glob


def create_new_name(path):
    nome, e = os.path.split(path)
    n, exte = os.path.splitext(e)
    return n + ".json"


def get_files_htmls(path,extension="*.HTML") -> set:
    list_files_htmls = []
    for file_html in glob.glob(os.path.join(path,extension)):
        list_files_htmls.append(file_html)
    
    return sorted(list_files_htmls)
        
        
def main(path_origem,path_destino,plotter):
    PATH = "testes/1904/09 23"
    files_htmls = get_files_htmls(path_origem)
    for file_html in files_htmls:
        path_json_file = os.path.join(path_destino,plotter,create_new_name(file_html))
        contexto = pyhtml.create_context_html(file_html)
        lista_dados = pyhtml.struct_base_file(contexto, "table")
        dicionario = pyhtml.create_dict_dados(lista_dados)
        
        write_json_file(
            path_json_file,dados=dicionario
        )        
        dicionario.clear()
        



