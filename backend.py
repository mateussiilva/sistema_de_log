import os.path
import re
import sys
import argparse
import util.util as util
from bs4 import BeautifulSoup

PATTERN = re.compile(r"\n", re.I)


def get_td(txt):
    t = str(txt.get_text())
    return re.sub(PATTERN, "", t)


def criar_matrix_tabelas(contexto_html):
    return list(contexto_html.find_all("table"))


def criar_contexto_html(caminho_arquivo_html, codificação="latin-1"):
    with open(caminho_arquivo_html, "r", encoding=codificação) as file_html:
        html_content = file_html.read()
    return BeautifulSoup(html_content, 'html.parser')


def criar_dicionario_de_dados(matrix_tabelas):
    lista_ = []
    temp = []
    lista_dicionarios = []
    for tabela in matrix_tabelas:
        chaves = list(map(lambda item: item.get_text().strip().replace(":", "").upper(), tabela.find_all("th")))
        valores = list(map(lambda item: item.get_text().strip(), tabela.find_all("td")))

        # removendo o primeiro elemento
        valor_0 = chaves.pop(0)
        if valor_0 == "INICIAR TRABALHO DE RIP":
            # # removendo o ultimo elemento
            chaves.pop(len(chaves) - 1)
            dicionario = dict(zip(chaves, valores))
            chaves.clear()
            valores.clear()
            lista_dicionarios.append(dicionario.copy())
            dicionario.clear()

    dicionarios = {
        f"imp_{k}": v
        for k, v in enumerate(lista_dicionarios)
    }

    return dicionarios


def gerar_novo_nome(texto):
    path, arquivo = os.path.split(texto)
    novo_nome = arquivo.replace(".HTML", ".json")
    return novo_nome


if __name__ == "__main__":
    FOLDER_JSON_FILES = "arquivos_json"
    caminho_arquivo_html = ""
    nome_arquivo_json = os.path.join(FOLDER_JSON_FILES, gerar_novo_nome(caminho_arquivo_html))

    contexto_html = criar_contexto_html(caminho_arquivo_html)
    matrix_tabelas = criar_matrix_tabelas(contexto_html)
    dicionarios = criar_dicionario_de_dados(matrix_tabelas)

    util.gravar_arquivo_json(
        nome_arquivo=nome_arquivo_json,
        dicionario_dados=dicionarios
    )
