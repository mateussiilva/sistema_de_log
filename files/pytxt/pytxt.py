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
