# from pprint import pprint as print

impressao = {
        "IMPRESSORA": "AC-1904 W",
        "PORTA": "FILE:",
        "ARQUIVO": "Z:\\das minys\\CORRIDOS VERAO 2023\\ESTAPAS CONFERIDAS\\D201.tif",
        "TAMANHO DO ARQUIVO": "272461.8k",
        "AUTOR": "User",
        "TIPO DE TRABALHO": "Trabalho de Impress\u00e3o",
        "TIPO": "Arquivo TIFF",
        "AP\u00d3S A SA\u00cdDA": "Manter",
        "DIMENS\u00c3O": "150.0 x 100.0cm",
        "RESOLU\u00c7\u00c3O": "360.00 x 1800.00",
        "MODO DE CORES": "CMYK (2 bits)",
        "TIPO DE DIFUS\u00c3O": "Estoc\u00e1stico avan\u00e7ado 2",
        "MODO DE RENDERIZA\u00c7\u00c3O": "Alta Qualidade",
        "PERFIL ICC CINZA": "GRACoL2006_Coated1v2.icc",
        "PERFIL ICC RGB": "278523_0.icc",
        "PERFIL ICC CMYK": "ISOcoated_v2_eci.icc",
        "PERFIL ICC DE SA\u00cdDA": "GS1904W_HIPRO_BN30GR_360X1800_3P_BZRA.icc",
        "BITMAP EM CMYK": "Imagem",
        "CMYK VECTOR": "Colorim\u00e9trico Relativo",
        "CMYK TEXT": "Colorim\u00e9trico Relativo",
        "CMYK GRADIENT": "Colorim\u00e9trico Relativo",
        "BITMAP N\u00c3O-CMYK": "Imagem",
        "VETOR N\u00c3O-CMYK": "Colorim\u00e9trico Relativo",
        "TEXTO N\u00c3O-CMYK": "Colorim\u00e9trico Relativo",
        "DEGRADE N\u00c3O-CMYK": "Colorim\u00e9trico Relativo",
        "CORRE\u00c7\u00c3O DE CORES": "OK",
        "USAR O PERFIL ICC EMBUTIDO PARA CMYK": "N\u00e3o",
        "USAR O PERFIL ICC EMBUTIDO PARA RGB": "N\u00e3o",
        "USAR O PERFIL ICC EMBUTIDO PARA CINZA": "N\u00e3o",
        "UTILIZAR REMAPEAMENTO DE CORES SPOT": "N\u00e3o",
        "QUANTIDADE DE C\u00d3PIAS": "25",
        "N\u00daMERO DO PAINEL": "1",
        "N\u00daMERO DE P\u00c1GINAS": "1",
        "ENVIAR DATA": "9/1/2023 6:27 AM",
        "SOBREPOSI\u00c7\u00c3O": "0.500cm",
        "IN\u00cdCIO, DATA E HORA DO RIP": "06:27:34 01/09/2023",
        "TEMPO DE PREPARA\u00c7\u00c3O DO TRABALHO": "0.000000 sec",
        "INFORMA\u00c7\u00d5ES": "O trabalho foi executado com sucesso",
        "FINALIZA\u00c7\u00c3O, DATA E HORA DO RIP": "06:28:00 01/09/2023",
        "DURA\u00c7\u00c3O DO RIP": "26 seg"
    }

CHAVES = (
    'ARQUIVO',
    'DIMENSÃO',
    'INÍCIO, DATA E HORA DO RIP',
    'PERFIL ICC DE SAÍDA',
    'QUANTIDADE DE CÓPIAS',
)

for chave in impressao:
    if chave in CHAVES:
        print(impressao[chave])
# print(impressao)