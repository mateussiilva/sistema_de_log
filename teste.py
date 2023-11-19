from pprint import pprint as print
import json

impressao = {
        "ARQUIVO": "Z:\\das minys\\CORRIDOS VERAO 2023\\ESTAPAS CONFERIDAS\\D201.tif",
        "DIMENS\u00c3O": "150.0 x 100.0cm",
        "PERFIL ICC DE SA\u00cdDA": "GS1904W_HIPRO_BN30GR_360X1800_3P_BZRA.icc",
        "QUANTIDADE DE C\u00d3PIAS": "25",
        "IN\u00cdCIO, DATA E HORA DO RIP": "06:27:34 01/09/2023"
    }


def limpar_dimensao(texto):
    return float(texto.replace("cm","").split(" x ")[1])


with open("01 09 23.json","r") as file:
    dados = json.load(file)

impressoes_moda = []
impressao_tactel = []
impressoes_papel = []

soma_moda = soma_painel = soma_papel = 0
for impressao,dado in dados.items():
    nome = dado.get("ARQUIVO").lower()
    # print(nome)
    if "das minys" in nome:
        quantidade_copias = int(dado.get("QUANTIDADE DE C\u00d3PIAS"))
        dimensao = limpar_dimensao(dado.get("DIMENS\u00c3O"))
        metros = (quantidade_copias * dimensao) // 100
        soma_moda += metros
        
    elif "tactel" in nome or "malha" in nome:
        quantidade_copias = int(dado.get("QUANTIDADE DE C\u00d3PIAS"))
        dimensao = limpar_dimensao(dado.get("DIMENS\u00c3O"))
        metros = (quantidade_copias * dimensao) // 100
        soma_painel += metros 


print(f"TOTAL DE IMPRESSÃO DE MODA: {soma_moda}")
print(f"TOTAL DE IMPRESSÃO DE PAINEL: {soma_painel}")