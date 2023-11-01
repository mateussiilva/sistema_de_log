from files.pytxt import pytxt
from files.html import pyhtml
from files.pyjson import pyjson
import glob
import os


def criar_nome_novo(path):
    nome, e = os.path.split(path)
    n, exte = os.path.splitext(e)
    return n + ".json"

def get_files_htmls(path,extension="*.HTML") -> set:
    list_files_htmls = []
    for file_html in glob.glob(os.path.join(path,extension)):
        list_files_htmls.append(file_html)
    
    return sorted(list_files_htmls)

DIR_HTMLS = "Z:\LOGS DAS MAQUINAS"
PLOTTER = "1604"
MES = "08 23"
PATH_HTML = os.path.join(DIR_HTMLS,PLOTTER,MES)

DIR_JSON = "Z:\LOGS DAS MAQUINAS\JSON"
PATH_JSON = os.path.join(DIR_JSON,PLOTTER,MES)

for arquivo_html in get_files_htmls(PATH_HTML):
    nome_json_arquivo = os.path.join(PATH_JSON,criar_nome_novo(arquivo_html))
    # print(nome_json_arquivo)
    context_html = pyhtml.create_context_html(arquivo_html)
    listas_tabelas = pyhtml.struct_base_file(context_html)
    lista_dicionarios = pyhtml.create_dict_dados(listas_tabelas)
    

    print(nome_json_arquivo)
    pyjson.write_json_file(
        nome_json_arquivo,
        lista_dicionarios)
    
    lista_dicionarios.clear()
    listas_tabelas.clear()
    