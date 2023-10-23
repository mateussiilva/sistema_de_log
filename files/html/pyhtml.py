from bs4 import BeautifulSoup


def create_context_html(path_file_html:str):
    with open(path_file_html,"r",encoding="latin-1") as file:
        html_content = file.read()
    return BeautifulSoup(html_content,"html.parser")


def struct_base_file(content_html,target_tag):
    return list(content_html.find_all(target_tag))


def create_dict_dados(base_list):
    lista_dicionarios = []
    for tabela in base_list:
        chaves = list(
            map(
                lambda item: 
                item
                    .get_text().strip()
                    .replace(":", "").upper(),
                tabela.find_all("th")
                )
            )
        valores = list(
            map(
                lambda item: 
                item
                    .get_text()
                    .strip(), 
                tabela
                    .find_all("td")
                )
            )

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
             




if __name__ == "__main__":
    path_html_file = "/home/mateus/projetos/gerenciador_de_log/arquivos_htmls/29 08 23.HTML"
    content_html = create_context_html(path_html_file)
    list_dados = struct_base_file(content_html,"table")
    dicinarios_limpos = create_dict_dados(list_dados)
    for dados in dicinarios_limpos:
        print(dados)