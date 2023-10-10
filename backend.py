
import files.html.pyhtml as pyhtml


def gravar_informações_uteis(dados_base) -> list:
    lista_impressoes_data = []
    for value  in dados_base.values():
        nome_arquivo = value.get("ARQUIVO")
        dimensao = value.get("DIMENS\u00c3O")
        perfil_icc = value.get('PERFIL ICC DE SAÍDA')
        quantidade = value.get('QUANTIDADE DE CÓPIAS')
        data_envio = value.get('INÍCIO, DATA E HORA DO RIP')
         
        lista_impressoes_data.append(
            [nome_arquivo,dimensao,perfil_icc,quantidade,data_envio])

    return lista_impressoes_data
    
    




if __name__ == "__main__":
    path_html_file = "/home/mateus/projetos/gerenciador_de_log/arquivos_htmls/29 08 23.HTML"
    content_html = pyhtml.create_context_html(path_html_file)
    list_dados = pyhtml.struct_base_file(content_html,"table")
    dicinarios_limpos = pyhtml.create_dict_dados(list_dados)
    for dados in dicinarios_limpos:
        print(dados)


