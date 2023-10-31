from json import dump,load


def write_json_file(name_file_json,dados) -> bool:
    """
    A função recebe o a caminho do arquivo json
    abre o arquivo e faz a gravação dos dados 
    """
    with open(name_file_json,"w+") as file:
        data = dump(dados,file)
        return True
    return False
    

def read_json_file(name_file_json):
    with open(name_file_json,"r") as file:
        data = load(fp=file)
        return data
    
    
    
if __name__ == "__main__":
    file_teste_json = "json_files/1602/09 23/1602/01 09 23.json"
    if write_json_file(file_teste_json,{"nome":"mateus","idade":22}):
        dados = read_json_file(file_teste_json)
        print(len(dados))
        
    