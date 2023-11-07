from files.pyjson import pyjson
from files.pytxt import pytxt

file_json = r"json_files/1904/09 23/01 09 23.json"
dados_json = pyjson.read_json_file(file_json)

print(dados_json)
