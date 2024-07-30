from json import load,dump



class PyJson:
    def __init__(self):
        pass
    
    def  ler_json(self,filename) -> dict:
        with open(filename,"r") as file:
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
    
    