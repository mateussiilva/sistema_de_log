import os
import glob

# MEUS MODULOS
import files.html.pyhtml as pyhtml
import files.pyjson.pyjson as pyjson


def create_new_name(path):
    nome, e = os.path.split(path)
    n, exte = os.path.splitext(e)
    return n + ".json"


def get_files_htmls(path,extension="*.HTML") -> set:
    list_files_htmls = []
    for file_html in glob.glob(os.path.join(path,extension)):
        list_files_htmls.append(file_html)
    
    return sorted(list_files_htmls)
        
        


if __name__ == "__main__":
    # HTML
    DIR_HTMLS = "files_htmls"
    PLOTTER = "1602"
    MES = "09 23"
    
    # JSON
    DIR_JSON = "json_files"
    PATH_JSON = os.path.join(DIR_JSON,PLOTTER,MES)
     
    
    PATH = os.path.join(DIR_HTMLS,PLOTTER,MES)
    arquivos_htmls = [
        os.path.join(PATH,file) for file in os.listdir(PATH)]
    arquivos_htmls.sort()
    
    file_html_1 = arquivos_htmls[0]
    context_html = pyhtml.create_context_html(file_html_1)
    listas_tabelas = pyhtml.struct_base_file(context_html)
    lista_dicionarios = pyhtml.create_dict_dados(listas_tabelas)
    nome_json_file = create_new_name(file_html_1)
    
    pyjson.write_json_file(
        os.path.join(PATH_JSON,nome_json_file),
        lista_dicionarios)
    print(nome_json_file)