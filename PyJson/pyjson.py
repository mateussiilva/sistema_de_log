from json import load,dump



class PyJson:
    def __init__(self,nome_arquivo_json:str):
        self.arquivo_json = nome_arquivo_json
    
    
    def  ler_json(self) -> dict:
        with open(self.arquivo_json,"r") as file:
            data = load(file)
        return data
    
    
    def escrever_json(self,dados,nome_arquivo) -> bool:
        try:
            fp = open(nome_arquivo,"w")
            dump(dados,fp)
        except:
            return False
        
        finally:
            fp.close()
            
        return True
    
    