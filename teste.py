from files.pytxt import pytxt
from files.json import json_mat


file_json = r"json_files/1904/01 09 23.json"
dados_json = json_mat.read_json_file(file_json).get("imp_1")
for linhas 