import os
import glob

# MEUS MODULOS
import files.html.pyhtml as pyhtml
import files.pyjson.pyjson as pyjson


def create_new_name(path):
    nome, e = os.path.split(path)
    n, exte = os.path.splitext(e)
    return n + ".json"



    
if __name__ == "__main__":
    # HTML
    DIR_HTMLS = "\\STORAGE-SILKART\impressao\LOGS DAS MAQUINAS"
    PLOTTER = "1904"
    MES = "09 23"
    PATH = os.path.join(DIR_HTMLS,PLOTTER,MES)
    print(PATH)
    arquivos_htmls = [
        os.path.join(PATH,file) for file in os.listdir(rf"{PATH}")]
    arquivos_htmls.sort()
    for arquivo in arquivos_htmls:
        print(arquivo)
    exit(1)
    if os.path.exists(PATH):
       print("Pasta existe")
    else:
        print("Pasta não existe, vai ser criada agora...")
        try:
            os.mkdir(PATH)
        except Exception as err:
            print("Houve um error %s",err)
            exit(1)
            
    
    # JSON
    DIR_JSON = "json_files"
    PATH_JSON = os.path.join(DIR_JSON,PLOTTER,MES)
     
    
    
    arquivos_htmls = [
        os.path.join(PATH,file) for file in os.listdir(PATH)]
    arquivos_htmls.sort()
    
    for file_html in arquivos_htmls:      
        context_html = pyhtml.create_context_html(file_html)
        listas_tabelas = pyhtml.struct_base_file(context_html)
        lista_dicionarios = pyhtml.create_dict_dados(listas_tabelas)
        
        nome_json_file = create_new_name(file_html)
        path_json_file = os.path.join(PATH_JSON, nome_json_file)
        
        print(path_json_file)
        pyjson.write_json_file(
            path_json_file,
            lista_dicionarios)
        
