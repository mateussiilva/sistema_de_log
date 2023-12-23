from PyJson import PyJson




json_py = PyJson("09 08 23.json")
dados_json = json_py.ler_arquivo_json()
json_py.escrever_json(dados_json,"teste.json")
print(dados_json)