import os

from pyhtml import ParserHtml
from pyjson import PyJson

def pegar_arquivos_html(path):
    arquivos = [
        os.path.join(path, file)
        for file in os.listdir(path)
        if os.path.isfile(os.path.join(path, file))
    ]
    return arquivos


def pegar_nome_arquivo(path):
    return os.path.split(path)[1]


PLOTTERS = {"mutoh": "1604", "prisamjet": "1602", "prismatetext": "1904"}
PATH = "/media/mateus/D395-E345/ProjetctFiles/LOGS DAS MAQUINAS"
PATH_DESTINO = "/tmp/arquivos_json"
ANO = "23"
MESES = {
    "janeiro": f"01 {ANO}",
    "fevereiro": f"02 {ANO}",
    "março": f"03 {ANO}",
    "abril": f"04 {ANO}",
    "maio": f"05 {ANO}",
    "junho": f"06 {ANO}",
    "julho": f"07 {ANO}",
    "agosto": f"08 {ANO}",
    "setembro": f"09 {ANO}",
    "outubro": f"10 {ANO}",
    "novembro": f"11 {ANO}",
    "dezembro": f"12 {ANO}",
}
MES_ALVO = MESES["dezembro"]
parserhtml = ParserHtml("latin-1")
pyjson = PyJson()

for plotter in PLOTTERS.values():
    p = os.path.join(PATH, plotter)

    for mes in os.listdir(p):
        p_destino = os.path.join(PATH_DESTINO, plotter, mes)
        try:
            os.mkdir(p_destino)
        except Exception as error:
            pass
            print(error)

        if mes == MES_ALVO:
            arquivos = pegar_arquivos_html(
                os.path.join(PATH, plotter, mes))
            for arquivo in arquivos:
                novo_nome = pegar_nome_arquivo(
                    arquivo).replace(".HTML", ".json")
                arquivo_destino = os.path.join(p_destino, novo_nome)
                print(arquivo_destino)
                
                listadados = parserhtml.struct_base_file(arquivo)
                matrixdicionarios = parserhtml.create_dict_dados(
                    listadados)
                pyjson.escrever_json(
                    dados=matrixdicionarios,
                    nome_arquivo=arquivo_destino
                )

            print()
            # print(pegar_arquivos_html(p))
    # print(p)
