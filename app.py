from pprint import pprint as print



dados_impressoes = ler_dados_json("arquivos_json/RIPLOG.json")

        

utl.gravar_txt(gravar_informações_uteis(dados_impressoes),"teste.txt")