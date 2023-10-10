from bs4 import BeautifulSoup


def create_context_html(path_file_html:str):
    with open(path_file_html,"r",encoding="latin-1") as file:
        html_content = file.read()
    return BeautifulSoup(html_content,"html.parser")



             
if __name__ == "__main__":
    path_html_file = "/home/mateus/projetos/gerenciador_de_log/arquivos_htmls/29 08 23.HTML"
    print(create_context_html(path_html_file))