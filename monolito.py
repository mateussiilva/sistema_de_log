import PySimpleGUI as sg
import os
from bs4 import BeautifulSoup
from PyUtilites import criar_matrix
from PySimpleGUI import popup_ok
from PyJson import PyJson
from pprint import pprint as print

""" CONSTANTES """
SIZE = (900, 700)
HEADERS_TABLE = [
    "Nome do Arquivo",
    "Metros",
    "Data da Impressão"]

PLOTTERS = {"mutoh": "1604", "prisamjet": "1602", "prismatetext": "1904"}

""" BACKEND """

CHAVES = (
    'ARQUIVO',
    'DIMENSÃO',
    'INÍCIO, DATA E HORA DO RIP',
    'PERFIL ICC DE SAÍDA',
    'QUANTIDADE DE CÓPIAS',
)


class ParserHtml:
    def __init__(self, encode) -> None:
        self.encode = encode

    def create_context_html(self, path_file_html: str):
        with open(path_file_html, "r", encoding=self.encode) as file:
            html_content = file.read()
        return BeautifulSoup(html_content, "html.parser")

    def struct_base_file(self, content_html, target_tag="table"):
        return list(content_html.find_all(target_tag))

    def create_dict_dados(self, base_list):
        lista_dicionarios = []
        for tabela in base_list:
            chaves = list(map(lambda item: item.get_text().strip().replace(":", "").upper(),
                              tabela.find_all("th")))
            valores = list(map(lambda item: item.get_text().strip(),
                               tabela.find_all("td")))

            # removendo o primeiro elemento
            valor_0 = chaves.pop(0)

            if valor_0 == "INICIAR TRABALHO DE RIP":
                # # removendo o ultimo elemento
                chaves.pop(len(chaves) - 1)
                dicionario_temp = dict(zip(chaves, valores))
                dicionario = {}
                for chave, valor in dicionario_temp.items():
                    if chave in CHAVES:
                        dicionario[chave] = valor
                chaves.clear()
                valores.clear()

                lista_dicionarios.append(dicionario.copy())
                dicionario.clear()

        dicionarios = {
            f"imp_{k}": v
            for k, v in enumerate(lista_dicionarios)
        }

        return dicionarios


# """ FRONTEND """
# layout = [
#     [sg.Text("Caminho do arquivo json"), sg.Input(key="-PATH_JSON-"),
#      sg.FileBrowse(button_text="Abrir Arquivo",
#                    initial_folder="/media/mateus/D395-E345/ProjetctFiles/arquivos_json/arquivos_antigos/")],
#     [sg.Table(values=[],
#               headings=HEADERS_TABLE,
#               enable_click_events=True, enable_events=True,
#               col_widths=100,
#               expand_x=True,
#               expand_y=True,
#               selected_row_colors="Red on Yellow", justification="left",
#               auto_size_columns=True, size=(45, 32), alternating_row_color="Gray", k="-TABELA-",
#               )
#      ],
#     [
#         sg.Button("Gerar Tabela", key="-LOAD_TABLE-"),
#         sg.Button("Limpar Tabela", key="-CLEAR_TABLE-"),
#         sg.Button("Somar Linhas", key="-SUM_TABLES-")
#     ]

# ]


# def carregar_frontend():
#     window = sg.Window("Gerenciador de LOG", layout, size=SIZE)

#     while 1:
#         events, values = window.read()
#         py_json = PyJson(values["-PATH_JSON-"])
#         valores = criar_matrix(py_json.ler_json())

#         if events == "-LOAD_TABLE-":
#             window["-TABELA-"].update(values=valores)
#             window.refresh()
#         elif events == "-CLEAR_TABLE-":
#             window["-TABELA-"].update(values=[])
#             window.refresh()

#         elif events == "-SUM_TABLES-":
#             indices = values["-TABELA-"]
#             s = 0
#             for indice in indices:
#                 metros = float(valores[indice][1])
#                 s += metros
#             msg = f"{s:.2f}"
#             popup_ok(msg)

#         if events == sg.WIN_CLOSED:
#             break

#         # print(values)

#     window.close()

def pegar_arquivos_html(path):
    arquivos = [
        os.path.join(path,file)
        for file in os.listdir(path)
        if os.path.isfile(os.path.join(path,file))
    ]
    return arquivos

if __name__ == "__main__":
    # carregar_frontend()
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
    MES_ALVO = MESES["novembro"]
    for plotter in PLOTTERS.values():
        p = os.path.join(PATH,plotter)
        
        for mes in os.listdir(p):
            p_destino = os.path.join(PATH_DESTINO,plotter,mes)
            try:
                os.mkdir(p_destino)
            except Exception as error:
                pass
                # print(error)

            if mes == MES_ALVO:
                p = os.path.join(PATH,plotter,mes)

                # print(pegar_arquivos_html(p))
        # print(p)
