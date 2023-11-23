from pprint import pprint as print

impressao = {
        "ARQUIVO": "Z:\\das minys\\CORRIDOS VERAO 2023\\ESTAPAS CONFERIDAS\\D201.tif",
        "DIMENS\u00c3O": "150.0 x 100.0cm",
        "PERFIL ICC DE SA\u00cdDA": "GS1904W_HIPRO_BN30GR_360X1800_3P_BZRA.icc",
        "QUANTIDADE DE C\u00d3PIAS": "25",
        "IN\u00cdCIO, DATA E HORA DO RIP": "06:27:34 01/09/2023"
    }



def limpar_dimensao(texto):
    return float(texto.replace("cm","").split(" x ")[1])



def orgnizar_lista(dicionario):
    tmp = []
    for chave,valor in impressao.items():
        if chave == "DIMENSÃO":
            qtd_copias = int(impressao["QUANTIDADE DE C\u00d3PIAS"])
            metros = qtd_copias * limpar_dimensao(valor)
            tmp.append(metros)
        else:
            tmp.append(valor)
            
    return tmp
            
    
    