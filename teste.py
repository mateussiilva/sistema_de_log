from files.pytxt import pytxt
from files.pyjson import json_mat


file_json = r"json_files/1904/01 09 23.json"
dados_json = json_mat.read_json_file(file_json).get("imp_1")

print(dados_json)
# for value in dados_json:
#     diemensao = dados_json.get("DIMENS\u00c3O")  
#     print(diemensao)
    # try:
    #     nome_arquivo = value.get("ARQUIVO")
    #     dimensao = value.get("DIMENS\u00c3O")
    #     perfil_icc = value.get('PERFIL ICC DE SAÍDA')
    #     quantidade = value.get('QUANTIDADE DE CÓPIAS')
    #     data_envio = value.get('INÍCIO, DATA E HORA DO RIP')
    # except:
    #     print("Deu pau")