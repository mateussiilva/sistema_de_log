import os



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
