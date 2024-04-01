from bs4 import BeautifulSoup


class ParserHtml:

    def __init__(self, encode) -> None:
        self.encode = encode
        self.__chaves = (
            'ARQUIVO',
            'DIMENSÃO',
            'INÍCIO, DATA E HORA DO RIP',
            'PERFIL ICC DE SAÍDA',
            'QUANTIDADE DE CÓPIAS',
        )
    def list_dados(self, path_file_html, target_tag="table"):
        with open(path_file_html, "r", encoding=self.encode) as file:
            html_content = file.read()
        _ctx = BeautifulSoup(html_content, "html.parser")
        return list(_ctx.find_all(target_tag))


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
                    if chave in self.__chaves:
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

