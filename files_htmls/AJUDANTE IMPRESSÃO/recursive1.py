import os

def escanear_pastas(pasta_inicial):
    #arquivos = os.listdir(pasta_inicial)
    
    for raiz,diretorio,arquivo in os.walk(pasta_inicial):
        if len(diretorio) > 0:
            path_dir = os.path.join(raiz,*diretorio)
            #print(path_dir)
            for file in os.listdir(path_dir):
             #   print(file)


if __name__ == '__main__':
    escanear_pastas(r"C:\Users\Usuario\Downloads")