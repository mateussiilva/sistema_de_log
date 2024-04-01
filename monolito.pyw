from pyjson import PyJson
import PySimpleGUI as sg
import os
from PySimpleGUI import popup_ok
from utils import criar_matrix


""" CONSTANTES """
SIZE = (900, 700)
HEADERS_TABLE = [
    "Nome do Arquivo",
    "Metros",
    "Data da Impressão"]


layout = [
    [sg.Text("Caminho do arquivo json"), sg.Input(key="-PATH_JSON-"),
     sg.FileBrowse(button_text="Abrir Arquivo",
                   initial_folder="/media/mateus/D395-E345/ProjetctFiles/arquivos_json/arquivos_antigos/")],
    [sg.Table(values=[],
              headings=HEADERS_TABLE,
              enable_click_events=True, enable_events=True,
              col_widths=100,
              expand_x=True,
              expand_y=True,
              selected_row_colors="Red on Yellow", justification="left",
              auto_size_columns=True, size=(45, 32), alternating_row_color="Gray", k="-TABELA-",
              )
     ],
    [
        sg.Button("Gerar Tabela", key="-LOAD_TABLE-"),
        sg.Button("Limpar Tabela", key="-CLEAR_TABLE-"),
        sg.Button("Somar Linhas", key="-SUM_TABLES-")
    ]

]


def carregar_frontend():
    window = sg.Window("Gerenciador de LOG", layout, size=SIZE)

    while 1:
        events, values = window.read()
        py_json = PyJson()
        valores = criar_matrix(py_json.ler_json(values["-PATH_JSON-"]))

        if events == "-LOAD_TABLE-":
            window["-TABELA-"].update(values=valores)
            window.refresh()
        elif events == "-CLEAR_TABLE-":
            window["-TABELA-"].update(values=[])
            window.refresh()

        elif events == "-SUM_TABLES-":
            indices = values["-TABELA-"]
            s = 0
            for indice in indices:
                metros = float(valores[indice][1])
                s += metros
            msg = f"{s:.2f}"
            popup_ok(msg)

        if events == sg.WIN_CLOSED:
            break

        # print(values)

    window.close()


def pegar_arquivos_html(path):
    arquivos = [
        os.path.join(path, file)
        for file in os.listdir(path)
        if os.path.isfile(os.path.join(path, file))
    ]
    return arquivos


def pegar_nome_arquivo(path):
    return os.path.split(path)[1]


if __name__ == "__main__":
    carregar_frontend()
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
                    contexto = parserhtml.create_context_html(arquivo)
                    listadados = parserhtml.struct_base_file(contexto)
                    matrixdicionarios = parserhtml.create_dict_dados(
                        listadados)
                    pyjson.escrever_json(
                        dados=matrixdicionarios,
                        nome_arquivo=arquivo_destino
                    )

                print()
                # print(pegar_arquivos_html(p))
        # print(p)
