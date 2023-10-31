


def gravar_informações_uteis(dados_base) -> list:
    lista_impressoes_data = []
    for _  in dados_base:
        nome_arquivo = dados_base.get("ARQUIVO")
        # print(nome_arquivo)
        perfil_icc = dados_base.get('PERFIL ICC DE SAÍDA')
        quantidade = dados_base.get('QUANTIDADE DE CÓPIAS')
        data_envio = dados_base.get('INÍCIO, DATA E HORA DO RIP')
        dimensao = dados_base.get("DIMENS\u00c3O")
        if dimensao is not None:
            dimensao = "teste"
        lista_impressoes_data.append(
            [nome_arquivo,dimensao,perfil_icc,quantidade,data_envio])

    return lista_impressoes_data


if __name__ == "__main__":
    file_json = r"json_files/1904/01 09 23.json"
    dados_json = json_mat.read_json_file(file_json).get("imp_1")
    lista_dados = gravar_informações_uteis(dados_json)
    with open("arquivos_.txt","w+") as file:
        for linhas in lista_dados:
            l = linhas + "\n"
            file.write(l)