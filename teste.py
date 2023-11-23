from pprint import pprint as print
import json
import PySimpleGUI as sg



impressao = {
        "ARQUIVO": "Z:\\das minys\\CORRIDOS VERAO 2023\\ESTAPAS CONFERIDAS\\D201.tif",
        "DIMENS\u00c3O": "150.0 x 100.0cm",
        "PERFIL ICC DE SA\u00cdDA": "GS1904W_HIPRO_BN30GR_360X1800_3P_BZRA.icc",
        "QUANTIDADE DE C\u00d3PIAS": "25",
        "IN\u00cdCIO, DATA E HORA DO RIP": "06:27:34 01/09/2023"
    }

def limpar_nome(texto):
    lista_texto = texto.split("\\")
    return lista_texto[len(lista_texto) -1]


def limpar_dimensao(texto):
    return float(texto.replace("cm","").split(" x ")[1])


with open("01 09 23.json","r") as file:
    dados = json.load(file)


def orgnizar_lista(dicionario,env):
    
    for chave,valor in dicionario.items():
        if chave == "DIMENSÃO":
            qtd_copias = int(dicionario["QUANTIDADE DE C\u00d3PIAS"])
            metros = str(round(qtd_copias * limpar_dimensao(valor))/100)
            env.append(metros)
        elif chave == "ARQUIVO":
            nome_limpo = limpar_nome(valor)
            env.append(nome_limpo)
        elif chave != "QUANTIDADE DE C\u00d3PIAS" and \
            chave != "PERFIL ICC DE SA\u00cdDA":
            env.append(valor)
                
            
    return env



def criar_matrix(dados:dict) -> list[list]:
    matrix = []
    tmp = []
    for _,dado in dados.items():
        tmp = orgnizar_lista(dado,tmp)
        matrix.append(tmp[:])
        tmp.clear()
        
    return matrix

matrix_de_dados= criar_matrix(dados)

# print(type(matrix_de_dados))
# print(matrix_de_dados)


largura_maxima_base = max(list(map(lambda li: len(li[0]), matrix_de_dados)))
print(largura_maxima_base)

headers = ["Nome do Arquivo","Quantide(metros)","Data e Hora da Impressão"]

layout = [
    [sg.Table(values=matrix_de_dados,
              headings=headers,
              enable_click_events=True,enable_events=True,
              col_widths=100,
              selected_row_colors="Red on Yellow",justification="center",
              auto_size_columns=True,size=(None,50),alternating_row_color="Gray")]
]


window = sg.Window(" ",layout)

while True:
    events,values = window.read()
    
    if events == sg.WIN_CLOSED:
        break
    
# window.close()

    
    


    