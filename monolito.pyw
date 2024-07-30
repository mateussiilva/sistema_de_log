import PySimpleGUI as sg
import os
import json

from config import PLOTTERS, CHAVES, SIZE
from bs4 import BeautifulSoup
# from json import load, dump
from PyJson.pyjson import PyJson
from PySimpleGUI import popup_ok


""" CONSTANTES """
HEADERS_TABLE = [
    "Nome do Arquivo",
    "Metros",
    "Data da Impressão"]


""" BACKEND """


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


def limpar_nome(texto):
    lista_texto = texto.split("\\")
    return lista_texto[len(lista_texto) - 1]


def limpar_dimensao(texto):
    return float(texto.replace("cm", "").split(" x ")[1])


def orgnizar_lista(dicionario, env):

    for chave, valor in dicionario.items():
        if chave == "DIMENSÃO":
            qtd_copias = 1
            try:
                qtd_copias = int(dicionario["QUANTIDADE DE C\u00d3PIAS"])
            except:
                qtd_copias = 1
            metros = str(round(qtd_copias * limpar_dimensao(valor))/100)
            env.append(metros)
        elif chave == "ARQUIVO":
            nome_limpo = limpar_nome(valor)
            env.append(nome_limpo)
        elif chave != "QUANTIDADE DE C\u00d3PIAS" and \
                chave != "PERFIL ICC DE SA\u00cdDA":
            env.append(valor)

    return env


def criar_matrix(dados: dict):
    matrix = []
    tmp = []
    for _, dado in dados.items():
        tmp = orgnizar_lista(dado, tmp)
        matrix.append(tmp[:])
        tmp.clear()
    return matrix


def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, "r") as file:
        dados = json.load(file)
    return dados


def validar_extensao(extensao_arquivo, extensao_alvo="html") -> bool:
    return True if extensao_arquivo.strip(".").lower() == extensao_alvo else False


def pegar_arquivos_html(path):
    import glob
    lista_arquivos = []
    for arquivo in os.listdir(path):
        _, extensao = os.path.splitext(arquivo)

        if validar_extensao(extensao):
            __ = os.path.join(path, arquivo)
            lista_arquivos.append(__)

    return sorted(lista_arquivos)


def verificar_pasta_existente(caminho_pasta: str) -> bool:
    if os.path.exists(caminho_pasta) and os.path.isdir(caminho_pasta):
        return True
    return False


""" FRONTEND """
layout = [
    [sg.Text("Caminho do arquivo json"), sg.Input(key="-PATH_JSON-"),
     sg.FileBrowse(button_text="Abrir Arquivo",
                   initial_folder="testes/ARQUIVOS_JSON")],
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
